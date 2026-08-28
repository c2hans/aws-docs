---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-notifications-notificationhub-notificationhubstatussummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::NotificationHub NotificationHubStatusSummary
<a name="aws-properties-notifications-notificationhub-notificationhubstatussummary"></a>

Provides additional information about the current `NotificationHub` status.

## Syntax
<a name="aws-properties-notifications-notificationhub-notificationhubstatussummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-notifications-notificationhub-notificationhubstatussummary-syntax.json"></a>

```
{
  "[NotificationHubStatus](#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatus)" : {{String}},
  "[NotificationHubStatusReason](#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatusreason)" : {{String}}
}
```

### YAML
<a name="aws-properties-notifications-notificationhub-notificationhubstatussummary-syntax.yaml"></a>

```
  [NotificationHubStatus](#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatus): {{String}}
  [NotificationHubStatusReason](#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatusreason): {{String}}
```

## Properties
<a name="aws-properties-notifications-notificationhub-notificationhubstatussummary-properties"></a>

`NotificationHubStatus`  <a name="cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatus"></a>
Indicates the current status of the `NotificationHub`.
*Required*: Yes
*Type*: String
*Allowed values*: `ACTIVE | REGISTERING | DEREGISTERING | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationHubStatusReason`  <a name="cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatusreason"></a>
An explanation for the current status.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
