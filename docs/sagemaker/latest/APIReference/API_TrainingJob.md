---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJob.html
---

# TrainingJob
<a name="API_TrainingJob"></a>

Contains information about a training job.

## Contents
<a name="API_TrainingJob_Contents"></a>

 ** AlgorithmSpecification **   <a name="sagemaker-Type-TrainingJob-AlgorithmSpecification"></a>
Information about the algorithm used for training, and algorithm metadata.
Type: [AlgorithmSpecification](API_AlgorithmSpecification.md) object
Required: No

 ** AutoMLJobArn **   <a name="sagemaker-Type-TrainingJob-AutoMLJobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`
Required: No

 ** BillableTimeInSeconds **   <a name="sagemaker-Type-TrainingJob-BillableTimeInSeconds"></a>
The billable time in seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** CheckpointConfig **   <a name="sagemaker-Type-TrainingJob-CheckpointConfig"></a>
Contains information about the output location for managed spot training checkpoint data.
Type: [CheckpointConfig](API_CheckpointConfig.md) object
Required: No

 ** DebugHookConfig **   <a name="sagemaker-Type-TrainingJob-DebugHookConfig"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
Type: [DebugHookConfig](API_DebugHookConfig.md) object
Required: No

 ** DebugRuleConfigurations **   <a name="sagemaker-Type-TrainingJob-DebugRuleConfigurations"></a>
