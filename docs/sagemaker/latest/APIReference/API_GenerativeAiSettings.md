---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GenerativeAiSettings.html
---

# GenerativeAiSettings
<a name="API_GenerativeAiSettings"></a>

The generative AI settings for the SageMaker Canvas application.

Configure these settings for Canvas users starting chats with generative AI foundation models. For more information, see [ Use generative AI with foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat.html).

## Contents
<a name="API_GenerativeAiSettings_Contents"></a>

 ** AmazonBedrockRoleArn **   <a name="sagemaker-Type-GenerativeAiSettings-AmazonBedrockRoleArn"></a>
The ARN of an AWS IAM role that allows fine-tuning of large language models (LLMs) in Amazon Bedrock. The IAM role should have Amazon S3 read and write permissions, as well as a trust relationship that establishes `bedrock.amazonaws.com` as a service principal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_GenerativeAiSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GenerativeAiSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GenerativeAiSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GenerativeAiSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
