---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpoint-autorollbackconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Endpoint AutoRollbackConfig
<a name="aws-properties-sagemaker-endpoint-autorollbackconfig"></a>

Automatic rollback configuration for handling endpoint deployment failures and recovery.

## Syntax
<a name="aws-properties-sagemaker-endpoint-autorollbackconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpoint-autorollbackconfig-syntax.json"></a>

```
{
  "[Alarms](#cfn-sagemaker-endpoint-autorollbackconfig-alarms)" : {{[ Alarm, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpoint-autorollbackconfig-syntax.yaml"></a>

```
  [Alarms](#cfn-sagemaker-endpoint-autorollbackconfig-alarms): {{
    - Alarm}}
```

## Properties
<a name="aws-properties-sagemaker-endpoint-autorollbackconfig-properties"></a>

`Alarms`  <a name="cfn-sagemaker-endpoint-autorollbackconfig-alarms"></a>
List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.
*Required*: Yes
*Type*: Array of [Alarm](aws-properties-sagemaker-endpoint-alarm.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
