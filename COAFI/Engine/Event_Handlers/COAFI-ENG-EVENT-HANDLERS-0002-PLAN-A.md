---
title: "COAFI – Event Handlers Implementation Plan"
document_id: COAFI-ENG-EVENT-HANDLERS-0002-PLAN-A
version: v1.0.0
status: PROPOSAL
author: GAIA Platforms Initiative
date: 2025-04-27
tags:
  - COAFI
  - Event Handlers
  - Implementation Plan
  - Federation
  - BITT
  - Ethics
infoCode: INFO-PLAN
utids: TBD
---

### COAFI Event Handlers Implementation Plan

*GenAI Proposal Status: This document outlines a detailed implementation plan for the COAFI Event Handlers System based on the v1.0.0 specification. This is an AI-generated proposal and should be reviewed by domain experts before implementation.*

## 1. Component Design

### Handler Base Architecture

```typescript
// Base handler interface
abstract class BaseEventHandler<T extends EventPayload> {
  constructor(
    protected readonly bittClient: BITTClient,
    protected readonly registryClient: RegistryClient,
    protected readonly workflowEngine: WorkflowEngine
  ) {}

  // Core handler method
  public async handle(event: Event<T>): Promise<HandlerResult> {
    try {
      // Common pre-processing
      await this.logEventReceived(event);
      await this.validateEvent(event);

      // Handler-specific processing
      const result = await this.processEvent(event);

      // Common post-processing
      await this.logEventProcessed(event, result);
      return result;
    } catch (error) {
      return this.handleError(event, error);
    }
  }

  // Abstract methods to be implemented by specific handlers
  protected abstract validateEvent(event: Event<T>): Promise<void>;
  protected abstract processEvent(event: Event<T>): Promise<HandlerResult>;

  // Common utility methods
  protected async logEventReceived(event: Event<T>): Promise<void> {
    // Example BITT logging
    await this.bittClient.logEvent({
      type: 'EVENT_RECEIVED',
      payload: {
        eventId: event.id,
        eventType: event.type,
        timestamp: new Date().toISOString()
      },
      utids: event.utids // Assuming UTidS is part of the event or generated
    });
  }

  protected async logEventProcessed(event: Event<T>, result: HandlerResult): Promise<void> {
     // Example BITT logging
     await this.bittClient.logEvent({
      type: 'EVENT_PROCESSED',
      payload: {
        eventId: event.id,
        handlerType: this.constructor.name,
        result: result,
        timestamp: new Date().toISOString()
      },
      utids: event.utids
    });
  }

  protected async handleError(event: Event<T>, error: any): Promise<HandlerResult> {
      // Example BITT logging for errors
      await this.bittClient.logEvent({
        type: 'EVENT_PROCESSING_FAILED',
        payload: {
          eventId: event.id,
          handlerType: this.constructor.name,
          error: error.message,
          stack: error.stack, // Optional: include stack trace
          timestamp: new Date().toISOString()
        },
        utids: event.utids
      });
      // Return a standardized error result
      return { success: false, message: error.message || 'Unknown error occurred' };
  }

  // Additional common methods...
}
```

### Handler-Specific Designs

#### GitCommitHandler

```typescript
// Assuming definitions for Event, GitCommitPayload, HandlerResult, ChangedFile, FileProcessingResult exist
// Assuming clients BITTClient, RegistryClient, GitClient exist
// Assuming services SchemaValidator, GeneratorService, WorkflowEngine exist

class GitCommitHandler extends BaseEventHandler<GitCommitPayload> {
  constructor(
    bittClient: BITTClient,
    registryClient: RegistryClient,
    workflowEngine: WorkflowEngine,
    private readonly schemaValidator: SchemaValidator,
    private readonly gitClient: GitClient,
    private readonly generatorService: GeneratorService
  ) {
    super(bittClient, registryClient, workflowEngine);
  }

  protected async validateEvent(event: Event<GitCommitPayload>): Promise<void> {
    // Validate commit payload structure against a predefined schema
    // Example: Check for presence and format of repositoryUrl, commitSha, etc.
    const schema = await this.registryClient.getSchema('GitCommitEventPayload'); // Fetch schema definition
    await this.schemaValidator.validate(event.payload, schema);
    console.log(`Validated GitCommitEvent payload for event: ${event.id}`);
  }

  protected async processEvent(event: Event<GitCommitPayload>): Promise<HandlerResult> {
    // 1. Extract commit details
    const { repositoryUrl, commitSha, branch, author } = event.payload;
    console.log(`Processing commit ${commitSha} for repo ${repositoryUrl}`);

    // 2. Get affected files from Git
    const changedFiles = await this.gitClient.getChangedFiles(repositoryUrl, commitSha);
    console.log(`Found ${changedFiles.length} changed files.`);

    // 3. Process each file based on type (validation, generation)
    const fileResults = await Promise.all(
      changedFiles.map(file => this.processFile(repositoryUrl, commitSha, file))
    );

    // 4. Trigger appropriate workflows based on results
    // Example: Start a workflow to update documentation indices or notify teams
    const workflowId = await this.workflowEngine.startWorkflow(
      'GitCommitProcessingWorkflow', // Name of the workflow to start
      { // Input payload for the workflow
        commitSha,
        repositoryUrl,
        branch,
        author,
        fileResults // Pass results of file processing
      }
    );
    console.log(`Started workflow ${workflowId} for commit ${commitSha}`);

    // 5. Return success result
    return {
      success: true,
      workflowId,
      message: `Successfully processed ${changedFiles.length} files from commit ${commitSha}. Workflow ${workflowId} started.`
    };
  }

  // Helper method to process an individual file
  private async processFile(
    repositoryUrl: string,
    commitSha: string,
    file: ChangedFile
  ): Promise<FileProcessingResult> {
    console.log(`Processing file: ${file.path}`);
    // Fetch file content
    const fileContent = await this.gitClient.getFileContent(repositoryUrl, commitSha, file.path);

    // Determine file type (e.g., based on extension or path)
    const fileType = this.determineFileType(file.path);

    // Validate file content against its specific schema
    const validationResult = await this.validateFileContent(fileType, fileContent);

    // Generate artifacts if validation passes and generation is applicable
    let generationResult = null;
    if (validationResult.valid && this.shouldGenerateArtifacts(fileType)) {
      generationResult = await this.generatorService.generateArtifacts(fileType, fileContent);
      console.log(`Generated artifacts for ${file.path}`);
    }

    // Log file processing details to BITT (optional, depends on granularity)
    await this.bittClient.logEvent({
        type: 'FILE_PROCESSED',
        payload: { filePath: file.path, commitSha, validation: validationResult.valid, generation: !!generationResult },
        utids: generateUTidS() // Generate relevant UTidS
    });


    return {
      path: file.path,
      fileType,
      validationResult,
      generationResult
    };
  }

  // Placeholder for determining file type logic
  private determineFileType(filePath: string): string {
      if (filePath.endsWith('.md')) return 'markdown';
      if (filePath.endsWith('.yaml') || filePath.endsWith('.yml')) return 'yaml_config';
      if (filePath.endsWith('.json')) return 'json_data';
      // Add more types as needed
      return 'unknown';
  }

  // Placeholder for validating file content against schema
  private async validateFileContent(fileType: string, content: string): Promise<{ valid: boolean; errors?: string[] }> {
      console.log(`Validating content for file type: ${fileType}`);
      // Fetch schema for fileType from registryClient
      // Use schemaValidator to validate content
      // Return { valid: true } or { valid: false, errors: [...] }
      return { valid: true }; // Placeholder
  }

    // Placeholder for deciding if artifacts should be generated
  private shouldGenerateArtifacts(fileType: string): boolean {
      // Example: Only generate for markdown or specific config files
      return ['markdown'].includes(fileType);
  }

  // Additional helper methods...
}
```

