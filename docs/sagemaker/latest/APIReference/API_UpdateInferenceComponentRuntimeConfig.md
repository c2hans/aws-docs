---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceComponentRuntimeConfig.html
---

# UpdateInferenceComponentRuntimeConfig
<a name="API_UpdateInferenceComponentRuntimeConfig"></a>

Runtime settings for a model that is deployed with an inference component.

## Request Syntax
<a name="API_UpdateInferenceComponentRuntimeConfig_RequestSyntax"></a>

```
{
   "DesiredRuntimeConfig": {
      "CopyCount": {{number}}
   },
   "InferenceComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateInferenceComponentRuntimeConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DesiredRuntimeConfig](#API_UpdateInferenceComponentRuntimeConfig_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponentRuntimeConfig-request-DesiredRuntimeConfig"></a>
Runtime settings for a model that is deployed with an inference component.
Type: [InferenceComponentRuntimeConfig](API_InferenceComponentRuntimeConfig.md) object
Required: Yes

 ** [InferenceComponentName](#API_UpdateInferenceComponentRuntimeConfig_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponentRuntimeConfig-request-InferenceComponentName"></a>
The name of the inference component to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## Response Syntax
<a name="API_UpdateInferenceComponentRuntimeConfig_ResponseSyntax"></a>

```
{
   "InferenceComponentArn": "string"
}
```

## Response Elements
<a name="API_UpdateInferenceComponentRuntimeConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceComponentArn](#API_UpdateInferenceComponentRuntimeConfig_ResponseSyntax) **   <a name="sagemaker-UpdateInferenceComponentRuntimeConfig-response-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_UpdateInferenceComponentRuntimeConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInferenceComponentRuntimeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateInferenceComponentRuntimeConfig)
