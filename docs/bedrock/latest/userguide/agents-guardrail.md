---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html
---

# Implement safeguards for your application by associating a guardrail with your agent
<a name="agents-guardrail"></a>

To implement safeguards and prevent unwanted behavior from model responses or user messages, associate a guardrail with your agent. To learn more about guardrails and how to create them, see [Detect and filter harmful content by using Amazon Bedrock Guardrails](guardrails.md).

You can associate a guardrail with your agent when you [create](agents-create.md) or [update](agents-edit.md) an agent. In the Amazon Bedrock console, you add a guardrail in the **Guardrail details** section of the **Agent builder**. In the Amazon Bedrock API, you specify a [GuardrailConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GuardrailConfiguration.html) when you send a [CreateAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgent.html) or [UpdateAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgent.html) request.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
