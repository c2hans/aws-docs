---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-listaiagentmessages.html
---

# List AI Agent messages for a contact
<a name="3P-apps-ai-agents-listaiagentmessages"></a>

Retrieves the AI Agent message history for a contact, ordered by sequence number.

 **Signature**

```
listAIAgentMessages(params: ListAIAgentMessagesParams): Promise<ListAIAgentMessagesResult>
```

 **Usage**

```
const result = await aiAgentsClient.listAIAgentMessages({
    contactId: "contact-123"
});

console.log("Messages:", result.messages);

// ListAIAgentMessagesParams Structure
{
  contactId?: string;
}

// ListAIAgentMessagesResult Structure
{
  contactId: string;
  messages: AIAgentMessageEvent[];
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
