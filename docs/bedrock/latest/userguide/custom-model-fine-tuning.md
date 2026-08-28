---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html
---

# Customize a model with fine-tuning in Amazon Bedrock
<a name="custom-model-fine-tuning"></a>

With Amazon Bedrock, you can train a foundation model to improve performance on specific tasks (known as fine-tuning). For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](https://docs.aws.amazon.com/nova/latest/userguide/customize-fine-tune.html).

## Supported models and Regions for fine-tuning
<a name="custom-model-supported"></a>

The following table shows the foundation models that you can fine-tune:

| Provider | Model | Model ID | Single-region model support |
| --- | --- | --- | --- |
| Amazon | Nova 2 Lite | amazon.nova-2-lite-v1:0:256k | us-east-1 |
| Amazon | Nova Canvas | amazon.nova-canvas-v1:0 | us-east-1 |
| Amazon | Nova Lite | amazon.nova-lite-v1:0:300k | us-east-1 |
| Amazon | Nova Micro | amazon.nova-micro-v1:0:128k | us-east-1 |
| Amazon | Nova Pro | amazon.nova-pro-v1:0:300k | us-east-1 |
| Amazon | Titan Image Generator G1 v2 | amazon.titan-image-generator-v2:0 | us-east-1<br />us-west-2 |
| Amazon | Titan Multimodal Embeddings G1 | amazon.titan-embed-image-v1:0 | us-east-1<br />us-west-2 |
| Anthropic | Claude 3 Haiku | anthropic.claude-3-haiku-20240307-v1:0:200k | us-west-2 |
| Meta | Llama 3.1 70B Instruct | meta.llama3-1-70b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.1 8B Instruct | meta.llama3-1-8b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.2 11B Instruct | meta.llama3-2-11b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.2 1B Instruct | meta.llama3-2-1b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.2 3B Instruct | meta.llama3-2-3b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.2 90B Instruct | meta.llama3-2-90b-instruct-v1:0:128k | us-west-2 |
| Meta | Llama 3.3 70B Instruct | meta.llama3-3-70b-instruct-v1:0:128k | us-west-2 |

For information about model customization hyperparameters for each model, see [Custom model hyperparameters](custom-models-hp.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
