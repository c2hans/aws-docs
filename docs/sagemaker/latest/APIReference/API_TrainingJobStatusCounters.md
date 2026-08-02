---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html
---

# TrainingJobStatusCounters
<a name="API_TrainingJobStatusCounters"></a>

The numbers of training jobs launched by a hyperparameter tuning job, categorized by status.

## Contents
<a name="API_TrainingJobStatusCounters_Contents"></a>

 ** Completed **   <a name="sagemaker-Type-TrainingJobStatusCounters-Completed"></a>
The number of completed training jobs launched by the hyperparameter tuning job.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InProgress **   <a name="sagemaker-Type-TrainingJobStatusCounters-InProgress"></a>
The number of in-progress training jobs launched by a hyperparameter tuning job.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NonRetryableError **   <a name="sagemaker-Type-TrainingJobStatusCounters-NonRetryableError"></a>
The number of training jobs that failed and can't be retried. A failed training job can't be retried if it failed because a client error occurred.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** RetryableError **   <a name="sagemaker-Type-TrainingJobStatusCounters-RetryableError"></a>
The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Stopped **   <a name="sagemaker-Type-TrainingJobStatusCounters-Stopped"></a>
The number of training jobs launched by a hyperparameter tuning job that were manually stopped.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TrainingJobStatusCounters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingJobStatusCounters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingJobStatusCounters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingJobStatusCounters)
