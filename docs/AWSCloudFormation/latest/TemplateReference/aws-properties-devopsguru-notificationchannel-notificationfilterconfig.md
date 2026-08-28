---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsGuru::NotificationChannel NotificationFilterConfig
<a name="aws-properties-devopsguru-notificationchannel-notificationfilterconfig"></a>

 The filter configurations for the Amazon SNS notification topic you use with DevOps Guru. You can choose to specify which events or message types to receive notifications for. You can also choose to specify which severity levels to receive notifications for.

## Syntax
<a name="aws-properties-devopsguru-notificationchannel-notificationfilterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsguru-notificationchannel-notificationfilterconfig-syntax.json"></a>

```
{
  "[MessageTypes](#cfn-devopsguru-notificationchannel-notificationfilterconfig-messagetypes)" : {{[ String, ... ]}},
  "[Severities](#cfn-devopsguru-notificationchannel-notificationfilterconfig-severities)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsguru-notificationchannel-notificationfilterconfig-syntax.yaml"></a>

```
  [MessageTypes](#cfn-devopsguru-notificationchannel-notificationfilterconfig-messagetypes): {{
    - String}}
  [Severities](#cfn-devopsguru-notificationchannel-notificationfilterconfig-severities): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsguru-notificationchannel-notificationfilterconfig-properties"></a>

`MessageTypes`  <a name="cfn-devopsguru-notificationchannel-notificationfilterconfig-messagetypes"></a>
 The events that you want to receive notifications for. For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Severities`  <a name="cfn-devopsguru-notificationchannel-notificationfilterconfig-severities"></a>
 The severity levels that you want to receive notifications for. For example, you can choose to receive notifications only for insights with `HIGH` and `MEDIUM` severity levels. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
