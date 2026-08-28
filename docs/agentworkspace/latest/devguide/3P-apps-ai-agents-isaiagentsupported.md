---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-isaiagentsupported.html
---

# Check if AI Agent is supported
<a name="3P-apps-ai-agents-isaiagentsupported"></a>

Checks whether the Connect Customer instance has an AI Agent configured.

 **Signature**

```
isAIAgentSupported(): Promise<AIAgentSupportedResult>
```

 **Usage**

```
const result = await aiAgentsClient.isAIAgentSupported();
console.log("AI Agent supported:", result.isSupported);

// AIAgentSupportedResult Structure
{
  isSupported: boolean;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
