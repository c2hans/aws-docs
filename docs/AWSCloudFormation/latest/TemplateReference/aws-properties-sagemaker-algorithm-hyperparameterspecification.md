---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-hyperparameterspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm HyperParameterSpecification
<a name="aws-properties-sagemaker-algorithm-hyperparameterspecification"></a>

Defines a hyperparameter to be used by an algorithm.

## Syntax
<a name="aws-properties-sagemaker-algorithm-hyperparameterspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-hyperparameterspecification-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-sagemaker-algorithm-hyperparameterspecification-defaultvalue)" : {{String}},
  "[Description](#cfn-sagemaker-algorithm-hyperparameterspecification-description)" : {{String}},
  "[IsRequired](#cfn-sagemaker-algorithm-hyperparameterspecification-isrequired)" : {{Boolean}},
  "[IsTunable](#cfn-sagemaker-algorithm-hyperparameterspecification-istunable)" : {{Boolean}},
  "[Name](#cfn-sagemaker-algorithm-hyperparameterspecification-name)" : {{String}},
  "[Range](#cfn-sagemaker-algorithm-hyperparameterspecification-range)" : {{ParameterRange}},
  "[Type](#cfn-sagemaker-algorithm-hyperparameterspecification-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-hyperparameterspecification-syntax.yaml"></a>

```
  [DefaultValue](#cfn-sagemaker-algorithm-hyperparameterspecification-defaultvalue): {{String}}
  [Description](#cfn-sagemaker-algorithm-hyperparameterspecification-description): {{String}}
  [IsRequired](#cfn-sagemaker-algorithm-hyperparameterspecification-isrequired): {{Boolean}}
  [IsTunable](#cfn-sagemaker-algorithm-hyperparameterspecification-istunable): {{Boolean}}
  [Name](#cfn-sagemaker-algorithm-hyperparameterspecification-name): {{String}}
  [Range](#cfn-sagemaker-algorithm-hyperparameterspecification-range): {{
    ParameterRange}}
  [Type](#cfn-sagemaker-algorithm-hyperparameterspecification-type): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-hyperparameterspecification-properties"></a>

`DefaultValue`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-defaultvalue"></a>
The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.
*Required*: No
*Type*: String
*Maximum*: `2500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-description"></a>
A brief description of the hyperparameter.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsRequired`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-isrequired"></a>
Indicates whether this hyperparameter is required.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsTunable`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-istunable"></a>
Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-name"></a>
The name of this hyperparameter. The name must be unique.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Range`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-range"></a>
The allowed range for this hyperparameter.
*Required*: No
*Type*: [ParameterRange](aws-properties-sagemaker-algorithm-parameterrange.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-sagemaker-algorithm-hyperparameterspecification-type"></a>
The type of this hyperparameter. The valid types are `Integer`, `Continuous`, `Categorical`, and `FreeText`.
*Required*: Yes
*Type*: String
*Allowed values*: `Integer | Continuous | Categorical | FreeText`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
