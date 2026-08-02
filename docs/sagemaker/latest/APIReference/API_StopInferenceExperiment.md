---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html
---

# StopInferenceExperiment
<a name="API_StopInferenceExperiment"></a>

Stops an inference experiment.

## Request Syntax
<a name="API_StopInferenceExperiment_RequestSyntax"></a>

```
{
   "DesiredModelVariants": [
      {
         "InfrastructureConfig": {
            "InfrastructureType": "{{string}}",
            "RealTimeInferenceConfig": {
               "InstanceCount": {{number}},
               "InstanceType": "{{string}}"
            }
         },
         "ModelName": "{{string}}",
         "VariantName": "{{string}}"
      }
   ],
   "DesiredState": "{{string}}",
   "ModelVariantActions": {
      "{{string}}" : "{{string}}"
   },
   "Name": "{{string}}",
   "Reason": "{{string}}"
}
```

## Request Parameters
<a name="API_StopInferenceExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DesiredModelVariants](#API_StopInferenceExperiment_RequestSyntax) **   <a name="sagemaker-StopInferenceExperiment-request-DesiredModelVariants"></a>
 An array of `ModelVariantConfig` objects. There is one for each variant that you want to deploy after the inference experiment stops. Each `ModelVariantConfig` describes the infrastructure configuration for deploying the corresponding variant.
Type: Array of [ModelVariantConfig](API_ModelVariantConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [DesiredState](#API_StopInferenceExperiment_RequestSyntax) **   <a name="sagemaker-StopInferenceExperiment-request-DesiredState"></a>
 The desired state of the experiment after stopping. The possible states are the following:
+  `Completed`: The experiment completed successfully
+  `Cancelled`: The experiment was canceled
Type: String
Valid Values: `Completed | Cancelled`
Required: No

 ** [ModelVariantActions](#API_StopInferenceExperiment_RequestSyntax) **   <a name="sagemaker-StopInferenceExperiment-request-ModelVariantActions"></a>
 Array of key-value pairs, with names of variants mapped to actions. The possible actions are the following:
+  `Promote` - Promote the shadow variant to a production variant
+  `Remove` - Delete the variant
+  `Retain` - Keep the variant as it is
Type: String to string map
Map Entries: Maximum number of 2 items.
Key Length Constraints: Minimum length of 0. Maximum length of 63.
Key Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Valid Values: `Retain | Remove | Promote`
Required: Yes

 ** [Name](#API_StopInferenceExperiment_RequestSyntax) **   <a name="sagemaker-StopInferenceExperiment-request-Name"></a>
The name of the inference experiment to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [Reason](#API_StopInferenceExperiment_RequestSyntax) **   <a name="sagemaker-StopInferenceExperiment-request-Reason"></a>
The reason for stopping the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_StopInferenceExperiment_ResponseSyntax"></a>

```
{
   "InferenceExperimentArn": "string"
}
```

## Response Elements
<a name="API_StopInferenceExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExperimentArn](#API_StopInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-StopInferenceExperiment-response-InferenceExperimentArn"></a>
The ARN of the stopped inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-experiment/.*`

## Errors
<a name="API_StopInferenceExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StopInferenceExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StopInferenceExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StopInferenceExperiment)
