---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-deploy.html
---

# Deploy and use an Amazon Bedrock agent in your application
<a name="agents-deploy"></a>

**Note**
Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html). Existing customers can continue to use the service as normal. For more information, see [Amazon Bedrock Agents Classic maintenance mode](agents-classic-maintenance-mode.md).

Before you can use an agent, you must deploy the agent by creating an alias. You can then use the agent in your application by calling the [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) operation. In this section, you learn how to create and manage an alias and how to call your agent from an application.

**Topics**
+ [Deploy an agent](deploy-agent.md)
+ [Invoke an agent from your application](agents-invoke-agent.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
