---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-deploy-agent.html
---

# Create and deploy your agent
<a name="create-deploy-agent"></a>

If you have an agent already up and running in AgentCore Runtime, you can skip the following steps

**Topics**
+ [Pick a supported framework](#create-deploy-agent-frameworks)
+ [Create and deploy your agent](#create-deploy-agent-steps)

## Pick a supported framework
<a name="create-deploy-agent-frameworks"></a>

Build your agent with a framework and instrumentation library that AgentCore Evaluations supports. For more information about supported frameworks and instrumentation libraries, see [Supported agent frameworks](supported-frameworks.md).

## Create and deploy your agent
<a name="create-deploy-agent-steps"></a>

Create and deploy your agent by following the [Get Started guide for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started.html) . Setup observability using [Get started with AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) . You can find additional examples in the [AgentCore Evaluations Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-features/06-observe-evaluate-optimize-your-agent/02-evaluate).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
