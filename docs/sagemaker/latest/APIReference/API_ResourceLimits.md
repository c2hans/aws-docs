---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html
---

# ResourceLimits
<a name="API_ResourceLimits"></a>

Specifies the maximum number of training jobs and parallel training jobs that a hyperparameter tuning job can launch.

## Contents
<a name="API_ResourceLimits_Contents"></a>

 ** MaxParallelTrainingJobs **   <a name="sagemaker-Type-ResourceLimits-MaxParallelTrainingJobs"></a>
The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** MaxNumberOfTrainingJobs **   <a name="sagemaker-Type-ResourceLimits-MaxNumberOfTrainingJobs"></a>
The maximum number of training jobs that a hyperparameter tuning job can launch.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MaxRuntimeInSeconds **   <a name="sagemaker-Type-ResourceLimits-MaxRuntimeInSeconds"></a>
The maximum time in seconds that a hyperparameter tuning job can run.
Type: Integer
Valid Range: Minimum value of 120. Maximum value of 15768000.
Required: No

## See Also
<a name="API_ResourceLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResourceLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResourceLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResourceLimits)
