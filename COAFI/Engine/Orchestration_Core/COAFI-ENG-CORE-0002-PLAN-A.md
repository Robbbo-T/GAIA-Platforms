---
title: "COAFI – Orchestration Core Phase 1 Implementation Guide"
document_id: COAFI-ENG-ORCHCORE-0002-PLAN-A
version: v0.9.2-PRELIMINARY
status: PROPOSAL
author: GAIA Platforms Initiative
date: 2025-04-27
tags:
  - COAFI
  - Orchestration Core
  - Temporal
  - Federation
  - Infrastructure-as-Code
  - PostgreSQL
  - Kubernetes
  - Terraform
infoCode: INFO-PLAN
utids: TBD
---


### COAFI Orchestration Core - Phase 1 Implementation Guide

*GenAI Proposal Status: This document provides implementation guidance for the initial phase of the COAFI Orchestration Core. This is an AI-generated proposal and should be reviewed by domain experts before implementation.*

## 1. Setting Up Temporal Server Infrastructure

Temporal is a distributed, scalable workflow engine that will serve as the foundation for the COAFI Orchestration Core. Let's set it up using Docker Compose for development and Kubernetes for production.

### Development Setup with Docker Compose

First, create a `docker-compose.yml` file in your project root:

```yaml
version: '3.8'

services:
  postgresql:
    image: postgres:14
    environment:
      POSTGRES_USER: temporal
      POSTGRES_PASSWORD: temporal
      POSTGRES_DB: temporal
    ports:
      - 5432:5432
    volumes:
      - postgresql-data:/var/lib/postgresql/data
    networks:
      - temporal-network

  temporal:
    image: temporalio/auto-setup:1.20.0
    depends_on:
      - postgresql
    environment:
      - DB=postgresql
      - DB_PORT=5432
      - POSTGRES_USER=temporal
      - POSTGRES_PWD=temporal
      - POSTGRES_SEEDS=postgresql
      - DYNAMIC_CONFIG_FILE_PATH=config/dynamicconfig/development.yaml
    ports:
      - 7233:7233
    volumes:
      - ./temporal-config:/etc/temporal/config/dynamicconfig
    networks:
      - temporal-network

  temporal-admin-tools:
    image: temporalio/admin-tools:1.20.0
    depends_on:
      - temporal
    environment:
      - TEMPORAL_CLI_ADDRESS=temporal:7233
    networks:
      - temporal-network

  temporal-ui:
    image: temporalio/ui:2.10.3
    depends_on:
      - temporal
    environment:
      - TEMPORAL_ADDRESS=temporal:7233
      - TEMPORAL_CORS_ORIGINS=http://localhost:3000
    ports:
      - 8080:8080
    networks:
      - temporal-network

networks:
  temporal-network:
    driver: bridge

volumes:
  postgresql-data:
```

Create a directory for Temporal configuration:

```shellscript
mkdir -p temporal-config
```

Create a basic dynamic configuration file at `temporal-config/development.yaml`:

```yaml
frontend.enableClientVersionCheck:
  - value: true
    constraints: {}
system.enableVisibility:
  - value: true
    constraints: {}
history.persistenceMaxQPS:
  - value: 3000
    constraints: {}
frontend.persistenceMaxQPS:
  - value: 3000
    constraints: {}
frontend.historyMgrNumConns:
  - value: 10
    constraints: {}
frontend.throttledLogRPS:
  - value: 20
    constraints: {}
history.historyMgrNumConns:
  - value: 50
    constraints: {}
system.advancedVisibilityWritingMode:
  - value: "off"
    constraints: {}
```

Start the Temporal server:

```shellscript
docker-compose up -d
```

