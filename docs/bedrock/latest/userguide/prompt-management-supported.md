---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-supported.html
---

# Supported Regions and models for Prompt management
<a name="prompt-management-supported"></a>

Prompt management is supported in the following AWS Regions:
+ ap-northeast-1
+ ap-northeast-2
+ ap-northeast-3
+ ap-south-1
+ ap-south-2
+ ap-southeast-1
+ ap-southeast-2
+ ca-central-1
+ eu-central-1
+ eu-central-2
+ eu-north-1
+ eu-south-1
+ eu-south-2
+ eu-west-1
+ eu-west-2
+ eu-west-3
+ sa-east-1
+ us-east-1
+ us-east-2
+ us-gov-east-1
+ us-gov-west-1
+ us-west-2

You can use Prompt management with any text model supported for the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) API. For a list of supported models, see [models at a glance](model-cards.md).

**Note**
[InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) only work on prompts from Prompt management whose configuration specifies an Anthropic Claude or Meta Llama model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