#### APIRequestHandler

```typescript
// Assuming definitions for Event, APIRequestPayload, HandlerResult exist
// Assuming clients BITTClient, RegistryClient exist
// Assuming services SchemaValidator, AuthenticationService, WorkflowEngine exist

class APIRequestHandler extends BaseEventHandler<APIRequestPayload> {
  constructor(
    bittClient: BITTClient,
    registryClient: RegistryClient,
    workflowEngine: WorkflowEngine,
    private readonly schemaValidator: SchemaValidator, // Added for consistency
    private readonly authService: AuthenticationService
  ) {
    super(bittClient, registryClient, workflowEngine);
  }

  protected async validateEvent(event: Event<APIRequestPayload>): Promise<void> {
    // 1. Validate basic request structure
    if (!event.payload || !event.payload.endpoint || !event.payload.method || !event.payload.requestId) {
        throw new Error("Invalid API request event structure");
    }
    console.log(`Validating API request ${event.payload.requestId} for endpoint ${event.payload.endpoint}:${event.payload.method}`);

    // 2. Validate request body against endpoint-specific schema
    const schemaId = `APIRequest.${event.payload.endpoint}.${event.payload.method}`; // Example schema ID convention
    const schema = await this.registryClient.getSchema(schemaId);
    await this.schemaValidator.validate(event.payload.body, schema);

    // 3. Validate authentication token (if provided)
    if (event.payload.authToken) {
        await this.authService.validateToken(event.payload.authToken);
    } else {
        // Handle cases where authentication is required but no token provided
        // This might depend on the specific endpoint's policy
        console.warn(`No auth token provided for request ${event.payload.requestId}`);
    }

    // 4. Check authorization based on token/identity and required permissions
    const requiredPermission = `api:${event.payload.endpoint}:${event.payload.method}`;
    await this.authService.checkPermission(event.payload.authToken, requiredPermission); // Assumes token contains identity info
    console.log(`Authorization successful for request ${event.payload.requestId}`);
  }

  protected async processEvent(event: Event<APIRequestPayload>): Promise<HandlerResult> {
    // Process based on endpoint and method
    const { endpoint, method, body, requestId } = event.payload;
    console.log(`Processing API request ${requestId} for ${endpoint}:${method}`);

    // Route to appropriate handler method within this class
    const handlerMethodName = `handle_${endpoint.replace(/\//g, '_')}_${method.toLowerCase()}`; // e.g., handle_registry_update_post

    if (typeof (this as any)[handlerMethodName] === 'function') {
      return await (this as any)[handlerMethodName](body, requestId);
    } else {
      console.error(`Unsupported endpoint/method: ${endpoint}:${method}`);
      throw new Error(`Unsupported endpoint: ${endpoint} with method ${method}`);
    }
  }

  // --- Endpoint-specific handlers ---

  // Example for POST /registry/update
  private async handle_registry_update_post(body: any, requestId: string): Promise<HandlerResult> {
    console.log(`Handling registry update for request ${requestId}`);
    // 1. Extract data from body
    const { registryId, entryId, data } = body;

    // 2. Interact with RegistryClient
    const updateResult = await this.registryClient.updateEntry(registryId, entryId, data);

    // 3. Optionally trigger a workflow
    const workflowId = await this.workflowEngine.startWorkflow('RegistryUpdateNotificationWorkflow', { registryId, entryId, updateResult });

    // 4. Return result
    return {
      success: true,
      message: `Registry entry ${entryId} in ${registryId} updated successfully.`,
      data: updateResult, // Optionally return updated data
      workflowId
    };
  }

  // Example for POST /workflow/start
  private async handle_workflow_start_post(body: any, requestId: string): Promise<HandlerResult> {
      console.log(`Handling workflow start request ${requestId}`);
      const { workflowName, inputPayload } = body;

      if (!workflowName) {
          throw new Error("Missing workflowName in request body");
      }

      const workflowId = await this.workflowEngine.startWorkflow(workflowName, inputPayload);

      return {
          success: true,
          message: `Workflow ${workflowName} started successfully.`,
          workflowId
      };
  }

  // Add more handler methods for other endpoints...
}
```

### Event Dispatcher Design

```typescript
// Assuming definitions for EventBus, HandlerRegistry, BITTClient, ConcurrencyManager exist
// Assuming specific handler classes like GitCommitHandler, APIRequestHandler exist

class EventDispatcher {
  constructor(
    private readonly eventBus: EventBus, // Listens for events from various sources
    private readonly handlerRegistry: HandlerRegistry, // Maps event types to handler instances
    private readonly bittClient: BITTClient, // For logging dispatch activities
    private readonly concurrencyManager: ConcurrencyManager // Manages parallel execution limits
  ) {}

  public async initialize(): Promise<void> {
    // Register event listeners for each source type defined in the specification
    await this.registerGitEventListener();
    await this.registerAPIEventListener();
    await this.registerBITTEventListener();
    await this.registerFederatedMessageListener();
    await this.registerScheduledTaskListener();
    console.log("Event Dispatcher initialized and listeners registered.");
  }

  // Example listener registration
  private async registerGitEventListener(): Promise<void> {
    // Subscribe to specific Git events from the event bus
    this.eventBus.subscribe('git.commit', async (event: Event<GitCommitPayload>) => {
      await this.dispatchEvent('GitCommitHandler', event); // Route to the correct handler type
    });
    // Potentially subscribe to other git events like 'git.tag', 'git.push'
    console.log("Registered listener for 'git.commit' events.");
  }

  private async registerAPIEventListener(): Promise<void> {
      // Assuming API gateway or framework pushes validated requests onto the bus
      this.eventBus.subscribe('api.request', async (event: Event<APIRequestPayload>) => {
          await this.dispatchEvent('APIRequestHandler', event);
      });
      console.log("Registered listener for 'api.request' events.");
  }

  private async registerBITTEventListener(): Promise<void> {
      // Implementation depends on BITT client's ability to subscribe to ledger events
      // This might involve polling or a websocket connection provided by bittClient
      // Example:
      // this.bittClient.subscribeToEvents(async (bittEvent) => {
      //     const event = this.transformBITTEvent(bittEvent); // Transform to standard Event format
      //     await this.dispatchEvent('BITTEventHandler', event);
      // });
      console.log("Registered listener for BITT events (implementation specific).");
  }

  private async registerFederatedMessageListener(): Promise<void> {
      // Implementation depends on the federated communication system (e.g., message queue like RabbitMQ, Kafka)
      // Example:
      // const messageQueueClient = this.getMessageQueueClient();
      // messageQueueClient.subscribe('gaia.federated.messages', async (message) => {
      //     const event = this.transformFederatedMessage(message); // Transform to standard Event format
      //     await this.dispatchEvent('FederatedMessageHandler', event);
      // });
      console.log("Registered listener for Federated Messages (implementation specific).");
  }

    private async registerScheduledTaskListener(): Promise<void> {
      // Implementation depends on the scheduler used (e.g., cron, internal timer)
      // Example: Using node-cron or similar
      // schedule.scheduleJob('0 * * * *', async () => { // Run hourly
      //     const event = this.createScheduledTaskEvent('HourlyReportTask');
      //     await this.dispatchEvent('ScheduledTaskHandler', event);
      // });
      console.log("Registered listener for Scheduled Tasks (implementation specific).");
  }