Verify the setup by accessing the Temporal UI at [http://localhost:8080](http://localhost:8080).

### Production Setup with Kubernetes

For production, create Kubernetes manifests in a `k8s` directory:

1. Create a namespace:


```yaml
# k8s/00-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: coafi-temporal
```

2. Create a ConfigMap for Temporal configuration:


```yaml
# k8s/01-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: temporal-config
  namespace: coafi-temporal
data:
  dynamicconfig.yaml: |
    frontend.enableClientVersionCheck:
      - value: true
        constraints: {}
    system.enableVisibility:
      - value: true
        constraints: {}
    history.persistenceMaxQPS:
      - value: 3000
        constraints: {}
    frontend.persistenceMaxQPS:
      - value: 3000
        constraints: {}
    frontend.historyMgrNumConns:
      - value: 10
        constraints: {}
    frontend.throttledLogRPS:
      - value: 20
        constraints: {}
    history.historyMgrNumConns:
      - value: 50
        constraints: {}
    system.advancedVisibilityWritingMode:
      - value: "off"
        constraints: {}
```

3. Create a Secret for database credentials:


```yaml
# k8s/02-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: temporal-postgresql
  namespace: coafi-temporal
type: Opaque
data:
  # Base64 encoded values (replace with your actual encoded values)
  username: dGVtcG9yYWw=  # "temporal"
  password: c2VjdXJlUGFzc3dvcmQ=  # "securePassword"
```

4. Create a StatefulSet for PostgreSQL:


```yaml
# k8s/03-postgresql.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgresql
  namespace: coafi-temporal
spec:
  serviceName: postgresql
  replicas: 1
  selector:
    matchLabels:
      app: postgresql
  template:
    metadata:
      labels:
        app: postgresql
    spec:
      containers:
      - name: postgresql
        image: postgres:14
        ports:
        - containerPort: 5432
          name: postgresql
        env:
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: temporal-postgresql
              key: username
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: temporal-postgresql
              key: password
        - name: POSTGRES_DB
          value: temporal
        volumeMounts:
        - name: postgresql-data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: postgresql-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi
---
apiVersion: v1
kind: Service
metadata:
  name: postgresql
  namespace: coafi-temporal
spec:
  selector:
    app: postgresql
  ports:
  - port: 5432
    targetPort: 5432
```

5. Deploy Temporal server:


```yaml
# k8s/04-temporal.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: temporal
  namespace: coafi-temporal
spec:
  replicas: 1
  selector:
    matchLabels:
      app: temporal
  template:
    metadata:
      labels:
        app: temporal
    spec:
      containers:
      - name: temporal
        image: temporalio/auto-setup:1.20.0
        env:
        - name: DB
          value: postgresql
        - name: DB_PORT
          value: "5432"
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: temporal-postgresql
              key: username
        - name: POSTGRES_PWD
          valueFrom:
            secretKeyRef:
              name: temporal-postgresql
              key: password
        - name: POSTGRES_SEEDS
          value: postgresql
        - name: DYNAMIC_CONFIG_FILE_PATH
          value: /etc/temporal/config/dynamicconfig/dynamicconfig.yaml
        ports:
        - containerPort: 7233
        volumeMounts:
        - name: config-volume
          mountPath: /etc/temporal/config/dynamicconfig
      volumes:
      - name: config-volume
        configMap:
          name: temporal-config
---
apiVersion: v1
kind: Service
metadata:
  name: temporal
  namespace: coafi-temporal
spec:
  selector:
    app: temporal
  ports:
  - port: 7233
    targetPort: 7233
```

6. Deploy Temporal UI:


```yaml
# k8s/05-temporal-ui.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: temporal-ui
  namespace: coafi-temporal
spec:
  replicas: 1
  selector:
    matchLabels:
      app: temporal-ui
  template:
    metadata:
      labels:
        app: temporal-ui
    spec:
      containers:
      - name: temporal-ui
        image: temporalio/ui:2.10.3
        env:
        - name: TEMPORAL_ADDRESS
          value: temporal:7233
        - name: TEMPORAL_CORS_ORIGINS
          value: "*"
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: temporal-ui
  namespace: coafi-temporal
spec:
  selector:
    app: temporal-ui
  ports:
  - port: 8080
    targetPort: 8080
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: temporal-ui-ingress
  namespace: coafi-temporal
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  rules:
  - host: temporal.coafi.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: temporal-ui
            port:
              number: 8080
```

Apply the Kubernetes manifests:

```shellscript
kubectl apply -f k8s/
```

### Create Temporal Namespaces for COAFI

Once Temporal is running, create namespaces for different environments:

```shellscript
# For development setup
docker-compose exec temporal-admin-tools tctl --namespace coafi-dev namespace register --retention 3

# For production setup (using kubectl)
kubectl exec -it -n coafi-temporal deployment/temporal -- tctl --namespace coafi-prod namespace register --retention 7
```

## 2. Implementing the WorkflowEngineInterface Adapter

Now, let's implement the WorkflowEngineInterface adapter for Temporal. First, set up a TypeScript project:

```shellscript
mkdir -p coafi-orchestration-core/src/{workflow-engine,state,models,utils}
cd coafi-orchestration-core
npm init -y
npm install typescript @types/node ts-node tsconfig-paths --save-dev
npm install @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/common uuid
```

Create a `tsconfig.json` file:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "declaration": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Define the WorkflowEngineInterface

Create the interface in `src/workflow-engine/interface.ts`:

```typescript
// src/workflow-engine/interface.ts
export interface WorkflowDefinition {
  id: string;
  name: string;
  version: string;
  steps: WorkflowStep[];
  triggers: WorkflowTrigger[];
  policies: string[];
}

export interface WorkflowStep {
  id: string;
  name: string;
  type: 'task' | 'subworkflow' | 'decision' | 'parallel';
  action: string;
  parameters: Record<string, any>;
  dependencies: string[];
  retryPolicy?: RetryPolicy;
  timeoutSeconds?: number;
}

export interface WorkflowTrigger {
  type: string;
  condition: Record<string, any>;
}

export interface RetryPolicy {
  maximumAttempts: number;
  initialInterval: number; // in milliseconds
  backoffCoefficient: number;
  maximumInterval?: number; // in milliseconds
}

export interface WorkflowOptions {
  taskQueue?: string;
  workflowId?: string;
  workflowRunTimeout?: number; // in milliseconds
  workflowTaskTimeout?: number; // in milliseconds
  retryPolicy?: RetryPolicy;
  searchAttributes?: Record<string, string[]>;
  memo?: Record<string, any>;
}

export interface WorkflowExecutionStatus {
  executionId: string;
  status: 'RUNNING' | 'COMPLETED' | 'FAILED' | 'CANCELED' | 'TERMINATED' | 'TIMED_OUT' | 'CONTINUED_AS_NEW';
  startTime: string;
  endTime?: string;
  workflowType: string;
  result?: any;
  error?: string;
}

export interface WorkflowEngineInterface {
  // Workflow management
  registerWorkflow(definition: WorkflowDefinition): Promise<void>;
  unregisterWorkflow(workflowId: string, version?: string): Promise<void>;
  
  // Workflow execution
  startWorkflow(workflowId: string, input: Record<string, any>, options?: WorkflowOptions): Promise<string>;
  getWorkflowStatus(executionId: string): Promise<WorkflowExecutionStatus>;
  terminateWorkflow(executionId: string, reason?: string): Promise<void>;
  
  // Task management
  completeTask(taskToken: string, result?: any): Promise<void>;
  failTask(taskToken: string, error: Error): Promise<void>;
  
  // Signals and queries
  signalWorkflow(executionId: string, signalName: string, payload?: any): Promise<void>;
  queryWorkflow(executionId: string, queryName: string, args?: any): Promise<any>;
}
```

### Create a Workflow Registry

Create a simple workflow registry in `src/workflow-engine/workflow-registry.ts`:

```typescript
// src/workflow-engine/workflow-registry.ts
import { WorkflowDefinition } from './interface';

export class WorkflowRegistry {
  private workflows: Map<string, WorkflowDefinition> = new Map();
  private workflowsByName: Map<string, WorkflowDefinition[]> = new Map();
  
  async registerWorkflow(definition: WorkflowDefinition): Promise<void> {
    // Store by ID
    this.workflows.set(definition.id, definition);
    
    // Store by name (for versioning)
    const existingVersions = this.workflowsByName.get(definition.name) || [];
    this.workflowsByName.set(definition.name, [...existingVersions, definition]);
    
    console.log(`Registered workflow: ${definition.name} (${definition.version})`);
  }
  
  async unregisterWorkflow(workflowId: string, version?: string): Promise<void> {
    const workflow = this.workflows.get(workflowId);
    
    if (!workflow) {
      throw new Error(`Workflow ${workflowId} not found`);
    }
    
    // If version is specified, only unregister that version
    if (version && workflow.version !== version) {
      throw new Error(`Workflow ${workflowId} with version ${version} not found`);
    }
    
    // Remove from workflows map
    this.workflows.delete(workflowId);
    
    // Remove from workflowsByName map
    const existingVersions = this.workflowsByName.get(workflow.name) || [];
    this.workflowsByName.set(
      workflow.name,
      existingVersions.filter(w => w.id !== workflowId)
    );
    
    console.log(`Unregistered workflow: ${workflow.name} (${workflow.version})`);
  }
  
  async getWorkflow(workflowId: string): Promise<WorkflowDefinition | null> {
    return this.workflows.get(workflowId) || null;
  }
  
  async getWorkflowByName(name: string, version?: string): Promise<WorkflowDefinition | null> {
    const workflows = this.workflowsByName.get(name) || [];
    
    if (version) {
      return workflows.find(w => w.version === version) || null;
    }
    
    // If no version specified, return the latest version
    return workflows.sort((a, b) => {
      return this.compareVersions(b.version, a.version);
    })[0] || null;
  }
  
  async listWorkflows(): Promise<WorkflowDefinition[]> {
    return Array.from(this.workflows.values());
  }
  
  private compareVersions(a: string, b: string): number {
    const aParts = a.split('.').map(Number);
    const bParts = b.split('.').map(Number);
    
    for (let i = 0; i < Math.max(aParts.length, bParts.length); i++) {
      const aPart = aParts[i] || 0;
      const bPart = bParts[i] || 0;
      
      if (aPart > bPart) return 1;
      if (aPart < bPart) return -1;
    }
    
    return 0;
  }
}
```

### Implement the Temporal Adapter

Now, implement the Temporal adapter in `src/workflow-engine/temporal-engine.ts`:

```typescript
// src/workflow-engine/temporal-engine.ts
import { 
  Client, 
  Connection, 
  WorkflowClient,
  WorkflowExecutionStatus as TemporalWorkflowExecutionStatus,
  WorkflowHandle
} from '@temporalio/client';
import { 
  WorkflowEngineInterface, 
  WorkflowDefinition, 
  WorkflowOptions,
  WorkflowExecutionStatus,
  RetryPolicy
} from './interface';
import { WorkflowRegistry } from './workflow-registry';
import { v4 as uuidv4 } from 'uuid';

export interface TemporalEngineOptions {
  address: string;
  namespace: string;
  taskQueue?: string;
  connectionOptions?: Connection.Options;
}

export class TemporalWorkflowEngine implements WorkflowEngineInterface {
  private client: WorkflowClient;
  private workflowRegistry: WorkflowRegistry;
  private defaultTaskQueue: string;
  
  constructor(options: TemporalEngineOptions) {
    const connectionOptions = options.connectionOptions || {};
    const connection = new Connection({
      address: options.address,
      ...connectionOptions
    });
    
    this.client = new Client({
      connection,
      namespace: options.namespace
    });
    
    this.workflowRegistry = new WorkflowRegistry();
    this.defaultTaskQueue = options.taskQueue || 'coafi-default';
    
    console.log(`Initialized Temporal Workflow Engine with namespace: ${options.namespace}`);
  }
  
  async registerWorkflow(definition: WorkflowDefinition): Promise<void> {
    // In Temporal, workflows are registered at worker startup
    // This method stores the workflow definition in our registry
    await this.workflowRegistry.registerWorkflow(definition);
  }
  
  async unregisterWorkflow(workflowId: string, version?: string): Promise<void> {
    await this.workflowRegistry.unregisterWorkflow(workflowId, version);
  }
  
  async startWorkflow(
    workflowId: string, 
    input: Record<string, any>, 
    options?: WorkflowOptions
  ): Promise<string> {
    const workflowInfo = await this.workflowRegistry.getWorkflow(workflowId);
    
    if (!workflowInfo) {
      throw new Error(`Workflow ${workflowId} not found`);
    }
    
    // Generate a unique execution ID
    const executionId = options?.workflowId || `${workflowInfo.name}-${uuidv4()}`;
    
    // Convert retry policy if provided
    const retryPolicy = options?.retryPolicy ? this.convertRetryPolicy(options.retryPolicy) : undefined;
    
    // Start the workflow
    const handle = await this.client.start(workflowInfo.name, {
      args: [input],
      taskQueue: options?.taskQueue || this.defaultTaskQueue,
      workflowId: executionId,
      retry: retryPolicy,
      searchAttributes: this.convertSearchAttributes(options?.searchAttributes),
      memo: options?.memo,
      workflowRunTimeout: options?.workflowRunTimeout ? `${options.workflowRunTimeout}ms` : undefined,
      workflowTaskTimeout: options?.workflowTaskTimeout ? `${options.workflowTaskTimeout}ms` : undefined,
    });
    
    console.log(`Started workflow: ${workflowInfo.name}, execution ID: ${executionId}`);
    
    return executionId;
  }
  
  async getWorkflowStatus(executionId: string): Promise<WorkflowExecutionStatus> {
    const handle = this.client.getHandle(executionId);
    
    try {
      const description = await handle.describe();
      
      let result: any = undefined;
      let error: string | undefined = undefined;
      
      // If workflow is completed, try to get the result
      if (description.status.name === 'COMPLETED') {
        try {
          result = await handle.result();
        } catch (err) {
          console.warn(`Failed to get result for workflow ${executionId}:`, err);
        }
      }
      
      // If workflow failed, try to get the error
      if (description.status.name === 'FAILED') {
        try {
          await handle.result();
        } catch (err) {
          error = err instanceof Error ? err.message : String(err);
        }
      }
      
      return {
        executionId,
        status: this.mapTemporalStatus(description.status.name),
        startTime: description.startTime.toISOString(),
        endTime: description.closeTime?.toISOString(),
        workflowType: description.workflowType.name,
        result,
        error
      };
    } catch (error) {
      throw new Error(`Failed to get workflow status: ${error instanceof Error ? error.message : String(error)}`);
    }
  }
  
  async terminateWorkflow(executionId: string, reason?: string): Promise<void> {
    const handle = this.client.getHandle(executionId);
    await handle.terminate({ reason });
    console.log(`Terminated workflow: ${executionId}, reason: ${reason || 'No reason provided'}`);
  }
  
  async completeTask(taskToken: string, result?: any): Promise<void> {
    // In Temporal, this would be handled by the worker SDK
    throw new Error('Task completion is handled by Temporal worker SDK');
  }
  
  async failTask(taskToken: string, error: Error): Promise<void> {
    // In Temporal, this would be handled by the worker SDK
    throw new Error('Task failure is handled by Temporal worker SDK');
  }
  
  async signalWorkflow(executionId: string, signalName: string, payload?: any): Promise<void> {
    const handle = this.client.getHandle(executionId);
    await handle.signal(signalName, payload);
    console.log(`Sent signal ${signalName} to workflow: ${executionId}`);
  }
  
  async queryWorkflow(executionId: string, queryName: string, args?: any): Promise<any> {
    const handle = this.client.getHandle(executionId);
    const result = await handle.query(queryName, args);
    return result;
  }
  
  // Helper methods
  private mapTemporalStatus(status: string): WorkflowExecutionStatus['status'] {
    const statusMap: Record<string, WorkflowExecutionStatus['status']> = {
      'RUNNING': 'RUNNING',
      'COMPLETED': 'COMPLETED',
      'FAILED': 'FAILED',
      'CANCELED': 'CANCELED',
      'TERMINATED': 'TERMINATED',
      'TIMED_OUT': 'TIMED_OUT',
      'CONTINUED_AS_NEW': 'CONTINUED_AS_NEW'
    };
    
    return statusMap[status] || 'FAILED';
  }
  
  private convertRetryPolicy(policy: RetryPolicy): any {
    return {
      maximumAttempts: policy.maximumAttempts,
      initialInterval: `${policy.initialInterval}ms`,
      backoffCoefficient: policy.backoffCoefficient,
      maximumInterval: policy.maximumInterval ? `${policy.maximumInterval}ms` : undefined
    };
  }
  
  private convertSearchAttributes(searchAttributes?: Record<string, string[]>): any {
    if (!searchAttributes) return undefined;
    
    const result: Record<string, any> = {};
    
    for (const [key, value] of Object.entries(searchAttributes)) {
      result[key] = value;
    }
    
    return result;
  }
}
```

### Create a Worker Setup

Create a worker setup in `src/workflow-engine/temporal-worker.ts`:

```typescript
// src/workflow-engine/temporal-worker.ts
import { Worker, NativeConnection } from '@temporalio/worker';
import { WorkflowDefinition } from './interface';

export interface TemporalWorkerOptions {
  address: string;
  namespace: string;
  taskQueue: string;
  workflowsPath: string;
  activitiesPath: string;
}

export class TemporalWorkerManager {
  private options: TemporalWorkerOptions;
  private worker: Worker | null = null;
  
  constructor(options: TemporalWorkerOptions) {
    this.options = options;
  }
  
  async start(): Promise<void> {
    const connection = await NativeConnection.connect({
      address: this.options.address,
    });
    
    this.worker = await Worker.create({
      connection,
      namespace: this.options.namespace,
      taskQueue: this.options.taskQueue,
      workflowsPath: this.options.workflowsPath,
      activities: require(this.options.activitiesPath),
    });
    
    await this.worker.run();
    console.log(`Worker started for task queue: ${this.options.taskQueue}`);
  }
  
  async stop(): Promise<void> {
    if (this.worker) {
      await this.worker.shutdown();
      this.worker = null;
      console.log('Worker stopped');
    }
  }
}
```

### Create a Sample Workflow and Activities

Create a sample workflow in `src/workflows/sample-workflow.ts`:

```typescript
// src/workflows/sample-workflow.ts
import { proxyActivities } from '@temporalio/workflow';
import type { Activities } from '../activities/sample-activities';

const activities = proxyActivities<Activities>({
  startToCloseTimeout: '10 minutes',
});

export interface SampleWorkflowInput {
  name: string;
  data: Record<string, any>;
}

export interface SampleWorkflowResult {
  processedId: string;
  status: string;
  timestamp: string;
}

export async function sampleWorkflow(input: SampleWorkflowInput): Promise<SampleWorkflowResult> {
  // Step 1: Validate input
  const validationResult = await activities.validateInput(input);
  
  if (!validationResult.valid) {
    throw new Error(`Invalid input: ${validationResult.errors.join(', ')}`);
  }
  
  // Step 2: Process data
  const processResult = await activities.processData(input.data);
  
  // Step 3: Store result
  const storageResult = await activities.storeResult(processResult);
  
  // Return the final result
  return {
    processedId: storageResult.id,
    status: 'completed',
    timestamp: new Date().toISOString()
  };
}
```

Create sample activities in `src/activities/sample-activities.ts`:

```typescript
// src/activities/sample-activities.ts
import { SampleWorkflowInput } from '../workflows/sample-workflow';

export interface ValidationResult {
  valid: boolean;
  errors: string[];
}

export interface ProcessResult {
  id: string;
  result: any;
  metadata: {
    processingTime: number;
    timestamp: string;
  };
}

export interface StorageResult {
  id: string;
  location: string;
}

export interface Activities {
  validateInput(input: SampleWorkflowInput): Promise<ValidationResult>;
  processData(data: Record<string, any>): Promise<ProcessResult>;
  storeResult(result: ProcessResult): Promise<StorageResult>;
}

export async function validateInput(input: SampleWorkflowInput): Promise<ValidationResult> {
  const errors: string[] = [];
  
  if (!input.name) {
    errors.push('Name is required');
  }
  
  if (!input.data || Object.keys(input.data).length === 0) {
    errors.push('Data is required');
  }
  
  return {
    valid: errors.length === 0,
    errors
  };
}

export async function processData(data: Record<string, any>): Promise<ProcessResult> {
  // Simulate processing time
  const startTime = Date.now();
  await new Promise(resolve => setTimeout(resolve, 1000));
  const endTime = Date.now();
  
  return {
    id: `process-${Date.now()}`,
    result: {
      ...data,
      processed: true
    },
    metadata: {
      processingTime: endTime - startTime,
      timestamp: new Date().toISOString()
    }
  };
}

export async function storeResult(result: ProcessResult): Promise<StorageResult> {
  // Simulate storage operation
  await new Promise(resolve => setTimeout(resolve, 500));
  
  return {
    id: result.id,
    location: `storage://results/${result.id}`
  };
}
```

### Create a Main Application Entry Point

Create a main application entry point in `src/index.ts`:

```typescript
// src/index.ts
import { TemporalWorkflowEngine } from './workflow-engine/temporal-engine';
import { TemporalWorkerManager } from './workflow-engine/temporal-worker';
import { WorkflowDefinition } from './workflow-engine/interface';
import path from 'path';

