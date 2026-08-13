---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automlalgorithmconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLAlgorithmConfig
<a name="aws-properties-sagemaker-automljob-automlalgorithmconfig"></a>

The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.

## Syntax
<a name="aws-properties-sagemaker-automljob-automlalgorithmconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automlalgorithmconfig-syntax.json"></a>

```
{
  "[AutoMLAlgorithms](#cfn-sagemaker-automljob-automlalgorithmconfig-automlalgorithms)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automlalgorithmconfig-syntax.yaml"></a>

```
  [AutoMLAlgorithms](#cfn-sagemaker-automljob-automlalgorithmconfig-automlalgorithms): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automlalgorithmconfig-properties"></a>

`AutoMLAlgorithms`  <a name="cfn-sagemaker-automljob-automlalgorithmconfig-automlalgorithms"></a>
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
*Required*: Yes
*Type*: Array of String
*Allowed values*: `xgboost | linear-learner | mlp | lightgbm | catboost | randomforest | extra-trees | nn-torch | fastai | cnn-qr | deepar | prophet | npts | arima | ets`
*Maximum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
