---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/advanced-llm-settings.html
---

# Advanced LLM Settings
<a name="advanced-llm-settings"></a>

While using Amazon Bedrock, you can configure some advanced settings for your models such as Amazon Bedrock Guardrails, Provisioned Throughput for Amazon Bedrock, and additional model parameters.

## Amazon Bedrock Guardrails
<a name="guardrails-for-amazon-bedrock"></a>

Amazon Bedrock Guardrails is a feature with Amazon Bedrock which evaluates user inputs and LLM responses based on user configured policies and provides an additional layer of safeguards, regardless of the underlying LLM that the user selects for a use case. A Guardrail consists of 2 policies to avoid content that falls into undesirable or harmful categories:

1. Denied topics to define a set of topics that are undesirable in the context of user’s application, for example, investment advice in a financial application, and,

1. Content filters\*\*\*\*which allows filtering input user prompts or model responses containing harmful content.

For usage in Generative AI Application Builder solution, a Guardrail must be configured in the *Amazon Bedrock* console using the *Create guardrail* wizard. Once created, you can add this Guardrail to your chat use case created through Generative AI Application Builder solution wizard in the **Additional settings** in the Model Selection step by supplying your Guardrail Identifier and Guardrail version.

 **Depicts Deployment wizard - enabling Amazon Bedrock Guardrails**

![guardrails for bedrock](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/guardrails-for-bedrock.png)

## Provisioned Throughput for Amazon Bedrock
<a name="provisioned-throughput-for-amazon-bedrock"></a>

Each on-demand Amazon Bedrock model follows region-specific [account quota limit](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) for model inferencing. For example, Anthropic Claude 2.x on Bedrock currently allows for 500 requests and 500,000 tokens processed per minute in us-east-1 and us-west-2 regions. You may also want to use the solution with your fine-tuned or continued pre-trained models. For such instances, Amazon Bedrock allows [provisioned throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) which allows running large consistent inference workloads for your base, fine-tuned or continued pre-trained models for use in production-grade applications.

Once Provisioned Throughput is purchased within the Amazon Bedrock console, a Model ARN is generated for usage. You can now supply this Model ARN in the Generative AI Application Builder wizard in the Model selection step. To do so, select Bedrock as the model provider and the base model name which was used to generate this provisioned Model ARN in Amazon Bedrock console. Then, select '**Provisioned model'** when choosing between on-demand and provisioned models, and supply your Model ARN.

 **Depicts Deployment wizard - Enabling Provisioned Throughput for Amazon Bedrock**

![provisioned throughput for bedrock](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/provisioned-throughput-for-bedrock.png)

**Note**
Your guardrail and provisioned throughput must be in the same Region as the deployed Deployment Dashboard and use case stacks.

## Model parameters
<a name="model-parameters"></a>

LLMs often accept a wide range of parameters specific to its implementation. Model providers often provide documentation outlining the set of supported parameters and their uses.

The solution passes model parameters directly through to the underlying model so it is important to ensure parameters are set correctly. Refer to the model provider’s documentation for the latest information on supported parameters.
