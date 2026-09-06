---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-applifecyclemanagement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain AppLifecycleManagement
<a name="aws-properties-sagemaker-domain-applifecyclemanagement"></a>

Settings that are used to configure and manage the lifecycle of Amazon SageMaker Studio applications.

## Syntax
<a name="aws-properties-sagemaker-domain-applifecyclemanagement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-applifecyclemanagement-syntax.json"></a>

```
{
  "[IdleSettings](#cfn-sagemaker-domain-applifecyclemanagement-idlesettings)" : {{IdleSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-applifecyclemanagement-syntax.yaml"></a>

```
  [IdleSettings](#cfn-sagemaker-domain-applifecyclemanagement-idlesettings): {{
    IdleSettings}}
```

## Properties
<a name="aws-properties-sagemaker-domain-applifecyclemanagement-properties"></a>

`IdleSettings`  <a name="cfn-sagemaker-domain-applifecyclemanagement-idlesettings"></a>
Settings related to idle shutdown of Studio applications.
*Required*: No
*Type*: [IdleSettings](aws-properties-sagemaker-domain-idlesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
