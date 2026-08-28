---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceExperiment.html
---

# UpdateInferenceExperiment
<a name="API_UpdateInferenceExperiment"></a>

 Updates an inference experiment that you created. The status of the inference experiment has to be either `Created`, `Running`. For more information on the status of an inference experiment, see [DescribeInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html).

## Request Syntax
<a name="API_UpdateInferenceExperiment_RequestSyntax"></a>

```
{
   "DataStorageConfig": {
      "ContentType": {
         "CsvContentTypes": [ "{{string}}" ],
         "JsonContentTypes": [ "{{string}}" ]
      },
      "Destination": "{{string}}",
      "KmsKey": "{{string}}"
   },
   "Description": "{{string}}",
   "ModelVariants": [
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
   "Name": "{{string}}",
   "Schedule": {
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "ShadowModeConfig": {
      "ShadowModelVariants": [
         {
            "SamplingPercentage": {{number}},
            "ShadowModelVariantName": "{{string}}"
         }
      ],
      "SourceModelVariantName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateInferenceExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataStorageConfig](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-DataStorageConfig"></a>
The Amazon S3 location and configuration for storing inference request and response data.
Type: [InferenceExperimentDataStorageConfig](API_InferenceExperimentDataStorageConfig.md) object
Required: No

 ** [Description](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-Description"></a>
The description of the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ModelVariants](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-ModelVariants"></a>
 An array of `ModelVariantConfig` objects. There is one for each variant, whose infrastructure configuration you want to update.
Type: Array of [ModelVariantConfig](API_ModelVariantConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [Name](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-Name"></a>
The name of the inference experiment to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [Schedule](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-Schedule"></a>
 The duration for which the inference experiment will run. If the status of the inference experiment is `Created`, then you can update both the start and end dates. If the status of the inference experiment is `Running`, then you can update only the end date.
Type: [InferenceExperimentSchedule](API_InferenceExperimentSchedule.md) object
Required: No

 ** [ShadowModeConfig](#API_UpdateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-request-ShadowModeConfig"></a>
 The configuration of `ShadowMode` inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates.
Type: [ShadowModeConfig](API_ShadowModeConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateInferenceExperiment_ResponseSyntax"></a>

```
{
   "InferenceExperimentArn": "string"
}
```

## Response Elements
<a name="API_UpdateInferenceExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExperimentArn](#API_UpdateInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-UpdateInferenceExperiment-response-InferenceExperimentArn"></a>
The ARN of the updated inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-experiment/.*`

## Errors
<a name="API_UpdateInferenceExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInferenceExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateInferenceExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateInferenceExperiment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
