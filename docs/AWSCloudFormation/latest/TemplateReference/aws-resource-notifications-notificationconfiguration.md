---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-notificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::NotificationConfiguration
<a name="aws-resource-notifications-notificationconfiguration"></a>

Configures a `NotificationConfiguration` for AWS User Notifications.

## Syntax
<a name="aws-resource-notifications-notificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-notificationconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::NotificationConfiguration",
  "Properties" : {
      "[AggregationDuration](#cfn-notifications-notificationconfiguration-aggregationduration)" : {{String}},
      "[Description](#cfn-notifications-notificationconfiguration-description)" : {{String}},
      "[Name](#cfn-notifications-notificationconfiguration-name)" : {{String}},
      "[Tags](#cfn-notifications-notificationconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-notifications-notificationconfiguration-syntax.yaml"></a>

```
Type: AWS::Notifications::NotificationConfiguration
Properties:
  [AggregationDuration](#cfn-notifications-notificationconfiguration-aggregationduration): {{String}}
  [Description](#cfn-notifications-notificationconfiguration-description): {{String}}
  [Name](#cfn-notifications-notificationconfiguration-name): {{String}}
  [Tags](#cfn-notifications-notificationconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-notifications-notificationconfiguration-properties"></a>

`AggregationDuration`  <a name="cfn-notifications-notificationconfiguration-aggregationduration"></a>
The aggregation preference of the `NotificationConfiguration`.
+ Values:
  +  `LONG`
    + Aggregate notifications for long periods of time (12 hours).
  +  `SHORT`
    + Aggregate notifications for short periods of time (5 minutes).
  +  `NONE`
    + Don't aggregate notifications.
*Required*: No
*Type*: String
*Allowed values*: `LONG | SHORT | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-notifications-notificationconfiguration-description"></a>
The description of the `NotificationConfiguration`.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\u0001-\u001F\u007F-\u009F]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-notifications-notificationconfiguration-name"></a>
The name of the `NotificationConfiguration`. Supports RFC 3986's unreserved characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-notifications-notificationconfiguration-tags"></a>
A map of tags assigned to a `NotificationConfiguration`.
*Required*: No
*Type*: Array of [Tag](aws-properties-notifications-notificationconfiguration-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-notificationconfiguration-return-values"></a>

### Ref
<a name="aws-resource-notifications-notificationconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.

### Fn::GetAtt
<a name="aws-resource-notifications-notificationconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-notifications-notificationconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration` resource.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of the `NotificationConfiguration`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the `NotificationConfiguration`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
