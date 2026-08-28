---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-onaiagentcontactready.html
---

# Subscribe to AI Agent contact ready event in Connect Customer agent workspace
<a name="3P-apps-ai-agents-onaiagentcontactready"></a>

Subscribes a handler that fires when the session and agentic state have been resolved for a contact. Use this event to know when AI Agents features are available for a specific contact.

 **Signature**

```
onAIAgentContactReady(handler: AIAgentContactReadyHandler, contactId: string): void
```

 **Usage**

```
const handler: AIAgentContactReadyHandler = (data: AIAgentContactReadyEvent) => {
    console.log("AI Agent ready for contact:", data.contactId);
    console.log("Agentic enabled:", data.isAgenticEnabled);
};

aiAgentsClient.onAIAgentContactReady(handler, contactId);

// AIAgentContactReadyEvent Structure
{
  contactId: string;
  isAgenticEnabled: boolean;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
