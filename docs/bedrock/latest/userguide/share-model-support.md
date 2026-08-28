---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-support.html
---

# Supported Regions and models for model sharing
<a name="share-model-support"></a>

The following list provides links to general information about Regional and model support in Amazon Bedrock:
+ For a list of Region codes and endpoints supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bedrock_region).
+ For a list of Amazon Bedrock model IDs to use when calling Amazon Bedrock API operations, see [Supported foundation models in Amazon Bedrock](models-supported.md).

The following table shows the models that you can share and the Regions from which you can share:

| Provider | Model | Model ID | Single-region model support |
| --- | --- | --- | --- |
| Amazon | Titan Multimodal Embeddings G1 | amazon.titan-embed-image-v1 | ap-south-1<br />ap-southeast-2<br />eu-west-1<br />eu-west-3<br />us-east-1<br />us-west-2 |
| Anthropic | Claude 3 Haiku | anthropic.claude-3-haiku-20240307-v1:0 | ap-south-1<br />ap-southeast-2<br />eu-west-1<br />eu-west-2<br />us-east-1<br />us-west-2 |

**Note**
Custom Amazon Titan Text Premier models aren't shareable because they can't be [copied to a Region](copy-model.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
