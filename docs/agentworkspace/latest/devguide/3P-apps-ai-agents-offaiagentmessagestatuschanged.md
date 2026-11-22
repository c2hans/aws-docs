---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-offaiagentmessagestatuschanged.html
---

# Unsubscribe from AI Agent message status changes

Removes a previously registered `onAIAgentMessageStatusChanged` handler subscription.

 **Signature**

```typescript
offAIAgentMessageStatusChanged(handler: AIAgentMessageStatusHandler, contactId?: string): void
```

 **Usage**

```typescript
aiAgentsClient.offAIAgentMessageStatusChanged(handler, contactId);
```

 **Permissions required:**

```typescript
*
```
