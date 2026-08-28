---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarmmuterule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AlarmMuteRule
<a name="aws-resource-cloudwatch-alarmmuterule"></a>

Creates or updates an alarm mute rule.

Alarm mute rules automatically mute alarm actions during predefined time windows. When a mute rule is active, targeted alarms continue to evaluate metrics and transition between states, but their configured actions (such as Amazon SNS notifications or Auto Scaling actions) are muted.

You can create mute rules with recurring schedules using `cron` expressions or one-time mute windows using `at` expressions. Each mute rule can target up to 100 specific alarms by name.

If you specify a rule name that already exists, this operation updates the existing rule with the new configuration.

 **Permissions**

To create or update a mute rule, you must have the `cloudwatch:PutAlarmMuteRule` permission on two types of resources: the alarm mute rule resource itself, and each alarm that the rule targets.

For example, If you want to allow a user to create mute rules that target only specific alarms named "WebServerCPUAlarm" and "DatabaseConnectionAlarm", you would create an IAM policy with one statement granting `cloudwatch:PutAlarmMuteRule` on the alarm mute rule resource (`arn:aws:cloudwatch:[REGION]:123456789012:alarm-mute-rule:*`), and another statement granting `cloudwatch:PutAlarmMuteRule` on the targeted alarm resources (`arn:aws:cloudwatch:[REGION]:123456789012:alarm:WebServerCPUAlarm` and `arn:aws:cloudwatch:[REGION]:123456789012:alarm:DatabaseConnectionAlarm`).

You can also use IAM policy conditions to allow targeting alarms based on resource tags. For example, you can restrict users to create/update mute rules to only target alarms that have a specific tag key-value pair, such as `Team=TeamA`.

## Syntax
<a name="aws-resource-cloudwatch-alarmmuterule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-alarmmuterule-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::AlarmMuteRule",
  "Properties" : {
      "[Description](#cfn-cloudwatch-alarmmuterule-description)" : {{String}},
      "[ExpireDate](#cfn-cloudwatch-alarmmuterule-expiredate)" : {{String}},
      "[MuteTargets](#cfn-cloudwatch-alarmmuterule-mutetargets)" : {{MuteTargets}},
      "[Name](#cfn-cloudwatch-alarmmuterule-name)" : {{String}},
      "[Rule](#cfn-cloudwatch-alarmmuterule-rule)" : {{Rule}},
      "[StartDate](#cfn-cloudwatch-alarmmuterule-startdate)" : {{String}},
      "[Tags](#cfn-cloudwatch-alarmmuterule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-alarmmuterule-syntax.yaml"></a>

```
Type: AWS::CloudWatch::AlarmMuteRule
Properties:
  [Description](#cfn-cloudwatch-alarmmuterule-description): {{String}}
  [ExpireDate](#cfn-cloudwatch-alarmmuterule-expiredate): {{String}}
  [MuteTargets](#cfn-cloudwatch-alarmmuterule-mutetargets): {{
    MuteTargets}}
  [Name](#cfn-cloudwatch-alarmmuterule-name): {{String}}
  [Rule](#cfn-cloudwatch-alarmmuterule-rule): {{
    Rule}}
  [StartDate](#cfn-cloudwatch-alarmmuterule-startdate): {{String}}
  [Tags](#cfn-cloudwatch-alarmmuterule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-alarmmuterule-properties"></a>

`Description`  <a name="cfn-cloudwatch-alarmmuterule-description"></a>
A description of the alarm mute rule that helps you identify its purpose.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpireDate`  <a name="cfn-cloudwatch-alarmmuterule-expiredate"></a>
The date and time when the mute rule expires and is no longer evaluated, specified in ISO 8601 format (for example, `2026-12-31T23:59`). After this time, the rule status becomes EXPIRED. This date and time is interpreted according to the schedule timezone, or UTC if no timezone is specified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MuteTargets`  <a name="cfn-cloudwatch-alarmmuterule-mutetargets"></a>
Specifies which alarms this rule applies to.
*Required*: No
*Type*: [MuteTargets](aws-properties-cloudwatch-alarmmuterule-mutetargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-alarmmuterule-name"></a>
The name of the alarm mute rule. This name must be unique within your AWS account and region.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Rule`  <a name="cfn-cloudwatch-alarmmuterule-rule"></a>
The configuration that defines when and how long alarms should be muted.
*Required*: Yes
*Type*: [Rule](aws-properties-cloudwatch-alarmmuterule-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartDate`  <a name="cfn-cloudwatch-alarmmuterule-startdate"></a>
The date and time when the mute rule becomes active, specified in ISO 8601 format (for example, `2026-04-15T08:00`). If omitted, the rule becomes active immediately upon creation. This date and time is interpreted according to the schedule timezone, or UTC if no timezone is specified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-alarmmuterule-tags"></a>
A list of key-value pairs to associate with the alarm mute rule. You can use tags to categorize and manage your mute rules.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-alarmmuterule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-alarmmuterule-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-alarmmuterule-return-values-ref"></a>

The name of the alarm mute rule.

### Fn::GetAtt
<a name="aws-resource-cloudwatch-alarmmuterule-return-values-fn--getatt"></a>

Retrieves details for a specific alarm mute rule.

This operation returns complete information about the mute rule, including its configuration, status, targeted alarms, and metadata.

The returned status indicates the current state of the mute rule:
+ **SCHEDULED**: The mute rule is configured and will become active in the future
+ **ACTIVE**: The mute rule is currently muting alarm actions
+ **EXPIRED**: The mute rule has passed its expiration date and will no longer become active

 **Permissions**

To retrieve details for a mute rule, you need the `cloudwatch:GetAlarmMuteRule` permission on the alarm mute rule resource.

####
<a name="aws-resource-cloudwatch-alarmmuterule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the alarm mute rule.

`LastUpdatedTimestamp`  <a name="LastUpdatedTimestamp-fn::getatt"></a>
The date and time when the mute rule was last updated.

`MuteType`  <a name="MuteType-fn::getatt"></a>
Indicates whether the mute rule is one-time or recurring. Valid values are `ONE_TIME` or `RECURRING`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the alarm mute rule. Valid values are `SCHEDULED`, `ACTIVE`, or `EXPIRED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
