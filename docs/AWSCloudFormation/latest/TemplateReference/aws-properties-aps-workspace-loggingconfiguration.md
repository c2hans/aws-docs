---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace LoggingConfiguration
<a name="aws-properties-aps-workspace-loggingconfiguration"></a>

Contains information about the rules and alerting logging configuration for the workspace.

**Note**
These logging configurations are only for rules and alerting logs.

## Syntax
<a name="aws-properties-aps-workspace-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-loggingconfiguration-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-aps-workspace-loggingconfiguration-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-workspace-loggingconfiguration-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-aps-workspace-loggingconfiguration-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-aps-workspace-loggingconfiguration-properties"></a>

`LogGroupArn`  <a name="cfn-aps-workspace-loggingconfiguration-loggrouparn"></a>
The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
