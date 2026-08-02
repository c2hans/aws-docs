---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent AutoRollbackConfiguration
<a name="aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration"></a>

Configuration for automatic rollback of the inference component deployment if issues are detected.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration-syntax.json"></a>

```
{
  "[Alarms](#cfn-sagemaker-inferencecomponent-autorollbackconfiguration-alarms)" : {{[ Alarm, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration-syntax.yaml"></a>

```
  [Alarms](#cfn-sagemaker-inferencecomponent-autorollbackconfiguration-alarms): {{
    - Alarm}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration-properties"></a>

`Alarms`  <a name="cfn-sagemaker-inferencecomponent-autorollbackconfiguration-alarms"></a>
List of CloudWatch alarms that trigger automatic rollback if they enter the ALARM state during deployment.
*Required*: Yes
*Type*: Array of [Alarm](aws-properties-sagemaker-inferencecomponent-alarm.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
