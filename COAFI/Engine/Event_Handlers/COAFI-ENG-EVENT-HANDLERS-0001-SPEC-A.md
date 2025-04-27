---
title: "COAFI – Event Handlers System Specification"
document_id: COAFI-ENG-EVENT-HANDLERS-0001-SPEC-A
version: v0.9.2-PRELIMINARY # Incremented version
status: DRAFT
author: GAIA Platforms Initiative
date: 2025-04-27
tags:
  - COAFI
  - Event Handlers
  - Federation
  - BITT
  - Ethics
  - Git
infoCode: INFO-SPEC
utids: TBD
---

# COAFI – Event Handlers System Specification

This document specifies the modules and logic responsible for handling specific events that trigger actions within the COAFI orchestration engine. These handlers act as the reactive component of COAFI, allowing it to respond dynamically to changes and external stimuli within the GAIA Platforms ecosystem.

---

## Purpose & Functionality

The core purpose of the Event Handlers is to define how COAFI reacts to various triggers, initiating appropriate workflows and ensuring system coherence. They manage the detection, parsing, and routing of events to the correct processing logic.

---

## Specific Trigger Handling

This section outlines the primary event types COAFI is designed to handle and the general actions associated with each.

### Git Commits/Merges in Monitored Repositories
- **Detection**:
  COAFI monitors designated Git repositories for new commits or merges affecting tracked files (e.g., specification documents, configuration files).
- **Action**:
  Upon detection, the relevant handler (e.g., `GitCommitHandler`) parses the changes and initiates appropriate workflows, such as:
  - Validating the changed content against defined schemas (`COAFI/Schema/`).
  - Triggering automated documentation generation or updates (`COAFI/Generators/`).
  - Notifying dependent systems or updating COAFI registries (`COAFI/Registries/`).
  - Logging the change event via BITT.

#### Handler Detail: `GitCommitHandler`

* **Use case:** Commits/Merges in monitored repositories
* **Detección**
    * COAFI vigila uno o más repositorios Git configurados.
    * Detecta nuevos commits o merges que modifican archivos rastreados (p. ej., documentos de especificación, archivos de configuración).
* **Acción**
    1.  **Parsear cambios**:
        * Extraer `diff` y rutas de los archivos afectados.
        * Identificar tipo de archivo (esquema, doc, config, etc.).
    2.  **Validar contenido**:
        * Comparar cada archivo modificado contra los esquemas definidos en `COAFI/Schema/`.
        * Generar error o advertencia si no cumple el esquema. Registrar resultado.
    3.  **Generar o actualizar documentación/artefactos**:
        * Invocar el módulo generador correspondiente en `COAFI/Generators/` (si aplica según el tipo de archivo).
        * Reconstruir secciones impactadas, actualizar índices o generar artefactos derivados.
    4.  **Notificar sistemas dependientes**:
        * Disparar eventos o llamadas API/mensajes a servicios registrados como dependientes en `COAFI/Registries/`.
        * Incluir payload con metadatos relevantes (commit SHA, autor, lista de archivos modificados, resultado de validación).
    5.  **Registrar el evento en BITT**:
        * Crear un registro de auditoría inmutable en BITT con: Commit SHA, autor, fecha, repositoro, archivos modificados, resultado de validación, resultado de generación (si aplica), y el UTidS del evento.

> _Nota: Implementar cada paso de la acción como método o función modular para facilitar pruebas unitarias y extensibilidad._

##### Example Event Payload

```json
{
  "repositoryUrl": "https://github.com/gaia-platforms/coafi",
  "commitSha": "abc123def456",
  "branch": "main",
  "author": "developer@example.com",
  "filesChanged": [
    {
      "path": "COAFI/Schema/specification.yaml",
      "changeType": "modified"
    },
    {
      "path": "COAFI/Docs/overview.md",
      "changeType": "added"
    }
  ]
}
```

##### Expected Outcome

- Validation results for each file (success or detailed error).
- Documentation generation status (success or error).
- Notifications sent to dependent systems.
- Event logged in BITT with all relevant metadata.

---

### API Calls to COAFI Endpoints
- **Detection**:
  COAFI exposes APIs (`COAFI/Interfaces/API_Definitions/`) for external systems or users to interact with its functions (e.g., query registries, submit new information).
