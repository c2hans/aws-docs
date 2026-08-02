---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProcessingJob.html
---

# DescribeProcessingJob
<a name="API_DescribeProcessingJob"></a>

Returns a description of a processing job.

## Request Syntax
<a name="API_DescribeProcessingJob_RequestSyntax"></a>

```
{
   "ProcessingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProcessingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProcessingJobName](#API_DescribeProcessingJob_RequestSyntax) **   <a name="sagemaker-DescribeProcessingJob-request-ProcessingJobName"></a>
The name of the processing job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeProcessingJob_ResponseSyntax"></a>

```
{
   "AppSpecification": {
      "ContainerArguments": [ "string" ],
      "ContainerEntrypoint": [ "string" ],
      "ImageUri": "string"
   },
   "AutoMLJobArn": "string",
   "CreationTime": number,
   "Environment": {
      "string" : "string"
   },
   "ExitMessage": "string",
   "ExperimentConfig": {
      "ExperimentName": "string",
      "RunName": "string",
      "TrialComponentDisplayName": "string",
      "TrialName": "string"
   },
   "FailureReason": "string",
   "LastModifiedTime": number,
   "MonitoringScheduleArn": "string",
   "NetworkConfig": {
      "EnableInterContainerTrafficEncryption": boolean,
      "EnableNetworkIsolation": boolean,
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   },
   "ProcessingEndTime": number,
   "ProcessingInputs": [
      {
         "AppManaged": boolean,
         "DatasetDefinition": {
            "AthenaDatasetDefinition": {
               "Catalog": "string",
               "Database": "string",
               "KmsKeyId": "string",
               "OutputCompression": "string",
               "OutputFormat": "string",
               "OutputS3Uri": "string",
               "QueryString": "string",
               "WorkGroup": "string"
            },
            "DataDistributionType": "string",
            "InputMode": "string",
            "LocalPath": "string",
            "RedshiftDatasetDefinition": {
               "ClusterId": "string",
               "ClusterRoleArn": "string",
               "Database": "string",
               "DbUser": "string",
               "KmsKeyId": "string",
               "OutputCompression": "string",
               "OutputFormat": "string",
               "OutputS3Uri": "string",
               "QueryString": "string"
            }
         },
         "InputName": "string",
         "S3Input": {
            "LocalPath": "string",
            "S3CompressionType": "string",
            "S3DataDistributionType": "string",
            "S3DataType": "string",
            "S3InputMode": "string",
            "S3Uri": "string"
         }
      }
   ],
   "ProcessingJobArn": "string",
   "ProcessingJobName": "string",
   "ProcessingJobStatus": "string",
   "ProcessingOutputConfig": {
      "KmsKeyId": "string",
      "Outputs": [
         {
            "AppManaged": boolean,
            "FeatureStoreOutput": {
               "FeatureGroupName": "string"
            },
            "OutputName": "string",
            "S3Output": {
               "LocalPath": "string",
               "S3UploadMode": "string",
               "S3Uri": "string"
            }
         }
      ]
   },
   "ProcessingResources": {
      "ClusterConfig": {
         "InstanceCount": number,
         "InstanceType": "string",
         "VolumeKmsKeyId": "string",
         "VolumeSizeInGB": number
      }
   },
   "ProcessingStartTime": number,
   "RoleArn": "string",
   "StoppingCondition": {
      "MaxRuntimeInSeconds": number
   },
   "TrainingJobArn": "string"
}
```

## Response Elements
<a name="API_DescribeProcessingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppSpecification](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-AppSpecification"></a>
Configures the processing job to run a specified container image.
Type: [AppSpecification](API_AppSpecification.md) object

 ** [AutoMLJobArn](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-AutoMLJobArn"></a>
The ARN of an AutoML job associated with this processing job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

 ** [CreationTime](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-CreationTime"></a>
The time at which the processing job was created.
Type: Timestamp

 ** [Environment](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-Environment"></a>
The environment variables set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`

 ** [ExitMessage](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ExitMessage"></a>
An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [ExperimentConfig](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ExperimentConfig"></a>
The configuration information used to create an experiment.
Type: [ExperimentConfig](API_ExperimentConfig.md) object

 ** [FailureReason](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-FailureReason"></a>
A string, up to one KB in size, that contains the reason a processing job failed, if it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedTime](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-LastModifiedTime"></a>
The time at which the processing job was last modified.
Type: Timestamp

 ** [MonitoringScheduleArn](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-MonitoringScheduleArn"></a>
The ARN of a monitoring schedule for an endpoint associated with this processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [NetworkConfig](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-NetworkConfig"></a>
Networking options for a processing job.
Type: [NetworkConfig](API_NetworkConfig.md) object

 ** [ProcessingEndTime](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingEndTime"></a>
The time at which the processing job completed.
Type: Timestamp

 ** [ProcessingInputs](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingInputs"></a>
The inputs for a processing job.
Type: Array of [ProcessingInput](API_ProcessingInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [ProcessingJobArn](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingJobArn"></a>
The Amazon Resource Name (ARN) of the processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ProcessingJobName](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingJobName"></a>
The name of the processing job. The name must be unique within an AWS Region in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ProcessingJobStatus](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingJobStatus"></a>
Provides the status of a processing job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`

 ** [ProcessingOutputConfig](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingOutputConfig"></a>
Output configuration for the processing job.
Type: [ProcessingOutputConfig](API_ProcessingOutputConfig.md) object

 ** [ProcessingResources](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingResources"></a>
Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.
Type: [ProcessingResources](API_ProcessingResources.md) object

 ** [ProcessingStartTime](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-ProcessingStartTime"></a>
The time at which the processing job started.
Type: Timestamp

 ** [RoleArn](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-StoppingCondition"></a>
The time limit for how long the processing job is allowed to run.
Type: [ProcessingStoppingCondition](API_ProcessingStoppingCondition.md) object

 ** [TrainingJobArn](#API_DescribeProcessingJob_ResponseSyntax) **   <a name="sagemaker-DescribeProcessingJob-response-TrainingJobArn"></a>
The ARN of a training job associated with this processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_DescribeProcessingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProcessingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeProcessingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeProcessingJob)