  // Central dispatch logic
  private async dispatchEvent(handlerType: string, event: Event<any>): Promise<void> {
    console.log(`Dispatching event ${event.id} to handler ${handlerType}`);
    try {
      // 1. Get appropriate handler instance from the registry
      const handler = this.handlerRegistry.getHandler(handlerType);
      if (!handler) {
          throw new Error(`No handler registered for type: ${handlerType}`);
      }

      // 2. Acquire concurrency slot (throttling/rate limiting)
      await this.concurrencyManager.acquireSlot(handlerType); // Throws error or waits if limit reached

      try {
        // 3. Process the event using the handler's handle method
        const result = await handler.handle(event);

        // 4. Log successful handling to BITT (already done within BaseEventHandler.handle)
        // Optional: Add specific dispatch success log here if needed
        console.log(`Event ${event.id} handled successfully by ${handlerType}. Result:`, result);

      } finally {
        // 5. Always release the concurrency slot
        this.concurrencyManager.releaseSlot(handlerType);
        console.log(`Concurrency slot released for handler ${handlerType}`);
      }
    } catch (error) {
      // 6. Log dispatch or handling failure to BITT
      console.error(`Error dispatching/handling event ${event.id} for handler ${handlerType}:`, error);
      await this.bittClient.logEvent({
        type: 'EVENT_DISPATCH_FAILED',
        payload: {
          eventId: event.id,
          handlerType,
          error: error.message,
          stack: error.stack // Optional
        },
        utids: event.utids // Use original event's UTidS if available
      });

      // 7. Decide whether to move to dead letter queue based on error type
      if (this.shouldMoveToDeadLetterQueue(error)) {
        console.log(`Moving event ${event.id} to dead letter queue.`);
        await this.eventBus.publish('deadletter', {
          originalEvent: event,
          error: error.message,
          timestamp: new Date().toISOString()
        });
      }
      // Depending on policy, might re-throw error or just log
    }
  }

  // Helper to decide if an error warrants moving to DLQ
  private shouldMoveToDeadLetterQueue(error: any): boolean {
      // Example logic: Don't move for validation errors (client issue),
      // but do move for unexpected processing errors after retries fail.
      // This needs refinement based on specific error types.
      return !(error instanceof ValidationError); // Simple example
  }
}
```

## 2. Proof of Concept Implementation

### Minimal Event Dispatcher

```typescript
// src/dispatcher.ts
import { EventEmitter } from 'events';
import { v4 as uuidv4 } from 'uuid';
import { GitCommitHandler } from './handlers/git-commit-handler'; // Assuming handler exists
import { BITTClient } from './clients/bitt-client'; // Assuming mock client exists
import { RegistryClient } from './clients/registry-client'; // Assuming mock client exists
import { WorkflowEngine } from './services/workflow-engine'; // Assuming mock service exists
import { SchemaValidator } from './services/schema-validator'; // Assuming mock service exists
import { GitClient } from './clients/git-client'; // Assuming mock client exists
import { GeneratorService } from './services/generator-service'; // Assuming mock service exists

// Define simple types for PoC
type Event<T> = { id: string; type: string; timestamp: string; payload: T; utids: string };
type GitCommitPayload = { commitSha: string; repositoryUrl: string; branch: string; author: string; message: string };
type HandlerResult = { success: boolean; message: string; [key: string]: any };


// Simple in-memory event bus implementation for PoC
class SimpleEventBus {
  private emitter = new EventEmitter();

  public subscribe(eventType: string, callback: (event: Event<any>) => Promise<void>): void {
    this.emitter.on(eventType, callback);
  }

  public publish(eventType: string, payload: any): void {
    const event: Event<any> = {
        id: uuidv4(),
        type: eventType,
        timestamp: new Date().toISOString(),
        payload: payload,
        utids: uuidv4() // Simplified UTidS generation for PoC
    };
    console.log(`Publishing event: ${eventType} - ID: ${event.id}`);
    this.emitter.emit(eventType, event);
  }
}

// Minimal dispatcher implementation for PoC
export class MinimalDispatcher {
  private eventBus = new SimpleEventBus();
  // Use Mock Clients/Services for PoC
  private bittClient = new BITTClient();
  private registryClient = new RegistryClient();
  private workflowEngine = new WorkflowEngine();
  private schemaValidator = new SchemaValidator();
  private gitClient = new GitClient();
  private generatorService = new GeneratorService();

  // Instantiate handlers with mock dependencies
  private gitCommitHandler = new GitCommitHandler(
      this.bittClient,
      this.registryClient,
      this.workflowEngine,
      this.schemaValidator,
      this.gitClient, // Pass mock GitClient
      this.generatorService
  );

  constructor() {
    // Register handler for git commit events
    this.eventBus.subscribe('git.commit', async (event: Event<GitCommitPayload>) => {
      try {
        console.log(`Minimal Dispatcher: Received git commit event: ${event.id}`);
        // Directly call the handler's handle method for simplicity in PoC
        const result = await this.gitCommitHandler.handle(event);
        console.log(`Minimal Dispatcher: Successfully processed event ${event.id}:`, result);
      } catch (error) {
        console.error(`Minimal Dispatcher: Error processing event ${event.id}:`, error);
        // Basic error logging for PoC
        await this.bittClient.logEvent({
            type: 'POC_EVENT_PROCESSING_FAILED',
            payload: { eventId: event.id, error: error.message },
            utids: event.utids
        });
      }
    });
    console.log("Minimal Dispatcher Initialized.");
  }

  // Method to simulate a git commit event for testing PoC
  public simulateGitCommit(payload: GitCommitPayload): void {
    this.eventBus.publish('git.commit', payload);
  }
}
```

### GitCommitHandler Implementation (Simplified for PoC)

```typescript
// src/handlers/git-commit-handler.ts
// Simplified BaseEventHandler for PoC - assumes Event, HandlerResult types exist
abstract class BaseEventHandlerPOC<T> {
    constructor(
        protected readonly bittClient: BITTClient,
        protected readonly registryClient: RegistryClient,
        protected readonly workflowEngine?: WorkflowEngine // Optional for simpler handlers
    ) {}

    public async handle(event: Event<T>): Promise<HandlerResult> {
        try {
            await this.logEventReceived(event); // Log receipt
            await this.validateEvent(event);    // Validate
            const result = await this.processEvent(event); // Process
            await this.logEventProcessed(event, result); // Log success
            return result;
        } catch (error) {
            return this.handleError(event, error); // Log error
        }
    }
    // Abstract methods
    protected abstract validateEvent(event: Event<T>): Promise<void>;
    protected abstract processEvent(event: Event<T>): Promise<HandlerResult>;
    // Simplified logging/error methods for PoC
    protected async logEventReceived(event: Event<T>) { /* PoC Log */ console.log(`[BasePOC] Received Event: ${event.id}`); }
    protected async logEventProcessed(event: Event<T>, result: HandlerResult) { /* PoC Log */ console.log(`[BasePOC] Processed Event: ${event.id}, Success: ${result.success}`); }
    protected async handleError(event: Event<T>, error: any): Promise<HandlerResult> {
        console.error("[BasePOC] Handler Error:", error.message);
        await this.bittClient.logEvent({ type: 'HANDLER_ERROR', payload: { eventId: event.id, error: error.message }, utids: event.utids });
        return { success: false, message: error.message };
    }
}


// Simplified GitCommitHandler for PoC
export class GitCommitHandler extends BaseEventHandlerPOC<GitCommitPayload> {
  // GitClient is now passed in constructor for consistency with BaseEventHandler
  constructor(
    bittClient: BITTClient,
    registryClient: RegistryClient,
    workflowEngine: WorkflowEngine,
    private readonly schemaValidator: SchemaValidator,
    private readonly gitClient: GitClient, // Injected dependency
    private readonly generatorService: GeneratorService
  ) {
    super(bittClient, registryClient, workflowEngine);
  }

  protected async validateEvent(event: Event<GitCommitPayload>): Promise<void> {
    // Simplified validation for PoC
    console.log(`PoC Validate: Event ${event.id}`);
    if (!event.payload?.commitSha || !event.payload?.repositoryUrl) {
      throw new Error('PoC Validation Failed: Missing commitSha or repositoryUrl');
    }
    // Example: Use schemaValidator if needed (even if mock)
    // await this.schemaValidator.validate(event.payload, {});
  }

