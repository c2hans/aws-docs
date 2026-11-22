---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-offaiagentcontactready.html
---

# Unsubscribe from AI Agent contact ready event

Removes a previously registered `onAIAgentContactReady` handler subscription.

 **Signature**

```typescript
offAIAgentContactReady(handler: AIAgentContactReadyHandler, contactId: string): void
```

 **Usage**

```typescript
aiAgentsClient.offAIAgentContactReady(handler, contactId);
```

 **Permissions required:**

```typescript
*
```
