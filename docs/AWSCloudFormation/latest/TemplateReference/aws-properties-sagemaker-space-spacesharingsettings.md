---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacesharingsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceSharingSettings
<a name="aws-properties-sagemaker-space-spacesharingsettings"></a>

A collection of space sharing settings.

## Syntax
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax.json"></a>

```
{
  "[SharingType](#cfn-sagemaker-space-spacesharingsettings-sharingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax.yaml"></a>

```
  [SharingType](#cfn-sagemaker-space-spacesharingsettings-sharingtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacesharingsettings-properties"></a>

`SharingType`  <a name="cfn-sagemaker-space-spacesharingsettings-sharingtype"></a>
Specifies the sharing type of the space.
*Required*: Yes
*Type*: String
*Allowed values*: `Private | Shared`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
