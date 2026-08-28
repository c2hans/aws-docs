---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-onaiagentmessagestatuschanged.html
---

# Subscribe to AI Agent message status changes in Connect Customer agent workspace
<a name="3P-apps-ai-agents-onaiagentmessagestatuschanged"></a>

Subscribes to status lifecycle transitions for AI Agent messages. Use this to track whether messages have been received, succeeded, were blocked by guardrails, or failed.

 **Signature**

```
onAIAgentMessageStatusChanged(handler: AIAgentMessageStatusHandler, contactId?: string): void
```

 **Usage**

```
const handler: AIAgentMessageStatusHandler = (data: AIAgentMessageStatusEvent) => {
    console.log("Input ID:", data.inputId);
    console.log("Status:", data.status);
};

aiAgentsClient.onAIAgentMessageStatusChanged(handler, contactId);

// AIAgentMessageStatusEvent Structure
{
  inputId: string;
  status: "IN_FLIGHT" | "RECEIVED" | "SUCCESS" | "BLOCKED" | "FAILED";
  contactId?: string;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