  protected async processEvent(event: Event<GitCommitPayload>): Promise<HandlerResult> {
    console.log(`PoC Process: Event ${event.id}, Commit: ${event.payload.commitSha}`);
    // Use injected GitClient
    const changedFiles = await this.gitClient.getChangedFiles(
      event.payload.repositoryUrl,
      event.payload.commitSha
    );

    // Simulate processing each file
    const results = await Promise.all(changedFiles.map(async file => {
        // Simulate getting content too
        await this.gitClient.getFileContent(event.payload.repositoryUrl, event.payload.commitSha, file.path);
        return {
            path: file.path,
            type: this.getFileType(file.path), // Use helper
            valid: this.simulateValidation(), // Use helper
            processed: true
        };
    }));


    console.log(`PoC Process: Processed ${results.length} files.`);

    // Simulate starting a workflow using injected engine
     if (this.workflowEngine) {
        const workflowId = await this.workflowEngine.startWorkflow('PoCGitWorkflow', { commit: event.payload.commitSha, files: results });
        console.log(`PoC Process: Started workflow ${workflowId}`);
        return { success: true, filesProcessed: results.length, results, workflowId };
     } else {
        return { success: true, filesProcessed: results.length, results };
     }
  }

  // --- Helper methods (can be reused from full implementation) ---
   private getFileType(filePath: string): string {
    if (filePath.endsWith('.md')) return 'markdown';
    if (filePath.endsWith('.yaml') || filePath.endsWith('.yml')) return 'yaml';
    if (filePath.endsWith('.json')) return 'json';
    return 'unknown';
  }

  private simulateValidation(): boolean {
    return Math.random() > 0.1; // 90% success for PoC
  }
}
```

### Mock Clients (Simplified for PoC)

```typescript
// src/clients/bitt-client.ts
export class BITTClient {
  public async logEvent(event: any): Promise<void> {
    console.log('[PoC BITT Log]:', JSON.stringify(event.type, null, 2)); // Log only type for brevity
  }
}

// src/clients/registry-client.ts
export class RegistryClient {
  public async getSchema(schemaId: string): Promise<any> {
    console.log(`[PoC Registry]: Requesting schema ${schemaId}`);
    return { type: 'object', properties: {} }; // Minimal valid schema
  }
   public async updateEntry(registryId: string, entryId: string, data: any): Promise<any> {
    console.log(`[PoC Registry]: Updating ${registryId}/${entryId}`);
    return { id: entryId, status: 'updated' };
  }
}

// src/clients/git-client.ts
export class GitClient {
  public async getChangedFiles(repositoryUrl: string, commitSha: string): Promise<any[]> {
    console.log(`[PoC Git]: Getting changed files for ${commitSha}`);
    return [
      { path: 'README.md', status: 'modified' },
      { path: 'config.yaml', status: 'added' }
    ];
  }
  public async getFileContent(repositoryUrl: string, commitSha: string, filePath: string): Promise<string> {
     console.log(`[PoC Git]: Getting content for ${filePath}`);
    return `# Mock Content for ${filePath}`;
  }
}

// src/services/workflow-engine.ts (Mock)
export class WorkflowEngine {
    public async startWorkflow(workflowName: string, inputPayload: any): Promise<string> {
        const workflowId = `wf-${uuidv4().substring(0, 8)}`;
        console.log(`[PoC Workflow]: Starting ${workflowName} with ID ${workflowId}`);
        return workflowId;
    }
}

// src/services/schema-validator.ts (Mock)
export class SchemaValidator {
    public async validate(data: any, schema: any): Promise<void> {
        console.log(`[PoC Validator]: Validating data against schema`);
        // In PoC, assume validation passes if schema exists
        if (!schema) throw new Error("Schema not found for validation");
    }
}

// src/services/generator-service.ts (Mock)
export class GeneratorService {
    public async generateArtifacts(fileType: string, content: string): Promise<any> {
        console.log(`[PoC Generator]: Generating artifacts for type ${fileType}`);
        return { artifactPath: `/generated/${fileType}_artifact.out` };
    }
}

// src/services/authentication-service.ts (Mock)
export class AuthenticationService {
    public async validateToken(token: string | undefined): Promise<void> {
         console.log(`[PoC Auth]: Validating token`);
         if (!token) console.warn("No token provided for validation");
         // Assume valid for PoC
    }
     public async checkPermission(token: string | undefined, permission: string): Promise<void> {
         console.log(`[PoC Auth]: Checking permission '${permission}'`);
         // Assume authorized for PoC
    }
}
```

### Usage Example (PoC)

```typescript
// src/index.ts
import { MinimalDispatcher } from './dispatcher';
// Define or import the necessary types if not globally available
type GitCommitPayload = { commitSha: string; repositoryUrl: string; branch: string; author: string; message: string };

async function main() {
  console.log("--- Starting COAFI Event Handler PoC ---");
  // Create dispatcher
  const dispatcher = new MinimalDispatcher();

  // Simulate a git commit event
  const commitPayload: GitCommitPayload = {
    commitSha: 'poc-sha-12345',
    repositoryUrl: '[https://github.com/gaia-platforms/poc-repo](https://github.com/gaia-platforms/poc-repo)',
    branch: 'main',
    author: 'poc-dev@example.com',
    message: 'Proof of Concept Commit'
  };
  dispatcher.simulateGitCommit(commitPayload);

  // Keep process alive briefly to see logs
  await new Promise(resolve => setTimeout(resolve, 500)); // Wait 0.5 seconds

  console.log("--- COAFI Event Handler PoC Finished ---");
}

main().catch(error => {
    console.error("PoC execution failed:", error);
    process.exit(1);
});
```

## 3. Testing Framework

### Testing Strategy

#### Unit Testing

```typescript
// tests/unit/handlers/git-commit-handler.test.ts
import { GitCommitHandler } from '../../../src/handlers/git-commit-handler';
import { BITTClient } from '../../../src/clients/bitt-client';
import { RegistryClient } from '../../../src/clients/registry-client';
import { GitClient } from '../../../src/clients/git-client';
import { WorkflowEngine } from '../../../src/services/workflow-engine';
import { SchemaValidator } from '../../../src/services/schema-validator';
import { GeneratorService } from '../../../src/services/generator-service';

// Define or import necessary types
type Event<T> = { id: string; type: string; timestamp: string; payload: T; utids: string };
type GitCommitPayload = { commitSha: string; repositoryUrl: string; branch: string; author: string; message: string };


// Mock dependencies using Jest
jest.mock('../../../src/clients/bitt-client');
jest.mock('../../../src/clients/registry-client');
jest.mock('../../../src/clients/git-client');
jest.mock('../../../src/services/workflow-engine');
jest.mock('../../../src/services/schema-validator');
jest.mock('../../../src/services/generator-service');

