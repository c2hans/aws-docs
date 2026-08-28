---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSearchEntity.html
---

# HyperParameterTuningJobSearchEntity
<a name="API_HyperParameterTuningJobSearchEntity"></a>

An entity returned by the [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html) API containing the properties of a hyperparameter tuning job.

## Contents
<a name="API_HyperParameterTuningJobSearchEntity_Contents"></a>

 ** BestTrainingJob **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-BestTrainingJob"></a>
The container for the summary information about a training job.
Type: [HyperParameterTrainingJobSummary](API_HyperParameterTrainingJobSummary.md) object
Required: No

 ** ConsumedResources **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-ConsumedResources"></a>
The total amount of resources consumed by a hyperparameter tuning job.
Type: [HyperParameterTuningJobConsumedResources](API_HyperParameterTuningJobConsumedResources.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-CreationTime"></a>
The time that a hyperparameter tuning job was created.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-FailureReason"></a>
The error that was created when a hyperparameter tuning job failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** HyperParameterTuningEndTime **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-HyperParameterTuningEndTime"></a>
The time that a hyperparameter tuning job ended.
Type: Timestamp
Required: No

 ** HyperParameterTuningJobArn **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-HyperParameterTuningJobArn"></a>
The Amazon Resource Name (ARN) of a hyperparameter tuning job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`
Required: No

 ** HyperParameterTuningJobConfig **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-HyperParameterTuningJobConfig"></a>
Configures a hyperparameter tuning job.
Type: [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md) object
Required: No

 ** HyperParameterTuningJobName **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-HyperParameterTuningJobName"></a>
The name of a hyperparameter tuning job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: No

 ** HyperParameterTuningJobStatus **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-HyperParameterTuningJobStatus"></a>
The status of a hyperparameter tuning job.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping | Deleting | DeleteFailed`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-LastModifiedTime"></a>
The time that a hyperparameter tuning job was last modified.
Type: Timestamp
Required: No

 ** ObjectiveStatusCounters **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-ObjectiveStatusCounters"></a>
Specifies the number of training jobs that this hyperparameter tuning job launched, categorized by the status of their objective metric. The objective metric status shows whether the final objective metric for the training job has been evaluated by the tuning job and used in the hyperparameter tuning process.
Type: [ObjectiveStatusCounters](API_ObjectiveStatusCounters.md) object
Required: No

 ** OverallBestTrainingJob **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-OverallBestTrainingJob"></a>
The container for the summary information about a training job.
Type: [HyperParameterTrainingJobSummary](API_HyperParameterTrainingJobSummary.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-Tags"></a>
The tags associated with a hyperparameter tuning job. For more information see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TrainingJobDefinition **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-TrainingJobDefinition"></a>
Defines the training jobs launched by a hyperparameter tuning job.
Type: [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) object
Required: No

 ** TrainingJobDefinitions **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-TrainingJobDefinitions"></a>
The job definitions included in a hyperparameter tuning job.
Type: Array of [HyperParameterTrainingJobDefinition](API_HyperParameterTrainingJobDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** TrainingJobStatusCounters **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-TrainingJobStatusCounters"></a>
The numbers of training jobs launched by a hyperparameter tuning job, categorized by status.
Type: [TrainingJobStatusCounters](API_TrainingJobStatusCounters.md) object
Required: No

 ** TuningJobCompletionDetails **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-TuningJobCompletionDetails"></a>
Information about either a current or completed hyperparameter tuning job.
Type: [HyperParameterTuningJobCompletionDetails](API_HyperParameterTuningJobCompletionDetails.md) object
Required: No

 ** WarmStartConfig **   <a name="sagemaker-Type-HyperParameterTuningJobSearchEntity-WarmStartConfig"></a>
Specifies the configuration for a hyperparameter tuning job that uses one or more previous hyperparameter tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric, and the training job that performs the best is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.
All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.
Type: [HyperParameterTuningJobWarmStartConfig](API_HyperParameterTuningJobWarmStartConfig.md) object
Required: No

## See Also
<a name="API_HyperParameterTuningJobSearchEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobSearchEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobSearchEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobSearchEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
