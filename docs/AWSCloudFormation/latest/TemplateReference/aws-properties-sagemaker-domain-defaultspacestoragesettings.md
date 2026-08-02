---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-defaultspacestoragesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain DefaultSpaceStorageSettings
<a name="aws-properties-sagemaker-domain-defaultspacestoragesettings"></a>

The default storage settings for a space.

## Syntax
<a name="aws-properties-sagemaker-domain-defaultspacestoragesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-defaultspacestoragesettings-syntax.json"></a>

```
{
  "[DefaultEbsStorageSettings](#cfn-sagemaker-domain-defaultspacestoragesettings-defaultebsstoragesettings)" : {{DefaultEbsStorageSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-defaultspacestoragesettings-syntax.yaml"></a>

```
  [DefaultEbsStorageSettings](#cfn-sagemaker-domain-defaultspacestoragesettings-defaultebsstoragesettings): {{
    DefaultEbsStorageSettings}}
```

## Properties
<a name="aws-properties-sagemaker-domain-defaultspacestoragesettings-properties"></a>

`DefaultEbsStorageSettings`  <a name="cfn-sagemaker-domain-defaultspacestoragesettings-defaultebsstoragesettings"></a>
The default EBS storage settings for a space.
*Required*: No
*Type*: [DefaultEbsStorageSettings](aws-properties-sagemaker-domain-defaultebsstoragesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
