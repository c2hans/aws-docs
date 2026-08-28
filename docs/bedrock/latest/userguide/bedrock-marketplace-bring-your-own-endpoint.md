---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.html
---

# Bring your own endpoint
<a name="bedrock-marketplace-bring-your-own-endpoint"></a>

You can register an endpoint hosting an Amazon Bedrock AWS Marketplace model you've created in SageMaker AI. During the registration process, the models are checked for compatibility with Amazon Bedrock Marketplace requirements. You must have network isolation enabled on your endpoints. Additionally, you can't change the model artifacts from the base model that the provider supplies.

For more information about registering the endpoint, see [Use your SageMaker AI JumpStart Models in Amazon Bedrock](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-register-bedrock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