Information about the debug rule configuration.
Type: Array of [DebugRuleConfiguration](API_DebugRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** DebugRuleEvaluationStatuses **   <a name="sagemaker-Type-TrainingJob-DebugRuleEvaluationStatuses"></a>
Information about the evaluation status of the rules for the training job.
Type: Array of [DebugRuleEvaluationStatus](API_DebugRuleEvaluationStatus.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** EnableInterContainerTrafficEncryption **   <a name="sagemaker-Type-TrainingJob-EnableInterContainerTrafficEncryption"></a>
To encrypt all communications between ML compute instances in distributed training, choose `True`. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
Type: Boolean
Required: No

 ** EnableManagedSpotTraining **   <a name="sagemaker-Type-TrainingJob-EnableManagedSpotTraining"></a>
When true, enables managed spot training using Amazon EC2 Spot instances to run training jobs instead of on-demand instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html).
Type: Boolean
Required: No

 ** EnableNetworkIsolation **   <a name="sagemaker-Type-TrainingJob-EnableNetworkIsolation"></a>
If the `TrainingJob` was created with network isolation, the value is set to `true`. If network isolation is enabled, nodes can't communicate beyond the VPC they run in.
Type: Boolean
Required: No

 ** Environment **   <a name="sagemaker-Type-TrainingJob-Environment"></a>
The environment variables to set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `[\S\s]*`
Required: No

 ** ExperimentConfig **   <a name="sagemaker-Type-TrainingJob-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-TrainingJob-FailureReason"></a>
If the training job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FinalMetricDataList **   <a name="sagemaker-Type-TrainingJob-FinalMetricDataList"></a>
A list of final metric values that are set when the training job completes. Used only if the training job was configured to use metrics.
Type: Array of [MetricData](API_MetricData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** HyperParameters **   <a name="sagemaker-Type-TrainingJob-HyperParameters"></a>
Algorithm-specific parameters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** InputDataConfig **   <a name="sagemaker-Type-TrainingJob-InputDataConfig"></a>
An array of `Channel` objects that describes each data input channel.
Your input must be in the same AWS region as your training job.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** LabelingJobArn **   <a name="sagemaker-Type-TrainingJob-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the labeling job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`
Required: No

 ** ModelArtifacts **   <a name="sagemaker-Type-TrainingJob-ModelArtifacts"></a>
Information about the Amazon S3 location that is configured for storing model artifacts.
Type: [ModelArtifacts](API_ModelArtifacts.md) object
Required: No

 ** ModelPackageConfig **   <a name="sagemaker-Type-TrainingJob-ModelPackageConfig"></a>
 The model package configuration.
Type: [ModelPackageConfig](API_ModelPackageConfig.md) object
Required: No

 ** OutputDataConfig **   <a name="sagemaker-Type-TrainingJob-OutputDataConfig"></a>
The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: No

 ** OutputModelPackageArn **   <a name="sagemaker-Type-TrainingJob-OutputModelPackageArn"></a>
 The output model package Amazon Resource Name (ARN) that contains model weights or checkpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** ProfilerConfig **   <a name="sagemaker-Type-TrainingJob-ProfilerConfig"></a>
Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.
Type: [ProfilerConfig](API_ProfilerConfig.md) object
Required: No

 ** ResourceConfig **   <a name="sagemaker-Type-TrainingJob-ResourceConfig"></a>
Resources, including ML compute instances and ML storage volumes, that are configured for model training.
Type: [ResourceConfig](API_ResourceConfig.md) object
Required: No

 ** RetryStrategy **   <a name="sagemaker-Type-TrainingJob-RetryStrategy"></a>
The number of times to retry the job when the job fails due to an `InternalServerError`.
Type: [RetryStrategy](API_RetryStrategy.md) object
Required: No

 ** RoleArn **   <a name="sagemaker-Type-TrainingJob-RoleArn"></a>
The AWS Identity and Access Management (IAM) role configured for the training job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** SecondaryStatus **   <a name="sagemaker-Type-TrainingJob-SecondaryStatus"></a>
 Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html).
SageMaker provides primary statuses and secondary statuses that apply to each of them:
InProgress
+  `Starting` - Starting the training job.
+  `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
+  `Training` - Training is in progress.
+  `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.
Completed
+  `Completed` - The training job has completed.
Failed
+  `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse`.
Stopped
+  `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
+  `Stopped` - The training job has stopped.
Stopping
+  `Stopping` - Stopping the training job.
Valid values for `SecondaryStatus` are subject to change.
We no longer support the following secondary statuses:
+  `LaunchingMLInstances`
+  `PreparingTrainingStack`
+  `DownloadingTrainingImage`
Type: String
Valid Values: `Starting | LaunchingMLInstances | PreparingTrainingStack | Downloading | DownloadingTrainingImage | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Completed | Failed | Interrupted | MaxWaitTimeExceeded | Updating | Restarting | Pending`
Required: No

 ** SecondaryStatusTransitions **   <a name="sagemaker-Type-TrainingJob-SecondaryStatusTransitions"></a>
A history of all of the secondary statuses that the training job has transitioned through.
Type: Array of [SecondaryStatusTransition](API_SecondaryStatusTransition.md) objects
Required: No

 ** StoppingCondition **   <a name="sagemaker-Type-TrainingJob-StoppingCondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-TrainingJob-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TensorBoardOutputConfig **   <a name="sagemaker-Type-TrainingJob-TensorBoardOutputConfig"></a>
Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.
Type: [TensorBoardOutputConfig](API_TensorBoardOutputConfig.md) object
Required: No

 ** TrainingJobArn **   <a name="sagemaker-Type-TrainingJob-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** TrainingJobName **   <a name="sagemaker-Type-TrainingJob-TrainingJobName"></a>
The name of the training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** TrainingJobStatus **   <a name="sagemaker-Type-TrainingJob-TrainingJobStatus"></a>
The status of the training job.
Training job statuses are:
+  `InProgress` - The training is in progress.
+  `Completed` - The training job has completed.
+  `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
+  `Stopping` - The training job is stopping.
+  `Stopped` - The training job has stopped.
For more detailed information, see `SecondaryStatus`.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`
Required: No

 ** TrainingTimeInSeconds **   <a name="sagemaker-Type-TrainingJob-TrainingTimeInSeconds"></a>
The training time in seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TuningJobArn **   <a name="sagemaker-Type-TrainingJob-TuningJobArn"></a>
The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-TrainingJob-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** WarmPoolStatus **   <a name="sagemaker-Type-TrainingJob-WarmPoolStatus"></a>
The status of the warm pool associated with the training job.
Type: [WarmPoolStatus](API_WarmPoolStatus.md) object
Required: No

## See Also
<a name="API_TrainingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingJob)
