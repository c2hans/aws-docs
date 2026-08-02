---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-hiddensagemakerimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile HiddenSageMakerImage
<a name="aws-properties-sagemaker-userprofile-hiddensagemakerimage"></a>

The SageMaker images that are hidden from the Studio user interface. You must specify the SageMaker image name and version aliases.

## Syntax
<a name="aws-properties-sagemaker-userprofile-hiddensagemakerimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-hiddensagemakerimage-syntax.json"></a>

```
{
  "[SageMakerImageName](#cfn-sagemaker-userprofile-hiddensagemakerimage-sagemakerimagename)" : {{String}},
  "[VersionAliases](#cfn-sagemaker-userprofile-hiddensagemakerimage-versionaliases)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-hiddensagemakerimage-syntax.yaml"></a>

```
  [SageMakerImageName](#cfn-sagemaker-userprofile-hiddensagemakerimage-sagemakerimagename): {{String}}
  [VersionAliases](#cfn-sagemaker-userprofile-hiddensagemakerimage-versionaliases): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-hiddensagemakerimage-properties"></a>

`SageMakerImageName`  <a name="cfn-sagemaker-userprofile-hiddensagemakerimage-sagemakerimagename"></a>
 The SageMaker image name that you are hiding from the Studio user interface.
*Required*: No
*Type*: String
*Allowed values*: `sagemaker_distribution`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionAliases`  <a name="cfn-sagemaker-userprofile-hiddensagemakerimage-versionaliases"></a>
 The version aliases you are hiding from the Studio user interface.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
