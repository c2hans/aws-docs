---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html
---

# AutoMLAlgorithmConfig
<a name="API_AutoMLAlgorithmConfig"></a>

The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.

## Contents
<a name="API_AutoMLAlgorithmConfig_Contents"></a>

 ** AutoMLAlgorithms **   <a name="sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms"></a>
The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.
+  **For the tabular problem type `TabularJobConfig`:**
**Note**
Selected algorithms must belong to the list corresponding to the training mode set in [AutoMLJobConfig.Mode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-Mode) (`ENSEMBLING` or `HYPERPARAMETER_TUNING`). Choose a minimum of 1 algorithm.
  + In `ENSEMBLING` mode:
    + "catboost"
    + "extra-trees"
    + "fastai"
    + "lightgbm"
    + "linear-learner"
    + "nn-torch"
    + "randomforest"
    + "xgboost"
  + In `HYPERPARAMETER_TUNING` mode:
    + "linear-learner"
    + "mlp"
    + "xgboost"
+  **For the time-series forecasting problem type `TimeSeriesForecastingJobConfig`:**
  + Choose your algorithms from this list.
    + "cnn-qr"
    + "deepar"
    + "prophet"
    + "arima"
    + "npts"
    + "ets"
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `xgboost | linear-learner | mlp | lightgbm | catboost | randomforest | extra-trees | nn-torch | fastai | cnn-qr | deepar | prophet | npts | arima | ets`
Required: Yes

## See Also
<a name="API_AutoMLAlgorithmConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLAlgorithmConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLAlgorithmConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLAlgorithmConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
