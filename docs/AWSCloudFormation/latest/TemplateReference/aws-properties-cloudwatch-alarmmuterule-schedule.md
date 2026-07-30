---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarmmuterule-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AlarmMuteRule Schedule
<a name="aws-properties-cloudwatch-alarmmuterule-schedule"></a>

Defines the schedule configuration for an alarm mute rule.

The rule contains a schedule that specifies when and how long alarms should be muted. The schedule can be a recurring pattern using cron expressions or a one-time mute window using at expressions.

## Syntax
<a name="aws-properties-cloudwatch-alarmmuterule-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarmmuterule-schedule-syntax.json"></a>

```
{
  "[Duration](#cfn-cloudwatch-alarmmuterule-schedule-duration)" : {{String}},
  "[Expression](#cfn-cloudwatch-alarmmuterule-schedule-expression)" : {{String}},
  "[Timezone](#cfn-cloudwatch-alarmmuterule-schedule-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarmmuterule-schedule-syntax.yaml"></a>

```
  [Duration](#cfn-cloudwatch-alarmmuterule-schedule-duration): {{String}}
  [Expression](#cfn-cloudwatch-alarmmuterule-schedule-expression): {{String}}
  [Timezone](#cfn-cloudwatch-alarmmuterule-schedule-timezone): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarmmuterule-schedule-properties"></a>

`Duration`  <a name="cfn-cloudwatch-alarmmuterule-schedule-duration"></a>
The configuration that defines when and how long alarms should be muted.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-cloudwatch-alarmmuterule-schedule-expression"></a>
The configuration that defines when and how long alarms should be muted.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-cloudwatch-alarmmuterule-schedule-timezone"></a>
The configuration that defines when and how long alarms should be muted.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
