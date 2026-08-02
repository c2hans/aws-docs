---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html
---

# CreateProcessingJob
<a name="API_CreateProcessingJob"></a>

Creates a processing job.

## Request Syntax
<a name="API_CreateProcessingJob_RequestSyntax"></a>

```
{
   "AppSpecification": {
      "ContainerArguments": [ "{{string}}" ],
      "ContainerEntrypoint": [ "{{string}}" ],
      "ImageUri": "{{string}}"
   },
   "Environment": {
      "{{string}}" : "{{string}}"
   },
   "ExperimentConfig": {
      "ExperimentName": "{{string}}",
      "RunName": "{{string}}",
      "TrialComponentDisplayName": "{{string}}",
      "TrialName": "{{string}}"
   },
   "NetworkConfig": {
      "EnableInterContainerTrafficEncryption": {{boolean}},
      "EnableNetworkIsolation": {{boolean}},
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "ProcessingInputs": [
      {
         "AppManaged": {{boolean}},
         "DatasetDefinition": {
            "AthenaDatasetDefinition": {
               "Catalog": "{{string}}",
               "Database": "{{string}}",
               "KmsKeyId": "{{string}}",
               "OutputCompression": "{{string}}",
               "OutputFormat": "{{string}}",
               "OutputS3Uri": "{{string}}",
               "QueryString": "{{string}}",
               "WorkGroup": "{{string}}"
            },
            "DataDistributionType": "{{string}}",
            "InputMode": "{{string}}",
            "LocalPath": "{{string}}",
            "RedshiftDatasetDefinition": {
               "ClusterId": "{{string}}",
               "ClusterRoleArn": "{{string}}",
               "Database": "{{string}}",
               "DbUser": "{{string}}",
               "KmsKeyId": "{{string}}",
               "OutputCompression": "{{string}}",
               "OutputFormat": "{{string}}",
               "OutputS3Uri": "{{string}}",
               "QueryString": "{{string}}"
            }
         },
         "InputName": "{{string}}",
         "S3Input": {
            "LocalPath": "{{string}}",
            "S3CompressionType": "{{string}}",
            "S3DataDistributionType": "{{string}}",
            "S3DataType": "{{string}}",
            "S3InputMode": "{{string}}",
            "S3Uri": "{{string}}"
         }
      }
   ],
   "ProcessingJobName": "{{string}}",
   "ProcessingOutputConfig": {
      "KmsKeyId": "{{string}}",
      "Outputs": [
         {
            "AppManaged": {{boolean}},
            "FeatureStoreOutput": {
               "FeatureGroupName": "{{string}}"
            },
            "OutputName": "{{string}}",
            "S3Output": {
               "LocalPath": "{{string}}",
               "S3UploadMode": "{{string}}",
               "S3Uri": "{{string}}"
            }
         }
      ]
   },
   "ProcessingResources": {
      "ClusterConfig": {
         "InstanceCount": {{number}},
         "InstanceType": "{{string}}",
         "VolumeKmsKeyId": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   },
   "RoleArn": "{{string}}",
   "StoppingCondition": {
      "MaxRuntimeInSeconds": {{number}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateProcessingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppSpecification](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-AppSpecification"></a>
Configures the processing job to run a specified Docker container image.
Type: [AppSpecification](API_AppSpecification.md) object
Required: Yes

 ** [Environment](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-Environment"></a>
The environment variables to set in the Docker container. Up to 100 key and values entries in the map are supported.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

 ** [ExperimentConfig](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** [NetworkConfig](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-NetworkConfig"></a>
Networking options for a processing job, such as whether to allow inbound and outbound network calls to and from processing containers, and the VPC subnets and security groups to use for VPC-enabled processing jobs.
Type: [NetworkConfig](API_NetworkConfig.md) object
Required: No

 ** [ProcessingInputs](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-ProcessingInputs"></a>
An array of inputs configuring the data to download into the processing container.
Type: Array of [ProcessingInput](API_ProcessingInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [ProcessingJobName](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-ProcessingJobName"></a>
 The name of the processing job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ProcessingOutputConfig](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-ProcessingOutputConfig"></a>
Output configuration for the processing job.
Type: [ProcessingOutputConfig](API_ProcessingOutputConfig.md) object
Required: No

 ** [ProcessingResources](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-ProcessingResources"></a>
Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.
Type: [ProcessingResources](API_ProcessingResources.md) object
Required: Yes

 ** [RoleArn](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingCondition](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-StoppingCondition"></a>
The time limit for how long the processing job is allowed to run.
Type: [ProcessingStoppingCondition](API_ProcessingStoppingCondition.md) object
Required: No

 ** [Tags](#API_CreateProcessingJob_RequestSyntax) **   <a name="sagemaker-CreateProcessingJob-request-Tags"></a>
(Optional) An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the * AWS Billing and Cost Management User Guide*.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request tag variable or plain text fields.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateProcessingJob_ResponseSyntax"></a>

```
{
   "ProcessingJobArn": "string"
}
```

## Response Elements
<a name="API_CreateProcessingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessingJobArn](#API_CreateProcessingJob_ResponseSyntax) **   <a name="sagemaker-CreateProcessingJob-response-ProcessingJobArn"></a>
The Amazon Resource Name (ARN) of the processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateProcessingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateProcessingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateProcessingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateProcessingJob)
