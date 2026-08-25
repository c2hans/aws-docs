---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob MetricDefinitionsItems
<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems"></a>

<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems-description"></a>The `MetricDefinitionsItems` property type specifies Property description not available. for an [AWS::SageMaker::HyperParameterTuningJob](aws-resource-sagemaker-hyperparametertuningjob.md).

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-name)" : {{String}},
  "[Regex](#cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-regex)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-name): {{String}}
  [Regex](#cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-regex): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems-properties"></a>

`Name`  <a name="cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regex`  <a name="cfn-sagemaker-hyperparametertuningjob-metricdefinitionsitems-regex"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