- **Action**:
  The `APIRequestHandler` validates incoming requests (authentication, payload schema) and executes the corresponding action, which might involve:
  - Querying or updating COAFI registries.
  - Initiating specific orchestration workflows (`COAFI/Workflows/`).
  - Returning data to the caller.
  - Logging the API interaction via BITT.

#### Handler Detail: `APIRequestHandler`

* **Use case:** API calls to COAFI endpoints
* **Detección**
    * COAFI expone APIs para que sistemas externos o usuarios interactúen con sus funciones.
    * Detecta solicitudes entrantes a los endpoints definidos en `COAFI/Interfaces/API_Definitions/`.
* **Acción**
    1.  **Validar solicitud**:
        * Verificar autenticación y autorización del solicitante.
        * Validar el payload de la solicitud contra el esquema definido.
    2.  **Ejecutar acción correspondiente**:
        * Consultar o actualizar registros en `COAFI/Registries/`.
        * Iniciar workflows específicos en `COAFI/Workflows/`.
        * Devolver datos al solicitante.
    3.  **Registrar interacción en BITT**:
        * Crear un registro de auditoría inmutable en BITT con: Endpoint, método, solicitante, payload, resultado de la acción, y el UTidS del evento.

> _Nota: Implementar cada paso de la acción como método o función modular para facilitar pruebas unitarias y extensibilidad._

##### Example Event Payload

```json
{
  "endpoint": "/api/registry/update",
  "method": "POST",
  "requestId": "req-789xyz",
  "authToken": "Bearer abcdef123456",
  "body": {
    "registryId": "doc-registry",
    "entryId": "entry-001",
    "data": {
      "title": "Updated Document Title",
      "content": "Updated content of the document."
    }
  }
}
```

##### Expected Outcome

- Validation results (success or detailed error).
- Registry update status (success or error).
- Workflow initiation status (if applicable).
- Event logged in BITT with all relevant metadata.

---

### Events Logged in the BITT Ledger
- **Detection**:
  COAFI can monitor the BITT ledger for specific, predefined event types logged by other GAIA components (e.g., compliance failures, critical system alerts, completion of milestones).
- **Action**:
  The `BITTEventHandler` filters and processes relevant BITT events, triggering actions like:
  - Generating notifications to relevant stakeholders.
  - Initiating automated remediation or escalation workflows.
  - Updating the status of related items within COAFI registries.

#### Handler Detail: `BITTEventHandler`

* **Use case:** Events logged in the BITT ledger
* **Detección**
    * COAFI monitorea el ledger BITT para eventos específicos predefinidos.
    * Detecta eventos registrados por otros componentes de GAIA (p. ej., fallos de cumplimiento, alertas críticas del sistema, finalización de hitos).
* **Acción**
    1.  **Filtrar y procesar eventos relevantes**:
        * Identificar eventos de interés según patrones predefinidos.
        * Extraer datos relevantes del evento.
    2.  **Generar notificaciones a stakeholders**:
        * Enviar notificaciones a las partes interesadas relevantes.
    3.  **Iniciar workflows de remediación o escalamiento**:
        * Iniciar workflows automatizados para remediación o escalamiento según el tipo de evento.
    4.  **Actualizar estado de ítems relacionados en COAFI**:
        * Actualizar el estado de ítems relacionados en los registros de COAFI.

> _Nota: Implementar cada paso de la acción como método o función modular para facilitar pruebas unitarias y extensibilidad._

##### Example Event Payload

```json
{
  "eventType": "GAIA:COMPLIANCE:FAILURE",
  "eventId": "evt-456def",
  "timestamp": "2025-04-27T14:00:00Z",
  "source": "compliance-service",
  "details": {
    "complianceCheckId": "check-123",
    "failureReason": "Data privacy violation",
    "affectedEntities": ["entity-001", "entity-002"]
  }
}
```

##### Expected Outcome

- Event filtering and processing results (success or detailed error).
- Notifications sent to relevant stakeholders.
- Remediation or escalation workflow initiation status.
- Related items' status updated in COAFI registries.
- Event logged in BITT with all relevant metadata.

---

### Messages Received via Federated Communication Channels
- **Detection**:
  COAFI listens on designated secure communication channels (potentially using protocols defined in `Domains/AERO/INTERFACE/Data-Control-Interfaces/` or `Domains/SPACE/INTERFACE/`) for messages from other federated GAIA domains or systems.
