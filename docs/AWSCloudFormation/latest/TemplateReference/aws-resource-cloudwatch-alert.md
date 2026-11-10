---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alert.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert
<a name="aws-resource-cloudwatch-alert"></a>

Resource Type definition for `AWS::CloudWatch::Alert`. An alert runs a SQL or PromQL query in a CloudWatch Omni space on a fixed interval, compares the result against warning and critical thresholds, and sends notifications to Amazon SNS topics or integrations when its state changes.

## Syntax
<a name="aws-resource-cloudwatch-alert-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-alert-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::Alert",
  "Properties" : {
      "[Description](#cfn-cloudwatch-alert-description)" : {{String}},
      "[Name](#cfn-cloudwatch-alert-name)" : {{String}},
      "[NotificationRules](#cfn-cloudwatch-alert-notificationrules)" : {{[ NotificationRule, ... ]}},
      "[NotificationsEnabled](#cfn-cloudwatch-alert-notificationsenabled)" : {{Boolean}},
      "[ProfileId](#cfn-cloudwatch-alert-profileid)" : {{String}},
      "[Rule](#cfn-cloudwatch-alert-rule)" : {{Rule}},
      "[SpaceId](#cfn-cloudwatch-alert-spaceid)" : {{String}},
      "[Tags](#cfn-cloudwatch-alert-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-alert-syntax.yaml"></a>

```
Type: AWS::CloudWatch::Alert
Properties:
  [Description](#cfn-cloudwatch-alert-description): {{String}}
  [Name](#cfn-cloudwatch-alert-name): {{String}}
  [NotificationRules](#cfn-cloudwatch-alert-notificationrules): {{
    - NotificationRule}}
  [NotificationsEnabled](#cfn-cloudwatch-alert-notificationsenabled): {{Boolean}}
  [ProfileId](#cfn-cloudwatch-alert-profileid): {{String}}
  [Rule](#cfn-cloudwatch-alert-rule): {{
    Rule}}
  [SpaceId](#cfn-cloudwatch-alert-spaceid): {{String}}
  [Tags](#cfn-cloudwatch-alert-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-alert-properties"></a>

`Description`  <a name="cfn-cloudwatch-alert-description"></a>
A description of the alert.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-alert-name"></a>
The display name of the alert. Names don't need to be unique within a space; the alert is identified by AlertId.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.@~()-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationRules`  <a name="cfn-cloudwatch-alert-notificationrules"></a>
The notification rules that determine when and where notifications are sent.
*Required*: No
*Type*: Array of [NotificationRule](aws-properties-cloudwatch-alert-notificationrule.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationsEnabled`  <a name="cfn-cloudwatch-alert-notificationsenabled"></a>
Whether the alert sends notifications. When false, the alert is still evaluated and records its state, but sends nothing. Defaults to true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileId`  <a name="cfn-cloudwatch-alert-profileid"></a>
The ID of the access profile the alert uses to run its query and send notifications.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rule`  <a name="cfn-cloudwatch-alert-rule"></a>
Defines the schedule configuration for an alarm mute rule.
The rule contains a schedule that specifies when and how long alarms should be muted. The schedule can be a recurring pattern using cron expressions or a one-time mute window using at expressions.
*Required*: Yes
*Type*: [Rule](aws-properties-cloudwatch-alert-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceId`  <a name="cfn-cloudwatch-alert-spaceid"></a>
The ID of the space to create the alert in. Changing this value replaces the alert.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-alert-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-alert-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-alert-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-alert-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-alert-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-alert-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The AWS account ID that owns the alert.

`AlertId`  <a name="AlertId-fn::getatt"></a>
The ID of the alert, assigned by CloudWatch when the alert is created. It doesn't change when the alert is updated, and it is the resource ID in the alert's ARN.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the alert.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the alert was created, in ISO 8601 format (UTC).

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the alert was last updated, in ISO 8601 format (UTC).
