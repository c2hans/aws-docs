---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html
---

# DescribeInferenceExperiment
<a name="API_DescribeInferenceExperiment"></a>

Returns details about an inference experiment.

## Request Syntax
<a name="API_DescribeInferenceExperiment_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInferenceExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeInferenceExperiment_RequestSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-request-Name"></a>
The name of the inference experiment to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DescribeInferenceExperiment_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CompletionTime": number,
   "CreationTime": number,
   "DataStorageConfig": {
      "ContentType": {
         "CsvContentTypes": [ "string" ],
         "JsonContentTypes": [ "string" ]
      },
      "Destination": "string",
      "KmsKey": "string"
   },
   "Description": "string",
   "EndpointMetadata": {
      "EndpointConfigName": "string",
      "EndpointName": "string",
      "EndpointStatus": "string",
      "FailureReason": "string"
   },
   "KmsKey": "string",
   "LastModifiedTime": number,
   "ModelVariants": [
      {
         "InfrastructureConfig": {
            "InfrastructureType": "string",
            "RealTimeInferenceConfig": {
               "InstanceCount": number,
               "InstanceType": "string"
            }
         },
         "ModelName": "string",
         "Status": "string",
         "VariantName": "string"
      }
   ],
   "Name": "string",
   "RoleArn": "string",
   "Schedule": {
      "EndTime": number,
      "StartTime": number
   },
   "ShadowModeConfig": {
      "ShadowModelVariants": [
         {
            "SamplingPercentage": number,
            "ShadowModelVariantName": "string"
         }
      ],
      "SourceModelVariantName": "string"
   },
   "Status": "string",
   "StatusReason": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_DescribeInferenceExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Arn"></a>
The ARN of the inference experiment being described.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-experiment/.*`

 ** [CompletionTime](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-CompletionTime"></a>
 The timestamp at which the inference experiment was completed.
Type: Timestamp

 ** [CreationTime](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-CreationTime"></a>
The timestamp at which you created the inference experiment.
Type: Timestamp

 ** [DataStorageConfig](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-DataStorageConfig"></a>
The Amazon S3 location and configuration for storing inference request and response data.
Type: [InferenceExperimentDataStorageConfig](API_InferenceExperimentDataStorageConfig.md) object

 ** [Description](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Description"></a>
The description of the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`

 ** [EndpointMetadata](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-EndpointMetadata"></a>
The metadata of the endpoint on which the inference experiment ran.
Type: [EndpointMetadata](API_EndpointMetadata.md) object

 ** [KmsKey](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-KmsKey"></a>
 The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. For more information, see [CreateInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [LastModifiedTime](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-LastModifiedTime"></a>
The timestamp at which you last modified the inference experiment.
Type: Timestamp

 ** [ModelVariants](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-ModelVariants"></a>
 An array of `ModelVariantConfigSummary` objects. There is one for each variant in the inference experiment. Each `ModelVariantConfigSummary` object in the array describes the infrastructure configuration for deploying the corresponding variant.
Type: Array of [ModelVariantConfigSummary](API_ModelVariantConfigSummary.md) objects

 ** [Name](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Name"></a>
The name of the inference experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [RoleArn](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-RoleArn"></a>
 The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Schedule](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Schedule"></a>
The duration for which the inference experiment ran or will run.
Type: [InferenceExperimentSchedule](API_InferenceExperimentSchedule.md) object

 ** [ShadowModeConfig](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-ShadowModeConfig"></a>
 The configuration of `ShadowMode` inference experiment type, which shows the production variant that takes all the inference requests, and the shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also shows the percentage of requests that Amazon SageMaker replicates.
Type: [ShadowModeConfig](API_ShadowModeConfig.md) object

 ** [Status](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Status"></a>
 The status of the inference experiment. The following are the possible statuses for an inference experiment:
+  `Creating` - Amazon SageMaker is creating your experiment.
+  `Created` - Amazon SageMaker has finished the creation of your experiment and will begin the experiment at the scheduled time.
+  `Updating` - When you make changes to your experiment, your experiment shows as updating.
+  `Starting` - Amazon SageMaker is beginning your experiment.
+  `Running` - Your experiment is in progress.
+  `Stopping` - Amazon SageMaker is stopping your experiment.
+  `Completed` - Your experiment has completed.
+  `Cancelled` - When you conclude your experiment early using the [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html) API, or if any operation fails with an unexpected error, it shows as cancelled.
Type: String
Valid Values: `Creating | Created | Updating | Running | Starting | Stopping | Completed | Cancelled`

 ** [StatusReason](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-StatusReason"></a>
 The error message or client-specified `Reason` from the [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html) API, that explains the status of the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`

 ** [Type](#API_DescribeInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceExperiment-response-Type"></a>
The type of the inference experiment.
Type: String
Valid Values: `ShadowMode`

## Errors
<a name="API_DescribeInferenceExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInferenceExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeInferenceExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeInferenceExperiment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
