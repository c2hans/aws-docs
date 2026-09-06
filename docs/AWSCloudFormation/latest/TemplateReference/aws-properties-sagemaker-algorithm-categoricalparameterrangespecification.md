---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-categoricalparameterrangespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm CategoricalParameterRangeSpecification
<a name="aws-properties-sagemaker-algorithm-categoricalparameterrangespecification"></a>

Defines the possible values for a categorical hyperparameter.

## Syntax
<a name="aws-properties-sagemaker-algorithm-categoricalparameterrangespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-categoricalparameterrangespecification-syntax.json"></a>

```
{
  "[Values](#cfn-sagemaker-algorithm-categoricalparameterrangespecification-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-categoricalparameterrangespecification-syntax.yaml"></a>

```
  [Values](#cfn-sagemaker-algorithm-categoricalparameterrangespecification-values): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-categoricalparameterrangespecification-properties"></a>

`Values`  <a name="cfn-sagemaker-algorithm-categoricalparameterrangespecification-values"></a>
The allowed categories for the hyperparameter.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256 | 30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
