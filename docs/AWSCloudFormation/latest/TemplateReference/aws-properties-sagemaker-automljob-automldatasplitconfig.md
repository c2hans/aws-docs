---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automldatasplitconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLDataSplitConfig
<a name="aws-properties-sagemaker-automljob-automldatasplitconfig"></a>

This structure specifies how to split the data into train and validation datasets.

The validation and training datasets must contain the same headers. For jobs created by calling `CreateAutoMLJob`, the validation dataset must be less than 2 GB in size.

## Syntax
<a name="aws-properties-sagemaker-automljob-automldatasplitconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automldatasplitconfig-syntax.json"></a>

```
{
  "[ValidationFraction](#cfn-sagemaker-automljob-automldatasplitconfig-validationfraction)" : {{Number}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automldatasplitconfig-syntax.yaml"></a>

```
  [ValidationFraction](#cfn-sagemaker-automljob-automldatasplitconfig-validationfraction): {{Number}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automldatasplitconfig-properties"></a>

`ValidationFraction`  <a name="cfn-sagemaker-automljob-automldatasplitconfig-validationfraction"></a>
The validation fraction (optional) is a float that specifies the portion of the training dataset to be used for validation. The default value is 0.2, and values must be greater than 0 and less than 1. We recommend setting this value to be less than 0.5.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
