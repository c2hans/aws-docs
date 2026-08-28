---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-environment-monitor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Environment Monitor
<a name="aws-properties-appconfig-environment-monitor"></a>

Amazon CloudWatch alarms to monitor during the deployment process.

## Syntax
<a name="aws-properties-appconfig-environment-monitor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-environment-monitor-syntax.json"></a>

```
{
  "[AlarmArn](#cfn-appconfig-environment-monitor-alarmarn)" : {{String}},
  "[AlarmRoleArn](#cfn-appconfig-environment-monitor-alarmrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-environment-monitor-syntax.yaml"></a>

```
  [AlarmArn](#cfn-appconfig-environment-monitor-alarmarn): {{String}}
  [AlarmRoleArn](#cfn-appconfig-environment-monitor-alarmrolearn): {{String}}
```

## Properties
<a name="aws-properties-appconfig-environment-monitor-properties"></a>

`AlarmArn`  <a name="cfn-appconfig-environment-monitor-alarmarn"></a>
Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlarmRoleArn`  <a name="cfn-appconfig-environment-monitor-alarmrolearn"></a>
ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor `AlarmArn`.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
