---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob ContinuousParameterRangesItems
<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems"></a>

<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-description"></a>The `ContinuousParameterRangesItems` property type specifies Property description not available. for an [AWS::SageMaker::HyperParameterTuningJob](aws-resource-sagemaker-hyperparametertuningjob.md).

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-syntax.json"></a>

```
{
  "[MaxValue](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-maxvalue)" : {{String}},
  "[MinValue](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-minvalue)" : {{String}},
  "[Name](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-name)" : {{String}},
  "[ScalingType](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-scalingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-syntax.yaml"></a>

```
  [MaxValue](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-maxvalue): {{String}}
  [MinValue](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-minvalue): {{String}}
  [Name](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-name): {{String}}
  [ScalingType](#cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-scalingtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-properties"></a>

`MaxValue`  <a name="cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-maxvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinValue`  <a name="cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-minvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScalingType`  <a name="cfn-sagemaker-hyperparametertuningjob-continuousparameterrangesitems-scalingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Auto | Linear | Logarithmic | ReverseLogarithmic`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
