---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceRouterSummary.html
---

# InferenceRouterSummary
<a name="API_InferenceRouterSummary"></a>

A summary of an inference router.

## Contents
<a name="API_InferenceRouterSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-InferenceRouterSummary-CreationTime"></a>
The date and time that the inference router was created.
Type: Timestamp
Required: Yes

 ** InferenceRouterArn **   <a name="sagemaker-Type-InferenceRouterSummary-InferenceRouterArn"></a>
The Amazon Resource Name (ARN) of the inference router.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:inference-router/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** InferenceRouterName **   <a name="sagemaker-Type-InferenceRouterSummary-InferenceRouterName"></a>
The name of the inference router.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-InferenceRouterSummary-LastModifiedTime"></a>
The date and time that the inference router was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_InferenceRouterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceRouterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceRouterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceRouterSummary)
