---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html
---

# TrainingJobSummary
<a name="API_TrainingJobSummary"></a>

Provides summary information about a training job.

## Contents
<a name="API_TrainingJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TrainingJobSummary-CreationTime"></a>
A timestamp that shows when the training job was created.
Type: Timestamp
Required: Yes

 ** TrainingJobArn **   <a name="sagemaker-Type-TrainingJobSummary-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingJobName **   <a name="sagemaker-Type-TrainingJobSummary-TrainingJobName"></a>
The name of the training job that you want a summary for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingJobStatus **   <a name="sagemaker-Type-TrainingJobSummary-TrainingJobStatus"></a>
The status of the training job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-TrainingJobSummary-LastModifiedTime"></a>
 Timestamp when the training job was last modified.
Type: Timestamp
Required: No

 ** SecondaryStatus **   <a name="sagemaker-Type-TrainingJobSummary-SecondaryStatus"></a>
The secondary status of the training job.
Type: String
Valid Values: `Starting | LaunchingMLInstances | PreparingTrainingStack | Downloading | DownloadingTrainingImage | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Completed | Failed | Interrupted | MaxWaitTimeExceeded | Updating | Restarting | Pending`
Required: No

 ** TrainingEndTime **   <a name="sagemaker-Type-TrainingJobSummary-TrainingEndTime"></a>
A timestamp that shows when the training job ended. This field is set only if the training job has one of the terminal statuses (`Completed`, `Failed`, or `Stopped`).
Type: Timestamp
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-TrainingJobSummary-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan associated with this training job.
For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** WarmPoolStatus **   <a name="sagemaker-Type-TrainingJobSummary-WarmPoolStatus"></a>
The status of the warm pool associated with the training job.
Type: [WarmPoolStatus](API_WarmPoolStatus.md) object
Required: No

## See Also
<a name="API_TrainingJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingJobSummary)
