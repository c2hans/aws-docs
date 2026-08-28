---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CallbackStepMetadata.html
---

# CallbackStepMetadata
<a name="API_CallbackStepMetadata"></a>

Metadata about a callback step.

## Contents
<a name="API_CallbackStepMetadata_Contents"></a>

 ** CallbackToken **   <a name="sagemaker-Type-CallbackStepMetadata-CallbackToken"></a>
The pipeline generated token from the Amazon SQS queue.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** OutputParameters **   <a name="sagemaker-Type-CallbackStepMetadata-OutputParameters"></a>
A list of the output parameters of the callback step.
Type: Array of [OutputParameter](API_OutputParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** SqsQueueUrl **   <a name="sagemaker-Type-CallbackStepMetadata-SqsQueueUrl"></a>
The URL of the Amazon Simple Queue Service (Amazon SQS) queue used by the callback step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CallbackStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CallbackStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CallbackStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CallbackStepMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
