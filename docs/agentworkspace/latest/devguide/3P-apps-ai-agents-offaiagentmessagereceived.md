---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-offaiagentmessagereceived.html
---

# Unsubscribe from AI Agent message events

Removes a previously registered `onAIAgentMessageReceived` handler subscription.

 **Signature**

```typescript
offAIAgentMessageReceived(handler: AIAgentMessageHandler, contactId?: string): void
```

 **Usage**

```typescript
aiAgentsClient.offAIAgentMessageReceived(handler, contactId);
```

 **Permissions required:**

```typescript
*
```
