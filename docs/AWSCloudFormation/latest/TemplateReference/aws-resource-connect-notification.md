---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-notification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Notification
<a name="aws-resource-connect-notification"></a>

Contains information about a notification, including its content, priority, recipients, and metadata.

## Syntax
<a name="aws-resource-connect-notification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-notification-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Notification",
  "Properties" : {
      "[Content](#cfn-connect-notification-content)" : {{NotificationContent}},
      "[ExpiresAt](#cfn-connect-notification-expiresat)" : {{String}},
      "[InstanceArn](#cfn-connect-notification-instancearn)" : {{String}},
      "[Priority](#cfn-connect-notification-priority)" : {{String}},
      "[Recipients](#cfn-connect-notification-recipients)" : {{[ String, ... ]}},
      "[Tags](#cfn-connect-notification-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-notification-syntax.yaml"></a>

```
Type: AWS::Connect::Notification
Properties:
  [Content](#cfn-connect-notification-content): {{
    NotificationContent}}
  [ExpiresAt](#cfn-connect-notification-expiresat): {{String}}
  [InstanceArn](#cfn-connect-notification-instancearn): {{String}}
  [Priority](#cfn-connect-notification-priority): {{String}}
  [Recipients](#cfn-connect-notification-recipients): {{
    - String}}
  [Tags](#cfn-connect-notification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-notification-properties"></a>

`Content`  <a name="cfn-connect-notification-content"></a>
The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale.
*Required*: Yes
*Type*: [NotificationContent](aws-properties-connect-notification-notificationcontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpiresAt`  <a name="cfn-connect-notification-expiresat"></a>
The timestamp when the notification expires and is no longer displayed to users.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceArn`  <a name="cfn-connect-notification-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-connect-notification-priority"></a>
The priority level of the notification. Valid values are URGENT, HIGH, and LOW.
*Required*: No
*Type*: String
*Allowed values*: `HIGH | LOW`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Recipients`  <a name="cfn-connect-notification-recipients"></a>
A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Maximum of 200 recipients.
*Required*: No
*Type*: Array of String
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-notification-tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-notification-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-notification-return-values"></a>

### Ref
<a name="aws-resource-connect-notification-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the notification ARN.

### Fn::GetAtt
<a name="aws-resource-connect-notification-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-connect-notification-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the notification.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the notification was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier for the notification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
