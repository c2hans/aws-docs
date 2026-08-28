---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-evaluators-overview.html
---

# Built-in evaluators
<a name="built-in-evaluators-overview"></a>

Built-in evaluators in AgentCore Evaluations provide pre-configured evaluators for assessing your agents. These evaluators use predefined evaluator models and prompt templates that have been optimized for common evaluation scenarios.

You can use built-in evaluators with on-demand, batch, and online evaluations. To specify a built-in evaluator, use its ID in the following format: `Builtin.EvaluatorName` , such as `Builtin.Helpfulness`.

**Note**
Built-in evaluator configurations, including their evaluator models and prompt templates, cannot be modified.

For evaluators that only apply when a tool call loads a skill, see [Skill evaluators](skill-evaluators.md).

**Topics**
+ [Cross region inference](evaluations-cross-region-inference.md)
+ [Skill evaluators](skill-evaluators.md)
+ [Prompt templates](prompt-templates-builtin.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
