---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-offaiagentmessagereceived.html
---

# Unsubscribe from AI Agent message events
<a name="3P-apps-ai-agents-offaiagentmessagereceived"></a>

Removes a previously registered `onAIAgentMessageReceived` handler subscription.

 **Signature**

```
offAIAgentMessageReceived(handler: AIAgentMessageHandler, contactId?: string): void
```

 **Usage**

```
aiAgentsClient.offAIAgentMessageReceived(handler, contactId);
```

 **Permissions required:**

```
*
```
