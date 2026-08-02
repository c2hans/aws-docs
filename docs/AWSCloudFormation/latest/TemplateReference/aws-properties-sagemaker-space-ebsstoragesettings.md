---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-ebsstoragesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space EbsStorageSettings
<a name="aws-properties-sagemaker-space-ebsstoragesettings"></a>

A collection of EBS storage settings that apply to both private and shared spaces.

## Syntax
<a name="aws-properties-sagemaker-space-ebsstoragesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-ebsstoragesettings-syntax.json"></a>

```
{
  "[EbsVolumeSizeInGb](#cfn-sagemaker-space-ebsstoragesettings-ebsvolumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-ebsstoragesettings-syntax.yaml"></a>

```
  [EbsVolumeSizeInGb](#cfn-sagemaker-space-ebsstoragesettings-ebsvolumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-space-ebsstoragesettings-properties"></a>

`EbsVolumeSizeInGb`  <a name="cfn-sagemaker-space-ebsstoragesettings-ebsvolumesizeingb"></a>
The size of an EBS storage volume for a space.
*Required*: Yes
*Type*: Integer
*Minimum*: `5`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
