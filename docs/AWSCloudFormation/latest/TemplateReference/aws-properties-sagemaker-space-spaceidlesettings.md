---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spaceidlesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceIdleSettings
<a name="aws-properties-sagemaker-space-spaceidlesettings"></a>

Settings related to idle shutdown of Studio applications in a space.

## Syntax
<a name="aws-properties-sagemaker-space-spaceidlesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spaceidlesettings-syntax.json"></a>

```
{
  "[IdleTimeoutInMinutes](#cfn-sagemaker-space-spaceidlesettings-idletimeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spaceidlesettings-syntax.yaml"></a>

```
  [IdleTimeoutInMinutes](#cfn-sagemaker-space-spaceidlesettings-idletimeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-space-spaceidlesettings-properties"></a>

`IdleTimeoutInMinutes`  <a name="cfn-sagemaker-space-spaceidlesettings-idletimeoutinminutes"></a>
The time that SageMaker waits after the application becomes idle before shutting it down.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `525600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
