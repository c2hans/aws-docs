---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spaceapplifecyclemanagement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceAppLifecycleManagement
<a name="aws-properties-sagemaker-space-spaceapplifecyclemanagement"></a>

Settings that are used to configure and manage the lifecycle of Amazon SageMaker Studio applications in a space.

## Syntax
<a name="aws-properties-sagemaker-space-spaceapplifecyclemanagement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spaceapplifecyclemanagement-syntax.json"></a>

```
{
  "[IdleSettings](#cfn-sagemaker-space-spaceapplifecyclemanagement-idlesettings)" : {{SpaceIdleSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spaceapplifecyclemanagement-syntax.yaml"></a>

```
  [IdleSettings](#cfn-sagemaker-space-spaceapplifecyclemanagement-idlesettings): {{
    SpaceIdleSettings}}
```

## Properties
<a name="aws-properties-sagemaker-space-spaceapplifecyclemanagement-properties"></a>

`IdleSettings`  <a name="cfn-sagemaker-space-spaceapplifecyclemanagement-idlesettings"></a>
Settings related to idle shutdown of Studio applications.
*Required*: No
*Type*: [SpaceIdleSettings](aws-properties-sagemaker-space-spaceidlesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