describe('GitCommitHandler Unit Tests (PoC)', () => {
  let handler: GitCommitHandler;
  // Create typed mock instances
  let mockBittClient: jest.Mocked<BITTClient>;
  let mockRegistryClient: jest.Mocked<RegistryClient>;
  let mockWorkflowEngine: jest.Mocked<WorkflowEngine>;
  let mockSchemaValidator: jest.Mocked<SchemaValidator>;
  let mockGitClient: jest.Mocked<GitClient>;
  let mockGeneratorService: jest.Mocked<GeneratorService>;

  beforeEach(() => {
    // Create new mock instances for each test
    mockBittClient = new BITTClient() as jest.Mocked<BITTClient>;
    mockRegistryClient = new RegistryClient() as jest.Mocked<RegistryClient>;
    mockWorkflowEngine = new WorkflowEngine() as jest.Mocked<WorkflowEngine>;
    mockSchemaValidator = new SchemaValidator() as jest.Mocked<SchemaValidator>;
    mockGitClient = new GitClient() as jest.Mocked<GitClient>;
    mockGeneratorService = new GeneratorService() as jest.Mocked<GeneratorService>;

    // Instantiate the handler with mocks
    handler = new GitCommitHandler(
        mockBittClient,
        mockRegistryClient,
        mockWorkflowEngine,
        mockSchemaValidator,
        mockGitClient, // Pass mock GitClient
        mockGeneratorService
    );
  });

  test('should handle valid git commit event successfully', async () => {
    // Arrange
    const mockEvent: Event<GitCommitPayload> = { // Use defined type
      id: 'unit-test-event-1',
      type: 'git.commit',
      timestamp: '2025-04-27T14:00:00Z',
      payload: {
        commitSha: 'abc123xyz',
        repositoryUrl: '[https://github.com/test/repo](https://github.com/test/repo)',
        branch: 'main',
        author: 'test@example.com',
        message: 'Valid commit'
      },
      utids: 'utids-123'
    };

    // Mock GitClient responses
    mockGitClient.getChangedFiles.mockResolvedValue([
      { path: 'README.md', status: 'modified' },
      { path: 'src/code.ts', status: 'added' }
    ]);
    mockGitClient.getFileContent.mockResolvedValue('# Test Content'); // Mock content for all files

    // Mock WorkflowEngine response
    mockWorkflowEngine.startWorkflow.mockResolvedValue('wf-unit-test-1');

    // Act
    const result = await handler.handle(mockEvent);

    // Assert
    expect(result.success).toBe(true);
    expect(result.filesProcessed).toBe(2);
    expect(result.workflowId).toBe('wf-unit-test-1');
    expect(mockGitClient.getChangedFiles).toHaveBeenCalledWith(
      '[https://github.com/test/repo](https://github.com/test/repo)',
      'abc123xyz'
    );
    expect(mockGitClient.getFileContent).toHaveBeenCalledTimes(2);
    expect(mockWorkflowEngine.startWorkflow).toHaveBeenCalledWith(
        'PoCGitWorkflow', // Or the actual workflow name
        expect.objectContaining({ commit: 'abc123xyz' })
    );
     // Verify base class logs (optional, depends on needs)
    // expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'EVENT_RECEIVED' }));
    // expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'EVENT_PROCESSED' }));
  });

  test('should reject if validation fails (e.g., missing commitSha)', async () => {
    // Arrange
    const invalidEvent: Event<any> = { // Use 'any' for invalid payload test
      id: 'unit-test-event-invalid',
      type: 'git.commit',
      timestamp: '2025-04-27T14:05:00Z',
      payload: { repositoryUrl: '[https://github.com/test/repo](https://github.com/test/repo)' /* Missing commitSha */ },
      utids: 'utids-456'
    };

    // Act & Assert
    // Expect the handle method to reject because validateEvent will throw
    await expect(handler.handle(invalidEvent)).rejects.toThrow('PoC Validation Failed');

    // Verify the error was logged via the base class handleError
    // Need to wait for potential async error logging if not awaited in handle
    await new Promise(process.nextTick);
    expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'HANDLER_ERROR' }));
  });

  // Add more unit tests for different scenarios:
  // - Different file types (.yaml, .json) -> check getFileType logic
  // - Test simulateValidation branches (if made more complex)
  // - Error during gitClient.getChangedFiles call
  // - Error during gitClient.getFileContent call
  // - Error during workflowEngine.startWorkflow call
});
```

#### Integration Testing

```typescript
// tests/integration/git-workflow.test.ts
import { MinimalDispatcher } from '../../src/dispatcher'; // Use the PoC dispatcher
import { BITTClient } from '../../src/clients/bitt-client';
import { GitClient } from '../../src/clients/git-client';
import { WorkflowEngine } from '../../src/services/workflow-engine';
import { RegistryClient } from '../../src/clients/registry-client';
import { SchemaValidator } from '../../src/services/schema-validator';
import { GeneratorService } from '../../src/services/generator-service';

// Mock only the truly external dependencies or those hard to set up
jest.mock('../../src/clients/bitt-client');
// jest.mock('../../src/clients/git-client'); // Maybe let this run partially? Depends.
jest.mock('../../src/services/workflow-engine');
// Let RegistryClient, SchemaValidator, GeneratorService run with their mock implementations

describe('Git Commit Workflow Integration Test (PoC)', () => {
  let dispatcher: MinimalDispatcher;
  let mockBittClient: jest.Mocked<BITTClient>;
  let mockGitClient: jest.Mocked<GitClient>; // Still mock Git for controlled file lists
  let mockWorkflowEngine: jest.Mocked<WorkflowEngine>;

  beforeEach(() => {
    // Reset mocks
    jest.resetAllMocks();

    // Create specific mock instances
    mockBittClient = new BITTClient() as jest.Mocked<BITTClient>;
    mockGitClient = new GitClient() as jest.Mocked<GitClient>;
    mockWorkflowEngine = new WorkflowEngine() as jest.Mocked<WorkflowEngine>;

    // --- Setup Mocks ---
    // Mock BITT logging
    mockBittClient.logEvent.mockResolvedValue(undefined);

    // Mock GitClient to return specific files for this test
    mockGitClient.getChangedFiles.mockResolvedValue([
        { path: 'integration/README.md', status: 'modified' },
        { path: 'integration/config.yaml', status: 'added' }
    ]);
    mockGitClient.getFileContent.mockResolvedValue('# Integration Test Content');

    // Mock Workflow Engine start
    mockWorkflowEngine.startWorkflow.mockResolvedValue('wf-integration-test-123');


    // --- Inject Mocks ---
    // Use jest.spyOn to replace methods on the *actual* instances used by dispatcher
    // This requires knowing how dispatcher gets its dependencies. Assuming it news them up:
    jest.spyOn(BITTClient.prototype, 'logEvent').mockImplementation(mockBittClient.logEvent);
    jest.spyOn(GitClient.prototype, 'getChangedFiles').mockImplementation(mockGitClient.getChangedFiles);
    jest.spyOn(GitClient.prototype, 'getFileContent').mockImplementation(mockGitClient.getFileContent);
    jest.spyOn(WorkflowEngine.prototype, 'startWorkflow').mockImplementation(mockWorkflowEngine.startWorkflow);
    // No need to mock RegistryClient, SchemaValidator, GeneratorService if using their simple mock classes

    // Instantiate dispatcher AFTER spies are set up
    dispatcher = new MinimalDispatcher();
  });

  test('should process git commit event end-to-end through dispatcher', async () => {
    // Arrange
    const commitPayload = {
      commitSha: 'integration-sha-abc',
      repositoryUrl: '[https://github.com/gaia-platforms/integration-repo](https://github.com/gaia-platforms/integration-repo)',
      branch: 'develop',
      author: 'integ-test@example.com',
      message: 'Integration test commit'
    };

    // Act
    dispatcher.simulateGitCommit(commitPayload);

    // Wait for async operations within the handler to likely complete
    await new Promise(resolve => setTimeout(resolve, 150)); // Adjust timing

    // Assert
    // Verify external calls were made as expected
    expect(mockGitClient.getChangedFiles).toHaveBeenCalledWith(
      '[https://github.com/gaia-platforms/integration-repo](https://github.com/gaia-platforms/integration-repo)',
      'integration-sha-abc'
    );
    expect(mockGitClient.getFileContent).toHaveBeenCalledTimes(2); // For README.md and config.yaml

    expect(mockWorkflowEngine.startWorkflow).toHaveBeenCalledWith(
        'PoCGitWorkflow', // Or actual name
        expect.objectContaining({ // Check parts of the payload sent to workflow
            commit: 'integration-sha-abc',
            files: expect.arrayContaining([
                expect.objectContaining({ path: 'integration/README.md', type: 'markdown' }),
                expect.objectContaining({ path: 'integration/config.yaml', type: 'yaml' })
            ])
        })
    );

    // Check BITT logging calls (adjust count based on BaseEventHandlerPOC logging)
    // Example: Check specific log types
    expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'HANDLER_ERROR' })); // From BaseEventHandlerPOC.handleError (if error occurred)
    // Or check for success logs if expecting success
    // expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'EVENT_RECEIVED' })); // From BaseEventHandlerPOC
    // expect(mockBittClient.logEvent).toHaveBeenCalledWith(expect.objectContaining({ type: 'EVENT_PROCESSED' })); // From BaseEventHandlerPOC


  });

  // Add more integration tests:
  // - Test API request flow (requires mocking API input source)
  // - Test scenario where file validation fails inside the handler
  // - Test scenario where workflow start fails
});
```

#### Load Testing

```typescript
// tests/load/dispatcher-load.test.ts
import { MinimalDispatcher } from '../../src/dispatcher';
import { performance } from 'perf_hooks'; // Use Node.js performance hooks
import { GitCommitHandler } from '../../src/handlers/git-commit-handler'; // Import the actual handler

