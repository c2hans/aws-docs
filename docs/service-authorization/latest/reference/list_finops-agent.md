---
source_url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_finops-agent.html
---

# Actions, resources, and condition keys for AWS FinOps Agent

AWS FinOps Agent (service prefix: `finops-agent`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/finops-agent/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/finops-agent/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/finops-agent/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/finops-agent/finops-agent.json) for this service.

**Topics**
+ [Actions defined by AWS FinOps Agent](#list_finops-agent-actions-as-permissions)
+ [Permission-only actions for AWS FinOps Agent](#list_finops-agent-permission-only-actions)
+ [Resource types defined by AWS FinOps Agent](#list_finops-agent-resources-for-iam-policies)
+ [Condition keys for AWS FinOps Agent](#list_finops-agent-policy-keys)

## Actions defined by AWS FinOps Agent
<a name="list_finops-agent-actions-as-permissions"></a>

AWS FinOps Agent has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS FinOps Agent
<a name="list_finops-agent-permission-only-actions"></a>

The following actions are defined by AWS FinOps Agent but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.

- **   [AcceptAgentRequest](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to accept a pending approval request from the agent
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CancelTask](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to cancel a task
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CancelTurn](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to cancel an in-progress conversation turn
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateAgentSpace](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a new FinOps Agent workspace
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateAutomation](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a reusable automation
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a connection
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace) / **Condition keys:**
  - **Resource types (\*required):** [integration\*](#list_finops-agent-resource-integration) / **Condition keys:**
  - **Access level:** Write

- **   [CreateConversation](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a new conversation with the FinOps Agent
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateDocument](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a document
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a third-party integration
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateOneTimeLoginSession](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a one-time login session for the FinOps Agent web application
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateTask](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a task
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [CreateTurn](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to create a new turn in a conversation
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteAgentSpace](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete a FinOps Agent workspace
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteArtifact](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete an artifact and its content
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteAutomation](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete an automation
  - **Resource types (\*required):** [automation\*](#list_finops-agent-resource-automation)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connection\*](#list_finops-agent-resource-connection)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteDocument](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete a document
  - **Resource types (\*required):** [document\*](#list_finops-agent-resource-document)
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to delete a third-party integration
  - **Resource types (\*required):** [integration\*](#list_finops-agent-resource-integration)
  - **Condition keys:**
  - **Access level:** Write

- **   [GetAgentRequest](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a pending approval request from the agent
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetAgentSpace](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a FinOps Agent workspace
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetArtifactContent](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to download artifact content
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetArtifactMetadata](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view artifact metadata
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetAutomation](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of an automation
  - **Resource types (\*required):** [automation\*](#list_finops-agent-resource-automation)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a connection
  - **Resource types (\*required):** [connection\*](#list_finops-agent-resource-connection)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetDocumentContent](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to download document content
  - **Resource types (\*required):** [document\*](#list_finops-agent-resource-document)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetDocumentMetadata](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view document metadata
  - **Resource types (\*required):** [document\*](#list_finops-agent-resource-document)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a third-party integration
  - **Resource types (\*required):** [integration\*](#list_finops-agent-resource-integration)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetOrganizationAccess](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view the organization-wide access setting for FinOps Agent
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [GetTask](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a task
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [GetTurn](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to view details of a conversation turn
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Read

- **   [ListAgentSpaces](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list all FinOps Agent workspaces in the account
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListArtifacts](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list artifacts
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListAutomations](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list automations
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListConnections](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list connections
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListConversations](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list conversations
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListDocuments](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list documents
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list third-party integrations
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListRecords](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list records for real-time agent activity display
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListTasks](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list tasks
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [ListTurns](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to list turns in a conversation
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** List

- **   [RejectAgentRequest](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to reject a pending approval request from the agent
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [RestoreDocument](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to restore an archived document
  - **Resource types (\*required):** [document\*](#list_finops-agent-resource-document)
  - **Condition keys:**
  - **Access level:** Write

- **   [SendFeedback](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to submit feedback on agent responses
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [UpdateAgentSpace](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to update a FinOps Agent workspace configuration
  - **Resource types (\*required):** [agentspace\*](#list_finops-agent-resource-agentspace)
  - **Condition keys:**
  - **Access level:** Write

- **   [UpdateAutomation](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to update an automation
  - **Resource types (\*required):** [automation\*](#list_finops-agent-resource-automation)
  - **Condition keys:**
  - **Access level:** Write

- **   [UpdateConnection](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to update a connection
  - **Resource types (\*required):** [connection\*](#list_finops-agent-resource-connection)
  - **Condition keys:**
  - **Access level:** Write

- **   [UpdateDocument](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to update a document's content and metadata
  - **Resource types (\*required):** [document\*](#list_finops-agent-resource-document)
  - **Condition keys:**
  - **Access level:** Write

- **   [UpdateOrganizationAccess](https://docs.aws.amazon.com/finops-agent/)  **
  - **Description:** Grants permission to enable or disable organization-wide access for FinOps Agent
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

## Resource types defined by AWS FinOps Agent
<a name="list_finops-agent-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.

| Resource types | ARN | Condition keys |
| --- | --- | --- |
|  [agentspace](https://docs.aws.amazon.com/finops-agent/)  | arn:${Partition}:finops-agent:${Region}:${Account}:agentspace/${AgentSpaceId} |   |
|  [automation](https://docs.aws.amazon.com/finops-agent/)  | arn:${Partition}:finops-agent:${Region}:${Account}:agentspace/${AgentSpaceId}/automation/${AutomationId} |   |
|  [connection](https://docs.aws.amazon.com/finops-agent/)  | arn:${Partition}:finops-agent:${Region}:${Account}:agentspace/${AgentSpaceId}/connection/${ConnectionId} |   |
|  [document](https://docs.aws.amazon.com/finops-agent/)  | arn:${Partition}:finops-agent:${Region}:${Account}:agentspace/${AgentSpaceId}/document/${DocumentId} |   |
|  [integration](https://docs.aws.amazon.com/finops-agent/)  | arn:${Partition}:finops-agent:${Region}:${Account}:integration/${IntegrationId} |   |

## Condition keys for AWS FinOps Agent
<a name="list_finops-agent-policy-keys"></a>

AWS FinOps Agent has no service-specific condition keys that can be used in the `Condition` element of policy statements.
