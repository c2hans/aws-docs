---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-notificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery NotificationConfiguration
<a name="aws-properties-timestream-scheduledquery-notificationconfiguration"></a>

Notification configuration for a scheduled query. A notification is sent by Timestream when a scheduled query is created, its state is updated or when it is deleted.

## Syntax
<a name="aws-properties-timestream-scheduledquery-notificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-notificationconfiguration-syntax.json"></a>

```
{
  "[SnsConfiguration](#cfn-timestream-scheduledquery-notificationconfiguration-snsconfiguration)" : {{SnsConfiguration}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-notificationconfiguration-syntax.yaml"></a>

```
  [SnsConfiguration](#cfn-timestream-scheduledquery-notificationconfiguration-snsconfiguration): {{
    SnsConfiguration}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-notificationconfiguration-properties"></a>

`SnsConfiguration`  <a name="cfn-timestream-scheduledquery-notificationconfiguration-snsconfiguration"></a>
Details on SNS configuration.
*Required*: Yes
*Type*: [SnsConfiguration](aws-properties-timestream-scheduledquery-snsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
