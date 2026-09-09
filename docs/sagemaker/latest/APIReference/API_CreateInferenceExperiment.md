---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html
---

# CreateInferenceExperiment
<a name="API_CreateInferenceExperiment"></a>

 Creates an inference experiment using the configurations specified in the request.

 Use this API to setup and schedule an experiment to compare model variants on a Amazon SageMaker inference endpoint. For more information about inference experiments, see [Shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html).

 Amazon SageMaker begins your experiment at the scheduled time and routes traffic to your endpoint's model variants based on your specified configuration.

 While the experiment is in progress or after it has concluded, you can view metrics that compare your model variants. For more information, see [View, monitor, and edit shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit.html).

## Request Syntax
<a name="API_CreateInferenceExperiment_RequestSyntax"></a>

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
   "EndpointName": "{{string}}",
   "KmsKey": "{{string}}",
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
   "RoleArn": "{{string}}",
   "Schedule": {
   },
   "ShadowModeConfig": {
      "ShadowModelVariants": [
         {
            "SamplingPercentage": {{number}},
            "ShadowModelVariantName": "{{string}}"
         }
      ],
      "SourceModelVariantName": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateInferenceExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataStorageConfig](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-DataStorageConfig"></a>
 The Amazon S3 location and configuration for storing inference request and response data.
 This is an optional parameter that you can use for data capture. For more information, see [Capture data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html).
Type: [InferenceExperimentDataStorageConfig](API_InferenceExperimentDataStorageConfig.md) object
Required: No

 ** [Description](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-Description"></a>
A description for the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [EndpointName](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-EndpointName"></a>
 The name of the Amazon SageMaker endpoint on which you want to run the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [KmsKey](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-KmsKey"></a>
 The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. The `KmsKey` can be any of the following formats:
+ KMS key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
+ KMS key Alias

   `"alias/ExampleAlias"`
+ Amazon Resource Name (ARN) of a KMS key Alias

   `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`
 If you use a KMS key ID or an alias of your KMS key, the Amazon SageMaker execution role must include permissions to call `kms:Encrypt`. If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. Amazon SageMaker uses server-side encryption with KMS managed keys for `OutputDataConfig`. If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"`. For more information, see [KMS managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*
 The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint` and `UpdateEndpoint` requests. For more information, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [ModelVariants](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-ModelVariants"></a>
 An array of `ModelVariantConfig` objects. There is one for each variant in the inference experiment. Each `ModelVariantConfig` object in the array describes the infrastructure configuration for the corresponding variant.
Type: Array of [ModelVariantConfig](API_ModelVariantConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [Name](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-Name"></a>
The name for the inference experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [RoleArn](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-RoleArn"></a>
 The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Schedule](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-Schedule"></a>
 The duration for which you want the inference experiment to run. If you don't specify this field, the experiment automatically starts immediately upon creation and concludes after 7 days.
Type: [InferenceExperimentSchedule](API_InferenceExperimentSchedule.md) object
Required: No

 ** [ShadowModeConfig](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-ShadowModeConfig"></a>
 The configuration of `ShadowMode` inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates.
Type: [ShadowModeConfig](API_ShadowModeConfig.md) object
Required: Yes

 ** [Tags](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-Tags"></a>
 Array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging your AWS Resources](https://docs.aws.amazon.com/ARG/latest/userguide/tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Type](#API_CreateInferenceExperiment_RequestSyntax) **   <a name="sagemaker-CreateInferenceExperiment-request-Type"></a>
 The type of the inference experiment that you want to run. The following types of experiments are possible:
+  `ShadowMode`: You can use this type to validate a shadow variant. For more information, see [Shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html).
Type: String
Valid Values: `ShadowMode`
Required: Yes

## Response Syntax
<a name="API_CreateInferenceExperiment_ResponseSyntax"></a>

```
{
   "InferenceExperimentArn": "string"
}
```

## Response Elements
<a name="API_CreateInferenceExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExperimentArn](#API_CreateInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-CreateInferenceExperiment-response-InferenceExperimentArn"></a>
The ARN for your inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-experiment/.*`

## Errors
<a name="API_CreateInferenceExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateInferenceExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateInferenceExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateInferenceExperiment)
