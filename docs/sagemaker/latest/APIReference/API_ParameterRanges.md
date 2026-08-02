---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html
---

# ParameterRanges
<a name="API_ParameterRanges"></a>

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

**Note**
The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges can't exceed the maximum number specified.

## Contents
<a name="API_ParameterRanges_Contents"></a>

 ** AutoParameters **   <a name="sagemaker-Type-ParameterRanges-AutoParameters"></a>
A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.
Type: Array of [AutoParameter](API_AutoParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** CategoricalParameterRanges **   <a name="sagemaker-Type-ParameterRanges-CategoricalParameterRanges"></a>
The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
Type: Array of [CategoricalParameterRange](API_CategoricalParameterRange.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** ContinuousParameterRanges **   <a name="sagemaker-Type-ParameterRanges-ContinuousParameterRanges"></a>
The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.
Type: Array of [ContinuousParameterRange](API_ContinuousParameterRange.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** IntegerParameterRanges **   <a name="sagemaker-Type-ParameterRanges-IntegerParameterRanges"></a>
The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.
Type: Array of [IntegerParameterRange](API_IntegerParameterRange.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

## See Also
<a name="API_ParameterRanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ParameterRanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ParameterRanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ParameterRanges)
