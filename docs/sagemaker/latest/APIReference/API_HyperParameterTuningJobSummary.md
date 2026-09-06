---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html
---

# HyperParameterTuningJobSummary
<a name="API_HyperParameterTuningJobSummary"></a>

Provides summary information about a hyperparameter tuning job.

## Contents
<a name="API_HyperParameterTuningJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-CreationTime"></a>
The date and time that the tuning job was created.
Type: Timestamp
Required: Yes

 ** HyperParameterTuningJobArn **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-HyperParameterTuningJobArn"></a>
The Amazon Resource Name (ARN) of the tuning job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:hyper-parameter-tuning-job/.*`
Required: Yes

 ** HyperParameterTuningJobName **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-HyperParameterTuningJobName"></a>
The name of the tuning job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** HyperParameterTuningJobStatus **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-HyperParameterTuningJobStatus"></a>
The status of the tuning job.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping | Deleting | DeleteFailed`
Required: Yes

 ** ObjectiveStatusCounters **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-ObjectiveStatusCounters"></a>
The [ObjectiveStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html) object that specifies the numbers of training jobs, categorized by objective metric status, that this tuning job launched.
Type: [ObjectiveStatusCounters](API_ObjectiveStatusCounters.md) object
Required: Yes

 ** Strategy **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-Strategy"></a>
Specifies the search strategy hyperparameter tuning uses to choose which hyperparameters to evaluate at each iteration.
Type: String
Valid Values: `Bayesian | Random | Hyperband | Grid`
Required: Yes

 ** TrainingJobStatusCounters **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-TrainingJobStatusCounters"></a>
The [TrainingJobStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html) object that specifies the numbers of training jobs, categorized by status, that this tuning job launched.
Type: [TrainingJobStatusCounters](API_TrainingJobStatusCounters.md) object
Required: Yes

 ** HyperParameterTuningEndTime **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-HyperParameterTuningEndTime"></a>
The date and time that the tuning job ended.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-LastModifiedTime"></a>
The date and time that the tuning job was modified.
Type: Timestamp
Required: No

 ** ResourceLimits **   <a name="sagemaker-Type-HyperParameterTuningJobSummary-ResourceLimits"></a>
The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training jobs and parallel training jobs allowed for this tuning job.
Type: [ResourceLimits](API_ResourceLimits.md) object
Required: No

## See Also
<a name="API_HyperParameterTuningJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobSummary)
