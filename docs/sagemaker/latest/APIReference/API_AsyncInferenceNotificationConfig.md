---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AsyncInferenceNotificationConfig.html
---

# AsyncInferenceNotificationConfig
<a name="API_AsyncInferenceNotificationConfig"></a>

Specifies the configuration for notifications of inference results for asynchronous inference.

## Contents
<a name="API_AsyncInferenceNotificationConfig_Contents"></a>

 ** ErrorTopic **   <a name="sagemaker-Type-AsyncInferenceNotificationConfig-ErrorTopic"></a>
Amazon SNS topic to post a notification to when inference fails. If no topic is provided, no notification is sent on failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sns:[a-z0-9\-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: No

 ** IncludeInferenceResponseIn **   <a name="sagemaker-Type-AsyncInferenceNotificationConfig-IncludeInferenceResponseIn"></a>
The Amazon SNS topics where you want the inference response to be included.
The inference response is included only if the response size is less than or equal to 128 KB.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `SUCCESS_NOTIFICATION_TOPIC | ERROR_NOTIFICATION_TOPIC`
Required: No

 ** SuccessTopic **   <a name="sagemaker-Type-AsyncInferenceNotificationConfig-SuccessTopic"></a>
Amazon SNS topic to post a notification to when inference completes successfully. If no topic is provided, no notification is sent on success.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sns:[a-z0-9\-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_AsyncInferenceNotificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AsyncInferenceNotificationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AsyncInferenceNotificationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AsyncInferenceNotificationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
