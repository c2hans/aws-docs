---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RoutingTargetAsyncInferenceNotificationConfig.html
---

# RoutingTargetAsyncInferenceNotificationConfig

The Amazon SNS topics that the inference router publishes to. The router publishes one notification for each request. The notification contains the location of the result, not the result itself. The destination endpoints also send their own notifications, if they're configured to.

## Contents
<a name="API_RoutingTargetAsyncInferenceNotificationConfig_Contents"></a>

 ** ErrorTopic **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceNotificationConfig-ErrorTopic"></a>
The ARN of the Amazon SNS topic to publish to when a request fails, or when the router can't place it on any destination. The topic must be a standard topic, and can be in any AWS Region.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sns:[a-z0-9-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: No

 ** SuccessTopic **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceNotificationConfig-SuccessTopic"></a>
The ARN of the Amazon SNS topic to publish to when a request completes. The topic must be a standard topic, and can be in any AWS Region.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sns:[a-z0-9-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_RoutingTargetAsyncInferenceNotificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RoutingTargetAsyncInferenceNotificationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RoutingTargetAsyncInferenceNotificationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RoutingTargetAsyncInferenceNotificationConfig)
