---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobSummary.html
---

# HyperParameterTrainingJobSummary
<a name="API_HyperParameterTrainingJobSummary"></a>

The container for the summary information about a training job.

## Contents
<a name="API_HyperParameterTrainingJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-CreationTime"></a>
The date and time that the training job was created.
Type: Timestamp
Required: Yes

 ** TrainingJobArn **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingJobName **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingJobName"></a>
The name of the training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingJobStatus **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingJobStatus"></a>
The status of the training job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`
Required: Yes

 ** TunedHyperParameters **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TunedHyperParameters"></a>
A list of the hyperparameters for which you specified ranges to search.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-FailureReason"></a>
The reason that the training job failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FinalHyperParameterTuningJobObjectiveMetric **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-FinalHyperParameterTuningJobObjectiveMetric"></a>
The [FinalHyperParameterTuningJobObjectiveMetric](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalHyperParameterTuningJobObjectiveMetric.html) object that specifies the value of the objective metric of the tuning job that launched this training job.
Type: [FinalHyperParameterTuningJobObjectiveMetric](API_FinalHyperParameterTuningJobObjectiveMetric.md) object
Required: No

 ** ObjectiveStatus **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-ObjectiveStatus"></a>
The status of the objective metric for the training job:
+ Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
+ Pending: The training job is in progress and evaluation of its final objective metric is pending.
+ Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
Type: String
Valid Values: `Succeeded | Pending | Failed`
Required: No

 ** TrainingEndTime **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingEndTime"></a>
Specifies the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.
Type: Timestamp
Required: No

 ** TrainingJobDefinitionName **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingJobDefinitionName"></a>
The training job definition name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: No

 ** TrainingStartTime **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TrainingStartTime"></a>
The date and time that the training job started.
Type: Timestamp
Required: No

 ** TuningJobName **   <a name="sagemaker-Type-HyperParameterTrainingJobSummary-TuningJobName"></a>
The HyperParameter tuning job that launched the training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: No

## See Also
<a name="API_HyperParameterTrainingJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTrainingJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTrainingJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTrainingJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