- **Action**:
  Handlers parse incoming messages, verify authenticity, and initiate workflows based on the message content and source domain. This enables cross-domain coordination and data synchronization orchestrated by COAFI.

---

### Scheduled Tasks or Time-Based Triggers
- **Detection**:
  An internal scheduler within the `COAFI/Engine/` triggers predefined tasks at specific times or intervals.
- **Action**:
  Handlers execute routine tasks such as:
  - Generating periodic compliance or status reports.
  - Performing system health checks on COAFI itself.
  - Running data aggregation or cleanup workflows.
  - Archiving old registry entries according to `COAFI/Policies/`.

---

## Detailed Considerations

### Specifications

#### Event Detection
- Define the specific event types to monitor (e.g., Git commits on `.md`, `.spec` files; API POST requests to `/registry/update`; BITT events matching pattern `GAIA:COMPLIANCE:*`; federated messages of type `SystemUpdateNotification`; daily scheduled task `GenerateReport`).
- Specify the exact sources (e.g., list of repository URLs/paths, specific API endpoint routes, BITT event topics/smart contract addresses, message queue names, cron expressions for scheduled tasks).

#### Event Routing
- Maintain a central routing map (e.g., in a configuration file like `handler_routes.yaml` or a dedicated registry) associating event types/sources with specific handler modules/classes (e.g., `GitCommitEvent -> handlers.git.GitCommitHandler`).

#### Workflow Initiation
- Define the specific workflow(s) (from `COAFI/Workflows/`) triggered by each handler upon successful event processing.
- Specify required inputs for each workflow (e.g., commit hash, changed file list, API payload, BITT event data).
- Document workflow dependencies and potential chaining (Workflow A completion triggers Event B handled by Handler C).

#### Integration Points
- Clearly document API contracts (e.g., OpenAPI specifications in `COAFI/Interfaces/API_Definitions/`).
- Define standardized message formats for federated communication channels.
- Specify authentication and authorization requirements for API endpoints and message sources.

---

### Implementation Details

#### Code Structure
- Organize handlers logically within `COAFI/Engine/Event_Handlers/` (e.g., `git_handlers.py`, `api_handlers.py`, `bitt_handlers.py`).
- Implement a central event dispatcher/listener service that monitors sources and routes events based on the defined mapping.
- Consider using an event bus or message queue internally for decoupling.

#### Handler Logic
- Define a common base class or interface for all handlers (e.g., an abstract `BaseEventHandler` with an `async handle_event(event_data)` method).
- Implement specific parsing, validation, and processing logic within each concrete handler class.
- Utilize shared utility modules for logging, configuration access, BITT interaction, etc.

#### Data Flow
- Define standardized internal event objects/data structures passed between the dispatcher and handlers.
- Implement robust parsing and validation (e.g., using Pydantic models) for incoming event payloads.

#### Dependencies
- Use dependency injection frameworks or patterns to provide handlers with access to external services (BITT client, Git API client, Workflow engine client, Database client).
- Develop mock implementations of these dependencies for effective unit and integration testing.

---

### Specific Error Handling Logic

#### Validation Errors
- Log detailed validation failures (e.g., missing fields, incorrect data types) with event context.
- For API requests, return standardized error responses (e.g., HTTP 400 Bad Request) with clear error messages.
- For other event types, potentially log to a specific error queue or notify an administrator.

#### Processing Failures
- Implement configurable retry mechanisms (e.g., using libraries like `tenacity`) with exponential backoff for transient issues (e.g., temporary network errors, database deadlocks).
- Log detailed errors including stack traces and relevant event data for debugging.
- Define a maximum retry limit, after which the event is moved to a dead-letter queue or triggers a critical failure alert.

#### Unrecognized Events
- Log unrecognized or unroutable events clearly, indicating the source and payload.
- Avoid discarding silently; move to an "unprocessed" queue or log for later analysis.

#### Critical Failures
- Define specific error conditions considered critical (e.g., inability to connect to BITT, unrecoverable database errors, consistent workflow initiation failures).
- Trigger automated escalation workflows: send alerts to monitoring systems (e.g., Prometheus Alertmanager), notify administrators via email/chatops.

#### Audit and Traceability
- Ensure every significant step (event received, validation success/failure, handler invoked, workflow initiated, processing success/failure, retries) is logged immutably to BITT, correlated with the original event and relevant UTidS identifiers.

---

