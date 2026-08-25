---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob IntegerParameterRangesItems
<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems"></a>

<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems-description"></a>The `IntegerParameterRangesItems` property type specifies Property description not available. for an [AWS::SageMaker::HyperParameterTuningJob](aws-resource-sagemaker-hyperparametertuningjob.md).

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems-syntax.json"></a>

```
{
  "[MaxValue](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-maxvalue)" : {{String}},
  "[MinValue](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-minvalue)" : {{String}},
  "[Name](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-name)" : {{String}},
  "[ScalingType](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-scalingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems-syntax.yaml"></a>

```
  [MaxValue](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-maxvalue): {{String}}
  [MinValue](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-minvalue): {{String}}
  [Name](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-name): {{String}}
  [ScalingType](#cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-scalingtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-integerparameterrangesitems-properties"></a>

`MaxValue`  <a name="cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-maxvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinValue`  <a name="cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-minvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScalingType`  <a name="cfn-sagemaker-hyperparametertuningjob-integerparameterrangesitems-scalingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Auto | Linear | Logarithmic | ReverseLogarithmic`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
