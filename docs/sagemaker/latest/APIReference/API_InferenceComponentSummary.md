---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentSummary.html
---

# InferenceComponentSummary
<a name="API_InferenceComponentSummary"></a>

A summary of the properties of an inference component.

## Contents
<a name="API_InferenceComponentSummary_Contents"></a>

 ** EndpointArn **   <a name="sagemaker-Type-InferenceComponentSummary-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-InferenceComponentSummary-EndpointName"></a>
The name of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** InferenceComponentArn **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** InferenceComponentName **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentName"></a>
The name of the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** VariantName **   <a name="sagemaker-Type-InferenceComponentSummary-VariantName"></a>
The name of the production variant that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** InferenceComponentStatus **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentStatus"></a>
The status of the inference component.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Deleting`
Required: No

## See Also
<a name="API_InferenceComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentSummary)
