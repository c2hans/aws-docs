---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html
---

# DescribeTrainingJob
<a name="API_DescribeTrainingJob"></a>

Returns information about a training job.

Some of the attributes below only appear if the training job successfully starts. If the training job fails, `TrainingJobStatus` is `Failed` and, depending on the `FailureReason`, attributes like `TrainingStartTime`, `TrainingTimeInSeconds`, `TrainingEndTime`, and `BillableTimeInSeconds` may not be present in the response.

## Request Syntax
<a name="API_DescribeTrainingJob_RequestSyntax"></a>

```
{
   "TrainingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrainingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrainingJobName](#API_DescribeTrainingJob_RequestSyntax) **   <a name="sagemaker-DescribeTrainingJob-request-TrainingJobName"></a>
The name of the training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeTrainingJob_ResponseSyntax"></a>

```
{
   "AlgorithmSpecification": {
      "AlgorithmName": "string",
      "ContainerArguments": [ "string" ],
      "ContainerEntrypoint": [ "string" ],
      "EnableSageMakerMetricsTimeSeries": boolean,
      "MetricDefinitions": [
         {
            "Name": "string",
            "Regex": "string"
         }
      ],
      "TrainingImage": "string",
      "TrainingImageConfig": {
         "TrainingRepositoryAccessMode": "string",
         "TrainingRepositoryAuthConfig": {
            "TrainingRepositoryCredentialsProviderArn": "string"
         }
      },
      "TrainingInputMode": "string"
   },
   "AutoMLJobArn": "string",
   "BillableTimeInSeconds": number,
   "BillableTokenCount": number,
   "CheckpointConfig": {
      "LocalPath": "string",
      "S3Uri": "string"
   },
   "DebugHookConfig": {
      "CollectionConfigurations": [
         {
            "CollectionName": "string",
            "CollectionParameters": {
               "string" : "string"
            }
         }
      ],
      "HookParameters": {
         "string" : "string"
      },
      "LocalPath": "string",
      "S3OutputPath": "string"
   },
   "DebugRuleConfigurations": [
      {
         "InstanceType": "string",
         "LocalPath": "string",
         "RuleConfigurationName": "string",
         "RuleEvaluatorImage": "string",
         "RuleParameters": {
            "string" : "string"
         },
         "S3OutputPath": "string",
         "VolumeSizeInGB": number
      }
   ],
   "DebugRuleEvaluationStatuses": [
      {
         "RuleConfigurationName": "string",
         "RuleEvaluationJobArn": "string",
         "RuleEvaluationStatus": "string",
         "StatusDetails": "string"
      }
   ],
   "EnableInterContainerTrafficEncryption": boolean,
   "EnableManagedSpotTraining": boolean,
   "EnableNetworkIsolation": boolean,
   "Environment": {
      "string" : "string"
   },
   "ExperimentConfig": {
      "ExperimentName": "string",
      "RunName": "string",
      "TrialComponentDisplayName": "string",
      "TrialName": "string"
   },
   "FailureReason": "string",
   "FinalMetricDataList": [
      {
         "MetricName": "string",
         "Value": number
      }
   ],
   "HyperParameters": {
      "string" : "string"
   },
   "InfraCheckConfig": {
      "EnableInfraCheck": boolean
   },
   "InputDataConfig": [
      {
         "ChannelName": "string",
         "CompressionType": "string",
         "ContentType": "string",
         "DataSource": {
            "DatasetSource": {
               "DatasetArn": "string"
            },
            "FileSystemDataSource": {
               "DirectoryPath": "string",
               "FileSystemAccessMode": "string",
               "FileSystemId": "string",
               "FileSystemType": "string"
            },
            "S3DataSource": {
               "AttributeNames": [ "string" ],
               "HubAccessConfig": {
                  "HubContentArn": "string"
               },
               "InstanceGroupNames": [ "string" ],
               "ModelAccessConfig": {
                  "AcceptEula": boolean
               },
               "S3DataDistributionType": "string",
               "S3DataType": "string",
               "S3Uri": "string"
            }
         },
         "InputMode": "string",
         "RecordWrapperType": "string",
         "ShuffleConfig": {
            "Seed": number
         }
      }
   ],
   "LabelingJobArn": "string",
   "MlflowConfig": {
      "MlflowExperimentName": "string",
      "MlflowResourceArn": "string",
      "MlflowRunName": "string"
   },
   "MlflowDetails": {
      "MlflowExperimentId": "string",
      "MlflowRunId": "string"
   },
   "ModelArtifacts": {
      "S3ModelArtifacts": "string"
   },
   "ModelPackageConfig": {
      "ModelPackageGroupArn": "string",
      "SourceModelPackageArn": "string"
   },
   "OutputDataConfig": {
      "CompressionType": "string",
      "KmsKeyId": "string",
      "S3OutputPath": "string"
   },
   "OutputModelPackageArn": "string",
   "ProfilerConfig": {
      "DisableProfiler": boolean,
      "ProfilingIntervalInMilliseconds": number,
      "ProfilingParameters": {
         "string" : "string"
      },
      "S3OutputPath": "string"
   },
   "ProfilerRuleConfigurations": [
      {
         "InstanceType": "string",
         "LocalPath": "string",
         "RuleConfigurationName": "string",
         "RuleEvaluatorImage": "string",
         "RuleParameters": {
            "string" : "string"
         },
         "S3OutputPath": "string",
         "VolumeSizeInGB": number
      }
   ],
   "ProfilerRuleEvaluationStatuses": [
      {
         "RuleConfigurationName": "string",
         "RuleEvaluationJobArn": "string",
         "RuleEvaluationStatus": "string",
         "StatusDetails": "string"
      }
   ],
   "ProfilingStatus": "string",
   "ProgressInfo": {
      "CurrentEpoch": number,
      "CurrentStep": number,
      "MaxEpoch": number,
      "TotalStepCountPerEpoch": number
   },
   "RemoteDebugConfig": {
      "EnableRemoteDebug": boolean
   },
   "ResourceConfig": {
      "InstanceCount": number,
      "InstanceGroups": [
         {
            "InstanceCount": number,
            "InstanceGroupName": "string",
            "InstanceType": "string"
         }
      ],
      "InstancePlacementConfig": {
         "EnableMultipleJobs": boolean,
         "PlacementSpecifications": [
            {
               "InstanceCount": number,
               "UltraServerId": "string"
            }
         ]
      },
      "InstancePreferences": [
         {
            "InstanceCount": number,
            "InstanceType": "string",
            "TrainingPlanArns": [ "string" ]
         }
      ],
      "InstanceType": "string",
      "KeepAlivePeriodInSeconds": number,
      "SelectedInstanceCount": number,
      "SelectedInstanceType": "string",
      "TrainingPlanArn": "string",
      "VolumeKmsKeyId": "string",
      "VolumeSizeInGB": number
   },
   "RetryStrategy": {
      "MaximumRetryAttempts": number
   },
   "RoleArn": "string",
   "SecondaryStatus": "string",
   "SecondaryStatusTransitions": [
      {
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "ServerlessJobConfig": {
      "AcceptEula": boolean,
      "BaseModelArn": "string",
      "CustomizationTechnique": "string",
      "EvaluationType": "string",
      "EvaluatorArn": "string",
      "JobType": "string",
      "Peft": "string",
      "SequenceLength": "string"
   },
   "StoppingCondition": {
      "MaxPendingTimeInSeconds": number,
      "MaxRuntimeInSeconds": number,
      "MaxWaitTimeInSeconds": number
   },
   "TensorBoardOutputConfig": {
      "LocalPath": "string",
      "S3OutputPath": "string"
   },
   "TrainingJobArn": "string",
   "TrainingJobName": "string",
   "TrainingJobStatus": "string",
   "TrainingTimeInSeconds": number,
   "TuningJobArn": "string",
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   },
   "WarmPoolStatus": {
      "ResourceRetainedBillableTimeInSeconds": number,
      "ReusedByJob": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTrainingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlgorithmSpecification](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-AlgorithmSpecification"></a>
Information about the algorithm used for training, and algorithm metadata.
Type: [AlgorithmSpecification](API_AlgorithmSpecification.md) object

 ** [AutoMLJobArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-AutoMLJobArn"></a>
The Amazon Resource Name (ARN) of an AutoML job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

 ** [BillableTimeInSeconds](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-BillableTimeInSeconds"></a>
The billable time in seconds. Billable time refers to the absolute wall-clock time.
Multiply `BillableTimeInSeconds` by the number of instances (`InstanceCount`) in your training cluster to get the total compute time SageMaker bills you if you run distributed training. The formula is as follows: `BillableTimeInSeconds * InstanceCount` .
You can calculate the savings from using managed spot training using the formula `(1 - BillableTimeInSeconds / TrainingTimeInSeconds) * 100`. For example, if `BillableTimeInSeconds` is 100 and `TrainingTimeInSeconds` is 500, the savings is 80%.
Type: Integer
Valid Range: Minimum value of 1.

 ** [BillableTokenCount](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-BillableTokenCount"></a>
 The billable token count for eligible serverless training jobs.
Type: Long
Valid Range: Minimum value of 0.

 ** [CheckpointConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-CheckpointConfig"></a>
Contains information about the output location for managed spot training checkpoint data.
Type: [CheckpointConfig](API_CheckpointConfig.md) object

 ** [DebugHookConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-DebugHookConfig"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
Type: [DebugHookConfig](API_DebugHookConfig.md) object

 ** [DebugRuleConfigurations](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-DebugRuleConfigurations"></a>
Configuration information for Amazon SageMaker Debugger rules for debugging output tensors.
Type: Array of [DebugRuleConfiguration](API_DebugRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [DebugRuleEvaluationStatuses](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-DebugRuleEvaluationStatuses"></a>
Evaluation status of Amazon SageMaker Debugger rules for debugging on a training job.
Type: Array of [DebugRuleEvaluationStatus](API_DebugRuleEvaluationStatus.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [EnableInterContainerTrafficEncryption](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-EnableInterContainerTrafficEncryption"></a>
To encrypt all communications between ML compute instances in distributed training, choose `True`. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithms in distributed training.
Type: Boolean

 ** [EnableManagedSpotTraining](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-EnableManagedSpotTraining"></a>
A Boolean indicating whether managed spot training is enabled (`True`) or not (`False`).
Type: Boolean

 ** [EnableNetworkIsolation](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-EnableNetworkIsolation"></a>
If you want to allow inbound or outbound network calls, except for calls between peers within a training cluster for distributed training, choose `True`. If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
Type: Boolean

 ** [Environment](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-Environment"></a>
The environment variables to set in the Docker container.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `[\S\s]*`

 ** [ExperimentConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object

 ** [FailureReason](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-FailureReason"></a>
If the training job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [FinalMetricDataList](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-FinalMetricDataList"></a>
A collection of `MetricData` objects that specify the names, values, and dates and times that the training algorithm emitted to Amazon CloudWatch.
Type: Array of [MetricData](API_MetricData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.

 ** [HyperParameters](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-HyperParameters"></a>
Algorithm-specific parameters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`

 ** [InfraCheckConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-InfraCheckConfig"></a>
Contains information about the infrastructure health check configuration for the training job.
Type: [InfraCheckConfig](API_InfraCheckConfig.md) object

 ** [InputDataConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-InputDataConfig"></a>
An array of `Channel` objects that describes each data input channel.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [LabelingJobArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Ground Truth labeling job that created the transform or training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`

 ** [MlflowConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-MlflowConfig"></a>
 The MLflow configuration using SageMaker managed MLflow.
Type: [MlflowConfig](API_MlflowConfig.md) object

 ** [MlflowDetails](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-MlflowDetails"></a>
 The MLflow details of this job.
Type: [MlflowDetails](API_MlflowDetails.md) object

 ** [ModelArtifacts](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ModelArtifacts"></a>
Information about the Amazon S3 location that is configured for storing model artifacts.
Type: [ModelArtifacts](API_ModelArtifacts.md) object

 ** [ModelPackageConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ModelPackageConfig"></a>
 The configuration for the model package.
Type: [ModelPackageConfig](API_ModelPackageConfig.md) object

 ** [OutputDataConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-OutputDataConfig"></a>
The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.
Type: [OutputDataConfig](API_OutputDataConfig.md) object

 ** [OutputModelPackageArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-OutputModelPackageArn"></a>
 The Amazon Resource Name (ARN) of the output model package containing model weights or checkpoints.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

 ** [ProfilerConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ProfilerConfig"></a>
Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.
Type: [ProfilerConfig](API_ProfilerConfig.md) object

 ** [ProfilerRuleConfigurations](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ProfilerRuleConfigurations"></a>
Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.
Type: Array of [ProfilerRuleConfiguration](API_ProfilerRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [ProfilerRuleEvaluationStatuses](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ProfilerRuleEvaluationStatuses"></a>
Evaluation status of Amazon SageMaker Debugger rules for profiling on a training job.
Type: Array of [ProfilerRuleEvaluationStatus](API_ProfilerRuleEvaluationStatus.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [ProfilingStatus](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ProfilingStatus"></a>
Profiling status of a training job.
Type: String
Valid Values: `Enabled | Disabled`

 ** [ProgressInfo](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ProgressInfo"></a>
 The Serverless training job progress information.
Type: [TrainingProgressInfo](API_TrainingProgressInfo.md) object

 ** [RemoteDebugConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-RemoteDebugConfig"></a>
Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through AWS Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html).
Type: [RemoteDebugConfig](API_RemoteDebugConfig.md) object

 ** [ResourceConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ResourceConfig"></a>
Resources, including ML compute instances and ML storage volumes, that are configured for model training.
Type: [ResourceConfig](API_ResourceConfig.md) object

 ** [RetryStrategy](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-RetryStrategy"></a>
The number of times to retry the job when the job fails due to an `InternalServerError`.
Type: [RetryStrategy](API_RetryStrategy.md) object

 ** [RoleArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-RoleArn"></a>
The AWS Identity and Access Management (IAM) role configured for the training job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [SecondaryStatus](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-SecondaryStatus"></a>
 Provides detailed information about the state of the training job. For detailed information on the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html).
SageMaker provides primary statuses and secondary statuses that apply to each of them:
InProgress
+  `Starting` - Starting the training job.
+  `Pending` - The training job is waiting for compute capacity or compute resource provision.
+  `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
+  `Training` - Training is in progress.
+  `Interrupted` - The job stopped because the managed spot training instances were interrupted.
+  `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.
Completed
+  `Completed` - The training job has completed.
Failed
+  `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse`.
Stopped
+  `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
+  `MaxWaitTimeExceeded` - The job stopped because it exceeded the maximum allowed wait time.
+  `Stopped` - The training job has stopped.
Stopping
+  `Stopping` - Stopping the training job.
Valid values for `SecondaryStatus` are subject to change.
We no longer support the following secondary statuses:
+  `LaunchingMLInstances`
+  `PreparingTraining`
+  `DownloadingTrainingImage`
Type: String
Valid Values: `Starting | LaunchingMLInstances | PreparingTrainingStack | Downloading | DownloadingTrainingImage | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Completed | Failed | Interrupted | MaxWaitTimeExceeded | Updating | Restarting | Pending`

 ** [SecondaryStatusTransitions](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-SecondaryStatusTransitions"></a>
A history of all of the secondary statuses that the training job has transitioned through.
Type: Array of [SecondaryStatusTransition](API_SecondaryStatusTransition.md) objects

 ** [ServerlessJobConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-ServerlessJobConfig"></a>
 The configuration for serverless training jobs.
Type: [ServerlessJobConfig](API_ServerlessJobConfig.md) object

 ** [StoppingCondition](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-StoppingCondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
Type: [StoppingCondition](API_StoppingCondition.md) object

 ** [TensorBoardOutputConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TensorBoardOutputConfig"></a>
Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.
Type: [TensorBoardOutputConfig](API_TensorBoardOutputConfig.md) object

 ** [TrainingJobArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [TrainingJobName](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TrainingJobName"></a>
 Name of the model training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [TrainingJobStatus](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TrainingJobStatus"></a>
The status of the training job.
SageMaker provides the following training job statuses:
+  `InProgress` - The training is in progress.
+  `Completed` - The training job has completed.
+  `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
+  `Stopping` - The training job is stopping.
+  `Stopped` - The training job has stopped.
For more detailed information, see `SecondaryStatus`.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`

 ** [TrainingTimeInSeconds](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TrainingTimeInSeconds"></a>
The training time in seconds.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TuningJobArn](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-TuningJobArn"></a>
The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`

 ** [VpcConfig](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object

 ** [WarmPoolStatus](#API_DescribeTrainingJob_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingJob-response-WarmPoolStatus"></a>
The status of the warm pool associated with the training job.
Type: [WarmPoolStatus](API_WarmPoolStatus.md) object

## Errors
<a name="API_DescribeTrainingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrainingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrainingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrainingJob)
