---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-offaiagentcontactready.html
---

# Unsubscribe from AI Agent contact ready event
<a name="3P-apps-ai-agents-offaiagentcontactready"></a>

Removes a previously registered `onAIAgentContactReady` handler subscription.

 **Signature**

```
offAIAgentContactReady(handler: AIAgentContactReadyHandler, contactId: string): void
```

 **Usage**

```
aiAgentsClient.offAIAgentContactReady(handler, contactId);
```

 **Permissions required:**

```
*
```
