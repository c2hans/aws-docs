---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html
---

# CandidateGenerationConfig
<a name="API_CandidateGenerationConfig"></a>

Stores the configuration information for how model candidates are generated using an AutoML job V2.

## Contents
<a name="API_CandidateGenerationConfig_Contents"></a>

 ** AlgorithmsConfig **   <a name="sagemaker-Type-CandidateGenerationConfig-AlgorithmsConfig"></a>
Your Autopilot job trains a default set of algorithms on your dataset. For tabular and time-series data, you can customize the algorithm list by selecting a subset of algorithms for your problem type.
 `AlgorithmsConfig` stores the customized selection of algorithms to train on your data.
+  **For the tabular problem type `TabularJobConfig`,** the list of available algorithms to choose from depends on the training mode set in [`AutoMLJobConfig.Mode`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html).
  +  `AlgorithmsConfig` should not be set when the training mode `AutoMLJobConfig.Mode` is set to `AUTO`.
  + When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only.

    If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
  + When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.

  For the list of all algorithms per training mode, see [ AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html).

  For more information on each algorithm, see the [Algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) section in the Autopilot developer guide.
+  **For the time-series forecasting problem type `TimeSeriesForecastingJobConfig`,** choose your algorithms from the list provided in [ AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html).

  For more information on each algorithm, see the [Algorithms support for time-series forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-algorithms.html) section in the Autopilot developer guide.
  + When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only.

    If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.
  + When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.
Type: Array of [AutoMLAlgorithmConfig](API_AutoMLAlgorithmConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_CandidateGenerationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CandidateGenerationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CandidateGenerationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CandidateGenerationConfig)
