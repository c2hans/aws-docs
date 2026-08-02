---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-customimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space CustomImage
<a name="aws-properties-sagemaker-space-customimage"></a>

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html).

## Syntax
<a name="aws-properties-sagemaker-space-customimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-customimage-syntax.json"></a>

```
{
  "[AppImageConfigName](#cfn-sagemaker-space-customimage-appimageconfigname)" : {{String}},
  "[ImageName](#cfn-sagemaker-space-customimage-imagename)" : {{String}},
  "[ImageVersionNumber](#cfn-sagemaker-space-customimage-imageversionnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-customimage-syntax.yaml"></a>

```
  [AppImageConfigName](#cfn-sagemaker-space-customimage-appimageconfigname): {{String}}
  [ImageName](#cfn-sagemaker-space-customimage-imagename): {{String}}
  [ImageVersionNumber](#cfn-sagemaker-space-customimage-imageversionnumber): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-space-customimage-properties"></a>

`AppImageConfigName`  <a name="cfn-sagemaker-space-customimage-appimageconfigname"></a>
The name of the AppImageConfig.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageName`  <a name="cfn-sagemaker-space-customimage-imagename"></a>
The name of the CustomImage. Must be unique to your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageVersionNumber`  <a name="cfn-sagemaker-space-customimage-imageversionnumber"></a>
The version number of the CustomImage.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
