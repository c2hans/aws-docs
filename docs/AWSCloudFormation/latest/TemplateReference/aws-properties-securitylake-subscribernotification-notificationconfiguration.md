---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscribernotification-notificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::SubscriberNotification NotificationConfiguration
<a name="aws-properties-securitylake-subscribernotification-notificationconfiguration"></a>

Specify the configurations you want to use for subscriber notification. The subscriber is notified when new data is written to the data lake for sources that the subscriber consumes in Security Lake.

## Syntax
<a name="aws-properties-securitylake-subscribernotification-notificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscribernotification-notificationconfiguration-syntax.json"></a>

```
{
  "[HttpsNotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration-httpsnotificationconfiguration)" : {{HttpsNotificationConfiguration}},
  "[SqsNotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration-sqsnotificationconfiguration)" : {{Json}}
}
```

### YAML
<a name="aws-properties-securitylake-subscribernotification-notificationconfiguration-syntax.yaml"></a>

```
  [HttpsNotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration-httpsnotificationconfiguration): {{
    HttpsNotificationConfiguration}}
  [SqsNotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration-sqsnotificationconfiguration): {{Json}}
```

## Properties
<a name="aws-properties-securitylake-subscribernotification-notificationconfiguration-properties"></a>

`HttpsNotificationConfiguration`  <a name="cfn-securitylake-subscribernotification-notificationconfiguration-httpsnotificationconfiguration"></a>
The configurations used for HTTPS subscriber notification.
*Required*: No
*Type*: [HttpsNotificationConfiguration](aws-properties-securitylake-subscribernotification-httpsnotificationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqsNotificationConfiguration`  <a name="cfn-securitylake-subscribernotification-notificationconfiguration-sqsnotificationconfiguration"></a>
The configurations for SQS subscriber notification. The members of this structure are context-dependent.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
