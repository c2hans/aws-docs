---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AsyncInferenceOutputConfig.html
---

# AsyncInferenceOutputConfig
<a name="API_AsyncInferenceOutputConfig"></a>

Specifies the configuration for asynchronous inference invocation outputs.

## Contents
<a name="API_AsyncInferenceOutputConfig_Contents"></a>

 ** KmsKeyId **   <a name="sagemaker-Type-AsyncInferenceOutputConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that SageMaker uses to encrypt the asynchronous inference output in Amazon S3.

Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** NotificationConfig **   <a name="sagemaker-Type-AsyncInferenceOutputConfig-NotificationConfig"></a>
Specifies the configuration for notifications of inference results for asynchronous inference.
Type: [AsyncInferenceNotificationConfig](API_AsyncInferenceNotificationConfig.md) object
Required: No

 ** S3FailurePath **   <a name="sagemaker-Type-AsyncInferenceOutputConfig-S3FailurePath"></a>
The Amazon S3 location to upload failure inference responses to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: No

 ** S3OutputPath **   <a name="sagemaker-Type-AsyncInferenceOutputConfig-S3OutputPath"></a>
The Amazon S3 location to upload inference responses to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: No

## See Also
<a name="API_AsyncInferenceOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AsyncInferenceOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AsyncInferenceOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AsyncInferenceOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
