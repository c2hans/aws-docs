---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-parameterranges.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob ParameterRanges
<a name="aws-properties-sagemaker-hyperparametertuningjob-parameterranges"></a>

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

**Note**
The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges can't exceed the maximum number specified.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-parameterranges-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-parameterranges-syntax.json"></a>

```
{
  "[AutoParameters](#cfn-sagemaker-hyperparametertuningjob-parameterranges-autoparameters)" : {{[ AutoParametersItems, ... ]}},
  "[CategoricalParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-categoricalparameterranges)" : {{[ CategoricalParameterRangesItems, ... ]}},
  "[ContinuousParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-continuousparameterranges)" : {{[ ContinuousParameterRangesItems, ... ]}},
  "[IntegerParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-integerparameterranges)" : {{[ IntegerParameterRangesItems, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-parameterranges-syntax.yaml"></a>

```
  [AutoParameters](#cfn-sagemaker-hyperparametertuningjob-parameterranges-autoparameters): {{
    - AutoParametersItems}}
  [CategoricalParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-categoricalparameterranges): {{
    - CategoricalParameterRangesItems}}
  [ContinuousParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-continuousparameterranges): {{
    - ContinuousParameterRangesItems}}
  [IntegerParameterRanges](#cfn-sagemaker-hyperparametertuningjob-parameterranges-integerparameterranges): {{
    - IntegerParameterRangesItems}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-parameterranges-properties"></a>

`AutoParameters`  <a name="cfn-sagemaker-hyperparametertuningjob-parameterranges-autoparameters"></a>
A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.
*Required*: No
*Type*: Array of [AutoParametersItems](aws-properties-sagemaker-hyperparametertuningjob-autoparametersitems.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CategoricalParameterRanges`  <a name="cfn-sagemaker-hyperparametertuningjob-parameterranges-categoricalparameterranges"></a>
The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
*Required*: No
*Type*: Array of [CategoricalParameterRangesItems](aws-properties-sagemaker-hyperparametertuningjob-categoricalparameterrangesitems.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContinuousParameterRanges`  <a name="cfn-sagemaker-hyperparametertuningjob-parameterranges-continuousparameterranges"></a>
The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.
*Required*: No
*Type*: Array of [ContinuousParameterRangesItems](aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegerParameterRanges`  <a name="cfn-sagemaker-hyperparametertuningjob-parameterranges-integerparameterranges"></a>
The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.
*Required*: No
*Type*: Array of [IntegerParameterRangesItems](aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