// --- Mock the dependencies of the handler itself ---
// We want the handler logic to run, but not its external calls
jest.mock('../../src/clients/bitt-client', () => {
    return { BITTClient: jest.fn().mockImplementation(() => ({ logEvent: jest.fn().mockResolvedValue(undefined) })) };
});
jest.mock('../../src/clients/registry-client', () => {
    return { RegistryClient: jest.fn().mockImplementation(() => ({ getSchema: jest.fn().mockResolvedValue({}) })) };
});
jest.mock('../../src/clients/git-client', () => {
    return { GitClient: jest.fn().mockImplementation(() => ({
        getChangedFiles: jest.fn().mockResolvedValue([{ path: 'load.md' }]), // Always return one file
        getFileContent: jest.fn().mockResolvedValue('#Load Test')
    })) };
});
jest.mock('../../src/services/workflow-engine', () => {
    return { WorkflowEngine: jest.fn().mockImplementation(() => ({ startWorkflow: jest.fn().mockResolvedValue('wf-load-test') })) };
});
jest.mock('../../src/services/schema-validator', () => {
    return { SchemaValidator: jest.fn().mockImplementation(() => ({ validate: jest.fn().mockResolvedValue(undefined) })) };
});
jest.mock('../../src/services/generator-service', () => {
    return { GeneratorService: jest.fn().mockImplementation(() => ({ generateArtifacts: jest.fn().mockResolvedValue(null) })) };
});


describe('Dispatcher Load Test (PoC)', () => {
  let dispatcher: MinimalDispatcher;

  beforeEach(() => {
     // Reset mocks if needed (though they are mocked per test file)
     jest.clearAllMocks();
     // Instantiate the dispatcher - it will create handlers which use the mocks defined above
     dispatcher = new MinimalDispatcher();
  });

  test('should handle a high volume of git commit events within performance threshold', async () => {
    // Arrange
    const eventCount = 500; // Number of events to simulate
    const eventsPayloads = [];
    for (let i = 0; i < eventCount; i++) {
        eventsPayloads.push({
            commitSha: `load-test-sha-${i}`,
            repositoryUrl: '[https://github.com/gaia-platforms/load-test-repo](https://github.com/gaia-platforms/load-test-repo)',
            branch: 'main',
            author: 'load-tester@example.com',
            message: `Load test commit ${i}`
        });
    }

    const startTime = performance.now();

    // Act - Dispatch all events - let dispatcher handle async calls
    eventsPayloads.forEach(payload => dispatcher.simulateGitCommit(payload));

    // Wait for processing to likely complete. This is tricky.
    // A better approach in a real app would be to track completion.
    // For PoC, estimate a reasonable time based on expected handler execution.
    await new Promise(resolve => setTimeout(resolve, 2000)); // Wait 2 seconds

    const endTime = performance.now();
    const duration = endTime - startTime;

    // Assert
    console.log(`\n--- Load Test Results ---`);
    console.log(`Dispatched ${eventCount} events in ${duration.toFixed(2)}ms`);
    console.log(`Approx Average time per event (incl. dispatch + mock handling): ${(duration / eventCount).toFixed(3)}ms`);

    // Check if the mocked calls were made approximately the right number of times
    // Note: Exact counts depend on BaseEventHandlerPOC logging logic
    // Example: Check a call made once per event processed
    // const mockWorkflowStart = (WorkflowEngine as jest.Mock).mock.instances[0].startWorkflow;
    // expect(mockWorkflowStart).toHaveBeenCalledTimes(eventCount);


    // Define a performance threshold (e.g., average total time < 15ms)
    const averageTimeThreshold = 15; // milliseconds - adjust based on complexity
    expect(duration / eventCount).toBeLessThan(averageTimeThreshold);

  }, 20000); // Increase Jest timeout for load tests

});
```

### Test Configuration

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest', // Use ts-jest preset for TypeScript
  testEnvironment: 'node', // Running tests in Node.js environment
  roots: ['<rootDir>/tests'], // Look for tests in the tests directory
  collectCoverage: true, // Enable coverage collection
  collectCoverageFrom: [ // Specify files to include in coverage
    'src/**/*.ts', // Include all TypeScript files in src
    '!src/index.ts', // Exclude main entry point if it just calls bootstrap logic
    '!src/**/*.d.ts', // Exclude TypeScript definition files
    '!src/types.ts', // Exclude type definition files
    '!src/clients/**', // Exclude mock clients from coverage
    '!src/services/**', // Exclude mock services from coverage
  ],
  coverageThreshold: { // Define minimum coverage requirements
    global: { // Apply thresholds globally
      branches: 70, // Example: 70% branch coverage
      functions: 75, // Example: 75% function coverage
      lines: 75,     // Example: 75% line coverage
      statements: 75 // Example: 75% statement coverage
    }
  },
  testMatch: [ // Patterns Jest uses to detect test files
    '**/tests/unit/**/*.test.ts', // Match unit tests
    '**/tests/integration/**/*.test.ts' // Match integration tests
  ],
  testPathIgnorePatterns: [ // Patterns to ignore
    '/node_modules/', // Ignore node_modules
    '/dist/',         // Ignore build output directory
    '/tests/load/'    // Ignore load tests (run separately)
  ],
   // Optional: Setup file to run before each test file (e.g., for global mocks)
  // setupFilesAfterEnv: ['./tests/setup.ts'],
  // Optional: Clear mocks between tests
  clearMocks: true,
};
```

## 4. Deployment Strategy

### CI/CD Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: COAFI Event Handlers CI/CD

on:
  push:
    branches: [ main, develop ] # Trigger on pushes to main and develop
  pull_request:
    branches: [ main, develop ] # Trigger on pull requests to main and develop
  workflow_dispatch: # Allow manual triggering

