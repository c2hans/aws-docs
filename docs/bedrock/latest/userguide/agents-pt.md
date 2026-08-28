---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-pt.html
---

# Provision additional throughput for your agent's model
<a name="agents-pt"></a>

**Note**
Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html). Existing customers can continue to use the service as normal. For more information, see [Amazon Bedrock Agents Classic maintenance mode](agents-classic-maintenance-mode.md).

To increase the rate and number of tokens that the agent can process during model inference, associate a Provisioned Throughput that you've purchased for the model that your agent is using. To learn more about Provisioned Throughput and how to purchase it, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md).

You can associate a Provisioned Throughput when you [create](agents-deploy.md) or [update](agents-alias-edit.md) an agent alias. In the Amazon Bedrock console, you choose the Provisioned Throughput when setting up the alias or editing it. In the Amazon Bedrock API, you specify the `provisionedThroughput` in the `routingConfiguration` when you send a [CreateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentAlias.html) or [UpdateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentAlias.html); request.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
