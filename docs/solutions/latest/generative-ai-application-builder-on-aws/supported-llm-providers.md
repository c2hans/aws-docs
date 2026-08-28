---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/supported-llm-providers.html
---

# Supported LLM providers
<a name="supported-llm-providers"></a>

The solution can integrate with the following LLM providers:

1. Amazon Bedrock
   + Documentation: https://aws.amazon.com/bedrock/
   + Supported models:
     + Amazon
       + Nova Lite
       + Nova Micro
       + Nova Pro
     + AI21 Labs
       + Jamba 1.5 Mini
       + Jamba 1.5 Large
     + Anthropic
       + Claude v3 Haiku
       + Claude v3.5 Sonnet
       + Claude v3.7 Sonnet (through the use of inference profiles)
     + Cohere
       + Command R
       + Command R\+
     + Deepseek
       + Deepseek-R1 (through the use of inference profiles)
     + Meta
       + Llama 3
       + Llama 3.2 (through the use of inference profiles)
     + Mistral AI
       + Mistral 7B Instruct
       + Mistral 8x7B Instruct
     + Cross-region inference
       + Ability to use inference profiles defined in the same Region as the Deployment dashboard

1. Amazon SageMaker AI
   + Documentation: https://aws.amazon.com/sagemaker/
   + Supported models: Text to Text models

For the latest model parameters, best practices, and recommended uses, refer to the documentation from the model providers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