jobs:
  # Job to run tests and linting
  test:
    name: Test & Lint
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4 # Use latest checkout action

      - name: Setup Node.js
        uses: actions/setup-node@v4 # Use latest Node setup action
        with:
          node-version: '18.x' # Specify Node.js version
          cache: 'npm' # Enable npm caching

      - name: Install dependencies
        run: npm ci # Use ci for clean installs

      - name: Run Linter (e.g., ESLint)
        run: npm run lint # Assumes lint script exists in package.json

      - name: Run Unit Tests with Coverage
        run: npm run test:unit -- --coverage # Assumes test:unit script exists

      - name: Run Integration Tests
        run: npm run test:integration # Assumes test:integration script exists

      - name: Upload Coverage Report to Codecov
        uses: codecov/codecov-action@v4 # Use latest Codecov action
        with:
          token: ${{ secrets.CODECOV_TOKEN }} # Securely stored token
          fail_ci_if_error: true # Optional: Fail CI if upload fails

  # Job to build the application
  build:
    name: Build Application
    needs: test # Run only after tests pass
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build TypeScript
        run: npm run build # Assumes build script compiles TS to JS in ./dist

      - name: Upload build artifact
        uses: actions/upload-artifact@v4 # Use latest upload action
        with:
          name: dist-artifact # Name of the artifact
          path: dist/ # Path to the build output

  # Job to build and push Docker image
  build-and-push-docker:
      name: Build & Push Docker Image
      needs: build # Run only after build is successful
      runs-on: ubuntu-latest
      permissions:
          contents: read
          packages: write # Permission to write to GitHub Packages (or configure for ECR/other)
      outputs: # Define outputs for image tag
          image_tag: ${{ steps.meta.outputs.version }} # Use version generated by metadata action
      steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          # Example for GitHub Packages (adjust for ECR/Docker Hub)
          - name: Log in to GitHub Container Registry
            uses: docker/login-action@v3
            with:
              registry: ghcr.io
              username: ${{ github.actor }}
              password: ${{ secrets.GITHUB_TOKEN }} # Use default token

          - name: Extract metadata (tags, labels) for Docker
            id: meta
            uses: docker/metadata-action@v5
            with:
              images: ghcr.io/${{ github.repository_owner }}/coafi-event-handlers # Adjust image name
              tags: | # Define tagging strategy
                  type=sha,prefix=,suffix=,format=short
                  type=ref,event=branch
                  type=ref,event=pr
                  type=semver,pattern={{version}}
                  type=semver,pattern={{major}}.{{minor}}

          - name: Build and push Docker image
            uses: docker/build-push-action@v5
            with:
              context: .
              push: ${{ github.event_name != 'pull_request' }} # Push only if not a PR
              tags: ${{ steps.meta.outputs.tags }}
              labels: ${{ steps.meta.outputs.labels }}
              cache-from: type=gha
              cache-to: type=gha,mode=max


  # Job to deploy to Development environment
  deploy-dev:
    name: Deploy to Development
    needs: build-and-push-docker # Run after Docker image is ready
    runs-on: ubuntu-latest
    environment: development # Define environment in GitHub settings
    if: github.ref == 'refs/heads/develop' # Deploy only from develop branch

    steps:
      - name: Checkout repository (for deployment scripts/configs if needed)
        uses: actions/checkout@v4

      # Add steps for deployment (e.g., update K8s manifest, trigger ECS update)
      # Example for Kubernetes using kubectl
      - name: Configure Kubeconfig (using secret)
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.KUBECONFIG_DEV }}" > $HOME/.kube/config
          chmod 600 $HOME/.kube/config

      - name: Update Kubernetes Deployment Image
        run: |
          IMAGE_TAG=${{ needs.build-and-push-docker.outputs.image_tag }} # Get tag from build job
          kubectl set image deployment/coafi-event-handlers \
            event-handlers=ghcr.io/${{ github.repository_owner }}/coafi-event-handlers:$IMAGE_TAG \
            -n coafi-dev --record # Specify namespace


  # Job to deploy to Production environment
  deploy-prod:
    name: Deploy to Production
    needs: build-and-push-docker # Run after Docker image is ready
    runs-on: ubuntu-latest
    environment: production # Define environment with approval rules
    if: github.ref == 'refs/heads/main' # Deploy only from main branch

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      # Add steps for production deployment (similar to dev, but target prod env)
      - name: Configure Kubeconfig (using secret)
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.KUBECONFIG_PROD }}" > $HOME/.kube/config
          chmod 600 $HOME/.kube/config

      - name: Update Kubernetes Deployment Image
        run: |
          IMAGE_TAG=${{ needs.build-and-push-docker.outputs.image_tag }} # Get tag from build job
          kubectl set image deployment/coafi-event-handlers \
            event-handlers=ghcr.io/${{ github.repository_owner }}/coafi-event-handlers:$IMAGE_TAG \
            -n coafi-prod --record # Specify namespace
```

### Containerization

```dockerfile
# Dockerfile

# ---- Builder Stage ----
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies using npm ci for consistency
# Use --omit=dev if you have separate devDependencies not needed for build
RUN npm ci

# Copy source code and build configuration
COPY tsconfig.json ./
COPY src/ ./src/

# Run the build script defined in package.json
RUN npm run build
# Optional: Prune development dependencies after build if needed
# RUN npm prune --production

# ---- Production Stage ----
FROM node:18-alpine

WORKDIR /app

# Copy only necessary package files for production dependencies
COPY package*.json ./
# Install only production dependencies
RUN npm ci --omit=dev # Use --omit=dev (npm v7+) or --production (older npm)

# Copy built application code from the builder stage
# Ensure the path matches your build output directory (e.g., dist)
COPY --from=builder /app/dist ./dist

# Copy configuration files if they are needed at runtime and not mounted as volumes/configmaps
# COPY config/ ./config/

# Set environment variables for production
ENV NODE_ENV=production
ENV PORT=8080 # Default port

# Expose the port the application will run on
EXPOSE 8080

# Add a basic health check endpoint (adjust path as needed)
# This assumes your application listens on /health for health checks
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:${PORT}/health || exit 1
  # Alternative using curl: CMD curl --fail http://localhost:${PORT}/health || exit 1

# Define the command to run your application
# Adjust the path to your main entry file (e.g., dist/index.js)
CMD ["node", "dist/index.js"]
```

### Kubernetes Deployment

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: coafi-event-handlers # Name of the deployment
  namespace: coafi # Target namespace
  labels:
    app: coafi-event-handlers # Label for selection
spec:
  replicas: 3 # Start with 3 replicas, managed by HPA later
  selector:
    matchLabels:
      app: coafi-event-handlers # Select pods with this label
  strategy:
    type: RollingUpdate # Use rolling update strategy
    rollingUpdate:
      maxSurge: 25% # Allow 25% extra pods during update
      maxUnavailable: 25% # Allow 25% of pods to be unavailable during update
  template:
    metadata:
      labels:
        app: coafi-event-handlers # Pods get this label
    spec:
      serviceAccountName: coafi-event-handlers # Optional: Specific service account
      containers:
      - name: event-handlers # Name of the container
        # Image URL will be dynamically set by CI/CD pipeline (e.g., kubectl set image)
        image: placeholder-registry/coafi-event-handlers:placeholder-tag
        imagePullPolicy: IfNotPresent # Or Always, depending on tag strategy
        ports:
        - containerPort: 8080 # Port exposed by the container
          name: http
          protocol: TCP
        resources: # Define resource requests and limits
          requests:
            cpu: "100m" # 0.1 vCPU
            memory: "256Mi" # 256 Megabytes
          limits:
            cpu: "500m" # 0.5 vCPU
            memory: "512Mi" # 512 Megabytes
        env: # Environment variables
        - name: NODE_ENV
          value: "production"
        - name: PORT # Ensure container uses this port
          value: "8080"
          # --- Configuration via ConfigMap ---
        - name: BITT_API_URL
          valueFrom:
            configMapKeyRef:
              name: coafi-config # Name of the ConfigMap
              key: bitt-api-url # Key within the ConfigMap
        - name: REGISTRY_API_URL
          valueFrom:
            configMapKeyRef:
              name: coafi-config
              key: registry-api-url
          # --- Secrets via Kubernetes Secrets ---
        - name: AUTH_SECRET # Example secret
          valueFrom:
            secretKeyRef:
              name: coafi-secrets # Name of the Secret object
              key: auth-secret # Key within the Secret
        # --- Liveness and Readiness Probes ---
        livenessProbe: # Check if the container is alive
          httpGet:
            path: /health # Path to the health check endpoint
            port: http # Use the named port 'http'
          initialDelaySeconds: 30 # Wait 30s before first probe
          periodSeconds: 15 # Probe every 15s
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe: # Check if the container is ready to serve traffic
          httpGet:
            path: /ready # Path to the readiness check endpoint (might be same as /health)
            port: http
          initialDelaySeconds: 10 # Wait 10s before first probe
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
      # Optional: Define volumes, security context, etc.
---
# kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: coafi-event-handlers # Name of the service
  namespace: coafi # Target namespace
  labels:
    app: coafi-event-handlers
spec:
  selector:
    app: coafi-event-handlers # Select pods with this label
  ports:
  - name: http
    port: 80 # Port the service listens on internally
    targetPort: http # Forward traffic to the container's 'http' port (8080)
    protocol: TCP
  type: ClusterIP # Internal service type (use LoadBalancer or NodePort for external access if needed)
```

