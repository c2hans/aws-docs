---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-notificationhub.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::NotificationHub
<a name="aws-resource-notifications-notificationhub"></a>

Configures a `NotificationHub` for AWS User Notifications. For more information about notification hub, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html).

## Syntax
<a name="aws-resource-notifications-notificationhub-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-notificationhub-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::NotificationHub",
  "Properties" : {
      "[Region](#cfn-notifications-notificationhub-region)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-notificationhub-syntax.yaml"></a>

```
Type: AWS::Notifications::NotificationHub
Properties:
  [Region](#cfn-notifications-notificationhub-region): {{String}}
```

## Properties
<a name="aws-resource-notifications-notificationhub-properties"></a>

`Region`  <a name="cfn-notifications-notificationhub-region"></a>
The `NotificationHub` Region.
*Required*: Yes
*Type*: String
*Minimum*: `2`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-notificationhub-return-values"></a>

### Ref
<a name="aws-resource-notifications-notificationhub-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-notifications-notificationhub-return-values-fn--getatt"></a>

####
<a name="aws-resource-notifications-notificationhub-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time the `NotificationHubOverview` was created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
