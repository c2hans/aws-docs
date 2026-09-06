---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RetryStrategy.html
---

# RetryStrategy
<a name="API_RetryStrategy"></a>

The retry strategy to use when a training job fails due to an `InternalServerError`. `RetryStrategy` is specified as part of the `CreateTrainingJob` and `CreateHyperParameterTuningJob` requests. You can add the `StoppingCondition` parameter to the request to limit the training time for the complete job.

## Contents
<a name="API_RetryStrategy_Contents"></a>

 ** MaximumRetryAttempts **   <a name="sagemaker-Type-RetryStrategy-MaximumRetryAttempts"></a>
The number of times to retry the job. When the job is retried, it's `SecondaryStatus` is changed to `STARTING`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: Yes

## See Also
<a name="API_RetryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RetryStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RetryStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RetryStrategy)