async function main() {
  // Initialize the workflow engine
  const workflowEngine = new TemporalWorkflowEngine({
    address: process.env.TEMPORAL_ADDRESS || 'localhost:7233',
    namespace: process.env.TEMPORAL_NAMESPACE || 'coafi-dev',
    taskQueue: process.env.TEMPORAL_TASK_QUEUE || 'coafi-task-queue'
  });
  
  // Register a sample workflow
  const sampleWorkflow: WorkflowDefinition = {
    id: 'sample-workflow-v1',
    name: 'sampleWorkflow',
    version: '1.0.0',
    steps: [
      {
        id: 'validate',
        name: 'Validate Input',
        type: 'task',
        action: 'validateInput',
        parameters: {},
        dependencies: []
      },
      {
        id: 'process',
        name: 'Process Data',
        type: 'task',
        action: 'processData',
        parameters: {},
        dependencies: ['validate']
      },
      {
        id: 'store',
        name: 'Store Result',
        type: 'task',
        action: 'storeResult',
        parameters: {},
        dependencies: ['process']
      }
    ],
    triggers: [
      {
        type: 'api',
        condition: {
          endpoint: '/api/sample-workflow',
          method: 'POST'
        }
      }
    ],
    policies: ['default-retry-policy']
  };
  
  await workflowEngine.registerWorkflow(sampleWorkflow);
  
  // Start a worker
  const workerManager = new TemporalWorkerManager({
    address: process.env.TEMPORAL_ADDRESS || 'localhost:7233',
    namespace: process.env.TEMPORAL_NAMESPACE || 'coafi-dev',
    taskQueue: process.env.TEMPORAL_TASK_QUEUE || 'coafi-task-queue',
    workflowsPath: path.resolve(__dirname, './workflows'),
    activitiesPath: path.resolve(__dirname, './activities/sample-activities')
  });
  
  await workerManager.start();
  
  // Example of starting a workflow
  const executionId = await workflowEngine.startWorkflow(
    'sample-workflow-v1',
    {
      name: 'Test Workflow',
      data: {
        key1: 'value1',
        key2: 'value2'
      }
    }
  );
  
  console.log(`Started workflow with execution ID: ${executionId}`);
  
  // Wait for workflow to complete
  setTimeout(async () => {
    const status = await workflowEngine.getWorkflowStatus(executionId);
    console.log('Workflow status:', status);
    
    // Shutdown worker
    await workerManager.stop();
    
    process.exit(0);
  }, 15000);
}

