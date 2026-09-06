---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-parameterrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm ParameterRange
<a name="aws-properties-sagemaker-algorithm-parameterrange"></a>

Defines the possible values for categorical, continuous, and integer hyperparameters to be used by an algorithm.

## Syntax
<a name="aws-properties-sagemaker-algorithm-parameterrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-parameterrange-syntax.json"></a>

```
{
  "[CategoricalParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-categoricalparameterrangespecification)" : {{CategoricalParameterRangeSpecification}},
  "[ContinuousParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-continuousparameterrangespecification)" : {{ContinuousParameterRangeSpecification}},
  "[IntegerParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-integerparameterrangespecification)" : {{IntegerParameterRangeSpecification}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-parameterrange-syntax.yaml"></a>

```
  [CategoricalParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-categoricalparameterrangespecification): {{
    CategoricalParameterRangeSpecification}}
  [ContinuousParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-continuousparameterrangespecification): {{
    ContinuousParameterRangeSpecification}}
  [IntegerParameterRangeSpecification](#cfn-sagemaker-algorithm-parameterrange-integerparameterrangespecification): {{
    IntegerParameterRangeSpecification}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-parameterrange-properties"></a>

`CategoricalParameterRangeSpecification`  <a name="cfn-sagemaker-algorithm-parameterrange-categoricalparameterrangespecification"></a>
A `CategoricalParameterRangeSpecification` object that defines the possible values for a categorical hyperparameter.
*Required*: No
*Type*: [CategoricalParameterRangeSpecification](aws-properties-sagemaker-algorithm-categoricalparameterrangespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContinuousParameterRangeSpecification`  <a name="cfn-sagemaker-algorithm-parameterrange-continuousparameterrangespecification"></a>
A `ContinuousParameterRangeSpecification` object that defines the possible values for a continuous hyperparameter.
*Required*: No
*Type*: [ContinuousParameterRangeSpecification](aws-properties-sagemaker-algorithm-continuousparameterrangespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegerParameterRangeSpecification`  <a name="cfn-sagemaker-algorithm-parameterrange-integerparameterrangespecification"></a>
A `IntegerParameterRangeSpecification` object that defines the possible values for an integer hyperparameter.
*Required*: No
*Type*: [IntegerParameterRangeSpecification](aws-properties-sagemaker-algorithm-integerparameterrangespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