### Horizontal Pod Autoscaler

```yaml
# kubernetes/hpa.yaml
apiVersion: autoscaling/v2 # Use v2 for resource metrics
kind: HorizontalPodAutoscaler
metadata:
  name: coafi-event-handlers # Name of the HPA resource
  namespace: coafi # Target namespace
spec:
  scaleTargetRef: # Reference to the deployment to scale
    apiVersion: apps/v1
    kind: Deployment
    name: coafi-event-handlers # Must match the Deployment name
  minReplicas: 3 # Minimum number of pods
  maxReplicas: 10 # Maximum number of pods
  metrics: # Define metrics for scaling
  - type: Resource # Scale based on CPU utilization
    resource:
      name: cpu
      target:
        type: Utilization # Target average utilization across all pods
        averageUtilization: 70 # Target 70% CPU utilization
  - type: Resource # Scale based on Memory utilization
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80 # Target 80% Memory utilization
  # Optional: Add custom metrics (e.g., queue length) if needed via custom metrics API
  # - type: Pods | Object | External | Resource ...
  behavior: # Fine-tune scaling behavior
    scaleUp:
      stabilizationWindowSeconds: 60 # Wait 60s after last scale-up before allowing another
      policies: # Define how aggressively to scale up
      - type: Percent
        value: 100 # Add 100% of current replicas (max 4 pods) per evaluation period
        periodSeconds: 60
      - type: Pods
        value: 4 # Add max 4 pods per evaluation period
        periodSeconds: 60
      selectPolicy: Max # Use the policy that allows the biggest increase
    scaleDown:
      stabilizationWindowSeconds: 300 # Wait 5 minutes after last scale-down before allowing another
      policies: # Define how conservatively to scale down
      - type: Percent
        value: 50 # Remove 50% of current replicas per evaluation period
        periodSeconds: 60
      selectPolicy: Max # Use the policy that allows the biggest decrease (most conservative here)
```

### Infrastructure as Code (Terraform)

```hcl
# terraform/main.tf

# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
}

# --- ECR Repository ---
module "ecr" {
  source          = "./modules/ecr" # Assuming a local module for ECR
  repository_name = "coafi-event-handlers-${var.environment}" # Environment-specific name
  # Add other ECR configurations like image scanning, lifecycle policies etc.
}

# --- ECS Cluster & Service ---
module "ecs_service" {
  source = "./modules/ecs_service" # Assuming a local module for ECS Service + Task Def

  # Cluster Info
  cluster_name = "coafi-${var.environment}"

  # Service Info
  service_name        = "coafi-event-handlers"
  desired_count       = var.service_min_replicas # Start with min replicas
  launch_type         = "FARGATE" # Or EC2
  platform_version    = "LATEST"  # For Fargate

  # Networking
  vpc_id              = var.vpc_id
  subnet_ids          = var.private_subnet_ids # Run service in private subnets
  security_group_ids  = [aws_security_group.ecs_service_sg.id]
  assign_public_ip    = false # For private subnets

  # Task Definition Info
  task_family         = "coafi-event-handlers-${var.environment}"
  task_cpu            = var.task_cpu    # e.g., "512" (0.5 vCPU for Fargate)
  task_memory         = var.task_memory # e.g., "1024" (1GB for Fargate)
  container_image     = "${module.ecr.repository_url}:${var.image_tag}" # Use tag passed from CI/CD
  container_port      = 8080
  container_name      = "event-handlers"
  log_group_name      = aws_cloudwatch_log_group.event_handlers_log_group.name
  aws_region          = var.aws_region

  # Environment Variables from ConfigMap/Secrets equivalent
  environment_variables = {
    NODE_ENV           = var.environment
    PORT               = "8080"
    BITT_API_URL       = data.aws_ssm_parameter.bitt_api_url.value
    REGISTRY_API_URL   = data.aws_ssm_parameter.registry_api_url.value
  }
  secret_variables = {
    AUTH_SECRET        = aws_ssm_parameter.auth_secret.name # Pass SSM Parameter name/ARN
  }

  # Health Check (optional, can be defined in container defs too)
  # health_check_path = "/health"

  # Optional: Load Balancer config if service needs external access
  # load_balancer_config = { ... }

  tags = {
    Environment = var.environment
    Project     = "GAIA-Platforms"
    Component   = "COAFI-EventHandlers"
  }
}

# --- Security Group ---
resource "aws_security_group" "ecs_service_sg" {
  name        = "coafi-event-handlers-sg-${var.environment}"
  description = "Allow traffic to COAFI Event Handlers ECS service"
  vpc_id      = var.vpc_id

  # Example Ingress: Allow traffic from within VPC (e.g., from API Gateway or other services)
  ingress {
    description = "Allow internal traffic on container port"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr_block] # Or specific subnet CIDRs / Security Group IDs
  }

  # Allow all outbound traffic (adjust if needed)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "coafi-event-handlers-sg-${var.environment}"
    Environment = var.environment
  }
}

# --- CloudWatch Log Group ---
resource "aws_cloudwatch_log_group" "event_handlers_log_group" {
  name              = "/ecs/coafi-event-handlers-${var.environment}"
  retention_in_days = 30 # Example retention

  tags = {
    Environment = var.environment
    Project     = "GAIA-Platforms"
  }
}

# --- SSM Parameters for Secrets/Config ---
# Fetch existing parameters (assuming they are created separately/securely)
data "aws_ssm_parameter" "bitt_api_url" {
  name = "/coafi/${var.environment}/config/bitt-api-url"
}

data "aws_ssm_parameter" "registry_api_url" {
  name = "/coafi/${var.environment}/config/registry-api-url"
}

# Reference the secure string parameter for the secret
resource "aws_ssm_parameter" "auth_secret" {
  # This defines the parameter if it doesn't exist,
  # or you can use a data source if it's managed elsewhere.
  # For secrets, it's often better to manage them outside main TF state.
  # This is just an example structure.
  name  = "/coafi/${var.environment}/secrets/event-handlers/auth-secret"
  type  = "SecureString"
  value = var.auth_secret_value # Pass the actual secret value securely (e.g., via tfvars marked sensitive)

  tags = {
    Environment = var.environment
  }
  # Add lifecycle ignore_changes if value managed externally
}

# --- Variables ---
variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
}

variable "environment" {
  description = "Deployment environment (e.g., dev, staging, prod)"
  type        = string
}

variable "image_tag" {
  description = "Docker image tag to deploy"
  type        = string
}

variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "private_subnet_ids" {
  description = "List of private subnet IDs for ECS tasks"
  type        = list(string)
}

variable "vpc_cidr_block" {
  description = "CIDR block of the VPC"
  type        = string
}

variable "service_min_replicas" {
  description = "Minimum number of tasks for the ECS service"
  type        = number
  default     = 3
}

variable "task_cpu" {
  description = "CPU units for the ECS task"
  type        = string
  default     = "512"
}

variable "task_memory" {
  description = "Memory for the ECS task"
  type        = string
  default     = "1024"
}
```
