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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
