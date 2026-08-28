---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model-support.html
---

# Supported Regions and models for model copy
<a name="copy-model-support"></a>

The following list provides links to general information about Regional and model support in Amazon Bedrock:
+ For a list of Region codes and endpoints supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bedrock_region).
+ For a list of Amazon Bedrock model IDs to use when calling Amazon Bedrock API operations, see [Supported foundation models in Amazon Bedrock](models-supported.md).

The following table shows the models whose customized version you can copy and the Regions to which you can copy them:

| Provider | Model | Model ID | Single-region model support |
| --- | --- | --- | --- |
| Amazon | Nova Canvas | amazon.nova-canvas-v1:0 | ap-northeast-2<br />eu-west-1<br />us-east-1 |
| Amazon | Nova Lite | amazon.nova-lite-v1:0 | ap-northeast-1<br />ap-northeast-2<br />ap-south-1<br />ap-southeast-1<br />ap-southeast-2<br />eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3<br />us-east-1<br />us-east-2<br />us-gov-west-1<br />us-west-2 |
| Amazon | Nova Micro | amazon.nova-micro-v1:0 | ap-northeast-1<br />ap-northeast-2<br />ap-south-1<br />ap-southeast-1<br />ap-southeast-2<br />eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3<br />us-east-1<br />us-east-2<br />us-gov-west-1<br />us-west-2 |
| Amazon | Nova Pro | amazon.nova-pro-v1:0 | ap-northeast-1<br />ap-northeast-2<br />ap-south-1<br />ap-southeast-1<br />ap-southeast-2<br />eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3<br />us-east-1<br />us-east-2<br />us-gov-west-1<br />us-west-2 |
| Amazon | Titan Multimodal Embeddings G1 | amazon.titan-embed-image-v1 | ap-south-1<br />ap-southeast-2<br />ca-central-1<br />eu-west-1<br />eu-west-2<br />eu-west-3<br />sa-east-1<br />us-east-1<br />us-west-2 |
| Anthropic | Claude 3 Haiku | anthropic.claude-3-haiku-20240307-v1:0 | ap-south-1<br />ap-southeast-2<br />eu-west-1<br />eu-west-2<br />us-east-1<br />us-west-2 |
| Meta | Llama 3.1 405B Instruct | meta.llama3-1-405b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.1 70B Instruct | meta.llama3-1-70b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.1 8B Instruct | meta.llama3-1-8b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.2 11B Instruct | meta.llama3-2-11b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.2 1B Instruct | meta.llama3-2-1b-instruct-v1:0 | eu-central-1<br />eu-west-1<br />eu-west-3<br />us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.2 3B Instruct | meta.llama3-2-3b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |
| Meta | Llama 3.2 90B Instruct | meta.llama3-2-90b-instruct-v1:0 | us-east-1<br />us-east-2<br />us-west-2 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
