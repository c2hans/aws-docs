---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RoutingTargetAsyncInferenceOutputConfig.html
---

# RoutingTargetAsyncInferenceOutputConfig
<a name="API_RoutingTargetAsyncInferenceOutputConfig"></a>

The output settings for the asynchronous requests of a routing target. Every destination writes to the same locations. `CreateInferenceRouter` and `UpdateInferenceRouter` don't check who owns the buckets. If another account owns the output bucket, requests fail.

## Contents
<a name="API_RoutingTargetAsyncInferenceOutputConfig_Contents"></a>

 ** S3FailurePath **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceOutputConfig-S3FailurePath"></a>
The Amazon S3 location for the failure details of failed requests. The bucket must be in the inference router's AWS Region and owned by the router's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** S3OutputPath **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceOutputConfig-S3OutputPath"></a>
The Amazon S3 location for the results of successful requests. The bucket must be in the inference router's AWS Region and owned by the router's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceOutputConfig-KmsKeyId"></a>
The AWS KMS key that encrypts the results in Amazon S3. You can specify a key ID, key ARN, alias name, or alias ARN. If any destination is in a different account or AWS Region from the inference router, specify a key ARN or an alias ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** NotificationConfig **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceOutputConfig-NotificationConfig"></a>
The Amazon SNS topics that the inference router publishes to when a request completes or fails.
Type: [RoutingTargetAsyncInferenceNotificationConfig](API_RoutingTargetAsyncInferenceNotificationConfig.md) object
Required: No

## See Also
<a name="API_RoutingTargetAsyncInferenceOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RoutingTargetAsyncInferenceOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RoutingTargetAsyncInferenceOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RoutingTargetAsyncInferenceOutputConfig)
