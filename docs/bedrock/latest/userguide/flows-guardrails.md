---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-guardrails.html
---

# Include guardrails in your flow in Amazon Bedrock
<a name="flows-guardrails"></a>

Amazon Bedrock Flows integrates with Amazon Bedrock Guardrails to let you identify and block or filter unwanted content in your flow. To learn how to apply guardrails to supported node types in a flow, see the following table:

| Node type | Console | API |
| --- | --- | --- |
| Prompt node | When you [create](flows-create.md) or [update](flows-modify.md) a flow, select the prompt node and specify the guardrail in the Configure section. | When you define the prompt node in the nodes field in a [CreateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlow.html) or [UpdateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateFlow.html) request, include a guardrailConfiguration field in the [PromptFlowNodeConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptFlowNodeConfiguration.html). |
| Knowledge base node | When you [create](flows-create.md) or [update](flows-modify.md) a flow, select the knowledge base node and specify the guardrail in the Configure section. You can only include a guardrail when generating responses based on retrieved results. | When you define the knowledge base node in the nodes field in a [CreateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlow.html) or [UpdateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateFlow.html) request, include a guardrailConfiguration field in the [KnowledgeBaseFlowNodeConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_KnowledgeBaseFlowNodeConfiguration.html). You can only include a guardrail when using RetrieveAndGenerate so you must include a modelId. |

For more information about guardrails, see [Detect and filter harmful content by using Amazon Bedrock Guardrails](guardrails.md).

For more information about node types, see [Node types for your flow](flows-nodes.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