main().catch(error => {
  console.error('Error in main:', error);
  process.exit(1);
});
```

## 3. Creating Initial Database Schema for State Management

Now, let's create the database schema for state management. We'll use PostgreSQL for this purpose.

### Create Database Migration Scripts

Create a `migrations` directory:

```shellscript
mkdir -p migrations
```

Create the initial migration script in `migrations/001_initial_schema.sql`:

```sql
-- migrations/001_initial_schema.sql

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Workflow definitions table
CREATE TABLE workflow_definitions (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    version VARCHAR(50) NOT NULL,
    definition JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    UNIQUE (name, version)
);

-- Workflow executions table
CREATE TABLE workflow_executions (
    execution_id VARCHAR(255) PRIMARY KEY,
    workflow_id VARCHAR(255) NOT NULL REFERENCES workflow_definitions(id),
    status VARCHAR(50) NOT NULL,
    input JSONB,
    output JSONB,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE,
    error TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create index on workflow executions
CREATE INDEX idx_workflow_executions_workflow_id ON workflow_executions(workflow_id);
CREATE INDEX idx_workflow_executions_status ON workflow_executions(status);
CREATE INDEX idx_workflow_executions_start_time ON workflow_executions(start_time);

-- Workflow steps table
CREATE TABLE workflow_steps (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id VARCHAR(255) NOT NULL REFERENCES workflow_executions(execution_id) ON DELETE CASCADE,
    step_id VARCHAR(255) NOT NULL,
    step_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    result JSONB,
    error TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    UNIQUE (execution_id, step_id)
);

-- Create index on workflow steps
CREATE INDEX idx_workflow_steps_execution_id ON workflow_steps(execution_id);
CREATE INDEX idx_workflow_steps_status ON workflow_steps(status);

-- Workflow variables table
CREATE TABLE workflow_variables (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id VARCHAR(255) NOT NULL REFERENCES workflow_executions(execution_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    value JSONB,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    UNIQUE (execution_id, name)
);

-- Create index on workflow variables
CREATE INDEX idx_workflow_variables_execution_id ON workflow_variables(execution_id);

-- Workflow checkpoints table
CREATE TABLE workflow_checkpoints (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id VARCHAR(255) NOT NULL REFERENCES workflow_executions(execution_id) ON DELETE CASCADE,
    checkpoint_data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create index on workflow checkpoints
CREATE INDEX idx_workflow_checkpoints_execution_id ON workflow_checkpoints(execution_id);

-- Workflow events table
CREATE TABLE workflow_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id VARCHAR(255) NOT NULL REFERENCES workflow_executions(execution_id) ON DELETE CASCADE,
    event_type VARCHAR(255) NOT NULL,
    event_data JSONB NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create index on workflow events
CREATE INDEX idx_workflow_events_execution_id ON workflow_events(execution_id);
CREATE INDEX idx_workflow_events_event_type ON workflow_events(event_type);
CREATE INDEX idx_workflow_events_timestamp ON workflow_events(timestamp);
```

### Implement the State Manager

Create the state manager interface in `src/state/manager.ts`:

```typescript
// src/state/manager.ts
export interface WorkflowState {
  executionId: string;
  workflowId: string;
  workflowVersion: string;
  status: WorkflowStatus;
  input: Record<string, any>;
  output?: Record<string, any>;
  currentSteps: StepState[];
  variables: Record<string, any>;
  startTime: string;
  updateTime: string;
  endTime?: string;
  error?: string;
  metadata: Record<string, any>;
}

export interface StepState {
  id: string;
  name: string;
  status: StepStatus;
  startTime?: string;
  endTime?: string;
  result?: any;
  error?: string;
}

export type WorkflowStatus = 
  | 'CREATED'
  | 'RUNNING'
  | 'COMPLETED'
  | 'FAILED'
  | 'CANCELED'
  | 'TERMINATED'
  | 'TIMED_OUT';

export type StepStatus = 
  | 'PENDING'
  | 'RUNNING'
  | 'COMPLETED'
  | 'FAILED'
  | 'SKIPPED'
  | 'CANCELED';

export interface WorkflowExecutionSummary {
  executionId: string;
  workflowId: string;
  status: WorkflowStatus;
  startTime: string;
  endTime?: string;
}

export interface WorkflowEvent {
  id: string;
  executionId: string;
  eventType: string;
  eventData: Record<string, any>;
  timestamp: string;
}

export interface StateQuery {
  workflowId?: string;
  status?: WorkflowStatus | WorkflowStatus[];
  startTimeFrom?: string;
  startTimeTo?: string;
  endTimeFrom?: string;
  endTimeTo?: string;
  limit?: number;
  offset?: number;
}

export interface StateManager {
  // State operations
  saveState(executionId: string, state: WorkflowState): Promise<void>;
  getState(executionId: string): Promise<WorkflowState | null>;
  updateState(executionId: string, updates: Partial<WorkflowState>): Promise<WorkflowState>;
  deleteState(executionId: string): Promise<void>;
  
  // Checkpointing
  createCheckpoint(executionId: string): Promise<string>;
  restoreFromCheckpoint(checkpointId: string): Promise<WorkflowState>;
  
  // Queries
  findExecutions(query: StateQuery): Promise<WorkflowExecutionSummary[]>;
  getExecutionHistory(executionId: string): Promise<WorkflowEvent[]>;
  
  // Events
  recordEvent(executionId: string, eventType: string, eventData: Record<string, any>): Promise<void>;
}
```

Implement the PostgreSQL state manager in `src/state/postgres-state-manager.ts`:

```typescript
// src/state/postgres-state-manager.ts
import { Pool, PoolClient } from 'pg';
import { 
  StateManager, 
  WorkflowState, 
  StateQuery, 
  WorkflowExecutionSummary,
  WorkflowEvent,
  StepState
} from './manager';
import { v4 as uuidv4 } from 'uuid';

export interface PostgresStateManagerOptions {
  connectionString: string;
  poolSize?: number;
}

export class PostgresStateManager implements StateManager {
  private pool: Pool;
  
  constructor(options: PostgresStateManagerOptions) {
    this.pool = new Pool({
      connectionString: options.connectionString,
      max: options.poolSize || 10
    });
  }
  
  async saveState(executionId: string, state: WorkflowState): Promise<void> {
    const client = await this.pool.connect();
    
    try {
      await client.query('BEGIN');
      
      // Insert or update workflow execution
      await client.query(
        `INSERT INTO workflow_executions 
         (execution_id, workflow_id, status, input, output, start_time, end_time, error)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
         ON CONFLICT (execution_id) DO UPDATE
         SET status = $3, output = $5, end_time = $7, error = $8, updated_at = NOW()`,
        [
          executionId,
          state.workflowId,
          state.status,
          JSON.stringify(state.input),
          state.output ? JSON.stringify(state.output) : null,
          state.startTime,
          state.endTime || null,
          state.error || null
        ]
      );
      
      // Save current steps
      await this.saveSteps(client, executionId, state.currentSteps);
      
      // Save variables
      await this.saveVariables(client, executionId, state.variables);
      
      await client.query('COMMIT');
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }
  
  async getState(executionId: string): Promise<WorkflowState | null> {
    const client = await this.pool.connect();
    
    try {
      // Get workflow execution
      const executionResult = await client.query(
        `SELECT 
           e.execution_id, e.workflow_id, d.version as workflow_version, 
           e.status, e.input, e.output, e.start_time, e.end_time, e.error
         FROM workflow_executions e
         JOIN workflow_definitions d ON e.workflow_id = d.id
         WHERE e.execution_id = $1`,
        [executionId]
      );
      
      if (executionResult.rows.length === 0) {
        return null;
      }
      
      const execution = executionResult.rows[0];
      
      // Get steps
      const steps = await this.getSteps(client, executionId);
      
      // Get variables
      const variables = await this.getVariables(client, executionId);
      
      return {
        executionId: execution.execution_id,
        workflowId: execution.workflow_id,
        workflowVersion: execution.workflow_version,
        status: execution.status,
        input: execution.input,
        output: execution.output,
        currentSteps: steps,
        variables,
        startTime: execution.start_time,
        updateTime: execution.updated_at,
        endTime: execution.end_time,
        error: execution.error,
        metadata: {} // Metadata not stored in this implementation
      };
    } finally {
      client.release();
    }
  }
  
  async updateState(executionId: string, updates: Partial<WorkflowState>): Promise<WorkflowState> {
    const currentState = await this.getState(executionId);
    
    if (!currentState) {
      throw new Error(`Workflow execution ${executionId} not found`);
    }
    
    const updatedState: WorkflowState = {
      ...currentState,
      ...updates,
      updateTime: new Date().toISOString()
    };
    
    await this.saveState(executionId, updatedState);
    
    return updatedState;
  }
  
  async deleteState(executionId: string): Promise<void> {
    await this.pool.query(
      'DELETE FROM workflow_executions WHERE execution_id = $1',
      [executionId]
    );
  }
  
  async createCheckpoint(executionId: string): Promise<string> {
    const state = await this.getState(executionId);
    
    if (!state) {
      throw new Error(`Workflow execution ${executionId} not found`);
    }
    
    const checkpointId = uuidv4();
    
    await this.pool.query(
      `INSERT INTO workflow_checkpoints 
       (id, execution_id, checkpoint_data)
       VALUES ($1, $2, $3)`,
      [checkpointId, executionId, JSON.stringify(state)]
    );
    
    return checkpointId;
  }
  
  async restoreFromCheckpoint(checkpointId: string): Promise<WorkflowState> {
    const result = await this.pool.query(
      `SELECT checkpoint_data FROM workflow_checkpoints WHERE id = $1`,
      [checkpointId]
    );
    
    if (result.rows.length === 0) {
      throw new Error(`Checkpoint ${checkpointId} not found`);
    }
    
    return result.rows[0].checkpoint_data;
  }
  
  async findExecutions(query: StateQuery): Promise<WorkflowExecutionSummary[]> {
    let sql = `
      SELECT 
        e.execution_id, e.workflow_id, e.status, e.start_time, e.end_time
      FROM workflow_executions e
      WHERE 1=1
    `;
    
    const params: any[] = [];
    let paramIndex = 1;
    
    if (query.workflowId) {
      sql += ` AND e.workflow_id = $${paramIndex++}`;
      params.push(query.workflowId);
    }
    
    if (query.status) {
      if (Array.isArray(query.status)) {
        sql += ` AND e.status IN (${query.status.map((_, i) => `$${paramIndex + i}`).join(', ')})`;
        params.push(...query.status);
        paramIndex += query.status.length;
      } else {
        sql += ` AND e.status = $${paramIndex++}`;
        params.push(query.status);
      }
    }
    
    if (query.startTimeFrom) {
      sql += ` AND e.start_time >= $${paramIndex++}`;
      params.push(query.startTimeFrom);
    }
    
    if (query.startTimeTo) {
      sql += ` AND e.start_time <= $${paramIndex++}`;
      params.push(query.startTimeTo);
    }
    
    if (query.endTimeFrom) {
      sql += ` AND e.end_time >= $${paramIndex++}`;
      params.push(query.endTimeFrom);
    }
    
    if (query.endTimeTo) {
      sql += ` AND e.end_time <= $${paramIndex++}`;
      params.push(query.endTimeTo);
    }
    
    sql += ` ORDER BY e.start_time DESC`;
    
    if (query.limit) {
      sql += ` LIMIT $${paramIndex++}`;
      params.push(query.limit);
    }
    
    if (query.offset) {
      sql += ` OFFSET $${paramIndex++}`;
      params.push(query.offset);
    }
    
    const result = await this.pool.query(sql, params);
    
    return result.rows.map(row => ({
      executionId: row.execution_id,
      workflowId: row.workflow_id,
      status: row.status,
      startTime: row.start_time,
      endTime: row.end_time
    }));
  }
  
  async getExecutionHistory(executionId: string): Promise<WorkflowEvent[]> {
    const result = await this.pool.query(
      `SELECT id, execution_id, event_type, event_data, timestamp
       FROM workflow_events
       WHERE execution_id = $1
       ORDER BY timestamp ASC`,
      [executionId]
    );
    
    return result.rows.map(row => ({
      id: row.id,
      executionId: row.execution_id,
      eventType: row.event_type,
      eventData: row.event_data,
      timestamp: row.timestamp
    }));
  }
  
  async recordEvent(executionId: string, eventType: string, eventData: Record<string, any>): Promise<void> {
    await this.pool.query(
      `INSERT INTO workflow_events
       (execution_id, event_type, event_data)
       VALUES ($1, $2, $3)`,
      [executionId, eventType, JSON.stringify(eventData)]
    );
  }
  
  // Helper methods
  private async saveSteps(client: PoolClient, executionId: string, steps: StepState[]): Promise<void> {
    // Delete existing steps
    await client.query(
      `DELETE FROM workflow_steps WHERE execution_id = $1`,
      [executionId]
    );
    
    // Insert new steps
    for (const step of steps) {
      await client.query(
        `INSERT INTO workflow_steps
         (execution_id, step_id, step_name, status, start_time, end_time, result, error)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8)`,
        [
          executionId,
          step.id,
          step.name,
          step.status,
          step.startTime || null,
          step.endTime || null,
          step.result ? JSON.stringify(step.result) : null,
          step.error || null
        ]
      );
    }
  }
  
  private async getSteps(client: PoolClient, executionId: string): Promise<StepState[]> {
    const result = await client.query(
      `SELECT step_id, step_name, status, start_time, end_time, result, error
       FROM workflow_steps
       WHERE execution_id = $1
       ORDER BY created_at ASC`,
      [executionId]
    );
    
    return result.rows.map(row => ({
      id: row.step_id,
      name: row.step_name,
      status: row.status,
      startTime: row.start_time,
      endTime: row.end_time,
      result: row.result,
      error: row.error
    }));
  }
  
  private async saveVariables(client: PoolClient, executionId: string, variables: Record<string, any>): Promise<void> {
    // Delete existing variables
    await client.query(
      `DELETE FROM workflow_variables WHERE execution_id = $1`,
      [executionId]
    );
    
    // Insert new variables
    for (const [name, value] of Object.entries(variables)) {
      await client.query(
        `INSERT INTO workflow_variables
         (execution_id, name, value)
         VALUES ($1, $2, $3)`,
        [
          executionId,
          name,
          JSON.stringify(value)
        ]
      );
    }
  }
  
  private async getVariables(client: PoolClient, executionId: string): Promise<Record<string, any>> {
    const result = await client.query(
      `SELECT name, value
       FROM workflow_variables
       WHERE execution_id = $1`,
      [executionId]
    );
    
    const variables: Record<string, any> = {};
    
    for (const row of result.rows) {
      variables[row.name] = row.value;
    }
    
    return variables;
  }
}
```

### Create a Database Migration Script

Create a script to run the database migrations in `src/utils/run-migrations.ts`:

```typescript
// src/utils/run-migrations.ts
import { Pool } from 'pg';
import fs from 'fs';
import path from 'path';

interface MigrationOptions {
  connectionString: string;
  migrationsDir: string;
}

async function runMigrations(options: MigrationOptions): Promise<void> {
  const pool = new Pool({
    connectionString: options.connectionString
  });
  
  try {
    // Create migrations table if it doesn't exist
    await pool.query(`
      CREATE TABLE IF NOT EXISTS migrations (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        applied_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
      )
    `);
    
    // Get applied migrations
    const appliedMigrationsResult = await pool.query(
      'SELECT name FROM migrations ORDER BY id'
    );
    
    const appliedMigrations = new Set(
      appliedMigrationsResult.rows.map(row => row.name)
    );
    
    // Get all migration files
    const migrationFiles = fs.readdirSync(options.migrationsDir)
      .filter(file => file.endsWith('.sql'))
      .sort();
    
    // Apply new migrations
    for (const file of migrationFiles) {
      if (!appliedMigrations.has(file)) {
        console.log(`Applying migration: ${file}`);
        
        const filePath = path.join(options.migrationsDir, file);
        const sql = fs.readFileSync(filePath, 'utf8');
        
        const client = await pool.connect();
        
        try {
          await client.query('BEGIN');
          
          // Apply migration
          await client.query(sql);
          
          // Record migration
          await client.query(
            'INSERT INTO migrations (name) VALUES ($1)',
            [file]
          );
          
          await client.query('COMMIT');
          
          console.log(`Migration applied: ${file}`);
        } catch (error) {
          await client.query('ROLLBACK');
          console.error(`Error applying migration ${file}:`, error);
          throw error;
        } finally {
          client.release();
        }
      }
    }
    
    console.log('All migrations applied successfully');
  } finally {
    await pool.end();
  }
}

// Run migrations if this script is executed directly
if (require.main === module) {
  const connectionString = process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/coafi';
  const migrationsDir = path.resolve(__dirname, '../../migrations');
  
  runMigrations({ connectionString, migrationsDir })
    .then(() => {
      console.log('Migrations completed');
      process.exit(0);
    })
    .catch(error => {
      console.error('Migration failed:', error);
      process.exit(1);
    });
}

export { runMigrations };
```

### Update package.json Scripts

Update the `package.json` file to include scripts for running migrations and starting the application:

```json
{
  "name": "coafi-orchestration-core",
  "version": "0.1.0",
  "description": "COAFI Orchestration Core",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node -r tsconfig-paths/register src/index.ts",
    "migrate": "ts-node -r tsconfig-paths/register src/utils/run-migrations.ts",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "coafi",
    "orchestration",
    "workflow"
  ],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@temporalio/client": "^1.8.0",
    "@temporalio/worker": "^1.8.0",
    "@temporalio/workflow": "^1.8.0",
    "@temporalio/common": "^1.8.0",
    "pg": "^8.11.0",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "@types/node": "^18.16.0",
    "@types/pg": "^8.10.2",
    "@types/uuid": "^9.0.1",
    "ts-node": "^10.9.1",
    "tsconfig-paths": "^4.2.0",
    "typescript": "^5.0.4"
  }
}
```

## Conclusion

You now have the foundation for the COAFI Orchestration Core with:

1. **Temporal Server Infrastructure**: Both development (Docker Compose) and production (Kubernetes) setups for the Temporal workflow engine.
2. **WorkflowEngineInterface Adapter**: A TypeScript implementation of the WorkflowEngineInterface that adapts Temporal's API to your abstraction layer.
3. **State Management Database Schema**: A PostgreSQL schema for storing workflow state, steps, variables, and events, along with a StateManager implementation.


### Next Steps

1. **Implement Workflow Definitions**: Create more complex workflow definitions for your specific use cases.
2. **Develop Activity Implementations**: Implement the activities needed for your workflows, connecting to other COAFI components.
3. **Add Error Handling**: Enhance the error handling and retry logic in the workflow engine adapter.
4. **Implement Monitoring**: Add telemetry and monitoring to track workflow execution and performance.
5. **Create API Layer**: Develop an API layer for triggering workflows and querying their status.


This implementation provides a solid foundation for the COAFI Orchestration Core, with a clean separation of concerns between the workflow engine, state management, and business logic.
