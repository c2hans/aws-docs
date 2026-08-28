---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-customimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain CustomImage
<a name="aws-properties-sagemaker-domain-customimage"></a>

A custom SageMaker AI image. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html).

## Syntax
<a name="aws-properties-sagemaker-domain-customimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-customimage-syntax.json"></a>

```
{
  "[AppImageConfigName](#cfn-sagemaker-domain-customimage-appimageconfigname)" : {{String}},
  "[ImageName](#cfn-sagemaker-domain-customimage-imagename)" : {{String}},
  "[ImageVersionNumber](#cfn-sagemaker-domain-customimage-imageversionnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-customimage-syntax.yaml"></a>

```
  [AppImageConfigName](#cfn-sagemaker-domain-customimage-appimageconfigname): {{String}}
  [ImageName](#cfn-sagemaker-domain-customimage-imagename): {{String}}
  [ImageVersionNumber](#cfn-sagemaker-domain-customimage-imageversionnumber): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-domain-customimage-properties"></a>

`AppImageConfigName`  <a name="cfn-sagemaker-domain-customimage-appimageconfigname"></a>
The name of the AppImageConfig.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageName`  <a name="cfn-sagemaker-domain-customimage-imagename"></a>
The name of the CustomImage. Must be unique to your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageVersionNumber`  <a name="cfn-sagemaker-domain-customimage-imageversionnumber"></a>
The version number of the CustomImage.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
