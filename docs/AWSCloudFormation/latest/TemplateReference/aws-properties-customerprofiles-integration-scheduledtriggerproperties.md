---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration ScheduledTriggerProperties
<a name="aws-properties-customerprofiles-integration-scheduledtriggerproperties"></a>

Specifies the configuration details of a scheduled-trigger flow that you define. Currently, these settings only apply to the scheduled-trigger type.

## Syntax
<a name="aws-properties-customerprofiles-integration-scheduledtriggerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-scheduledtriggerproperties-syntax.json"></a>

```
{
  "[DataPullMode](#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode)" : {{String}},
  "[FirstExecutionFrom](#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom)" : {{Number}},
  "[ScheduleEndTime](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime)" : {{Number}},
  "[ScheduleExpression](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression)" : {{String}},
  "[ScheduleOffset](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset)" : {{Integer}},
  "[ScheduleStartTime](#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime)" : {{Number}},
  "[Timezone](#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-scheduledtriggerproperties-syntax.yaml"></a>

```
  [DataPullMode](#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode): {{String}}
  [FirstExecutionFrom](#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom): {{Number}}
  [ScheduleEndTime](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime): {{Number}}
  [ScheduleExpression](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression): {{String}}
  [ScheduleOffset](#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset): {{Integer}}
  [ScheduleStartTime](#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime): {{Number}}
  [Timezone](#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-scheduledtriggerproperties-properties"></a>

`DataPullMode`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode"></a>
Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
*Required*: No
*Type*: String
*Allowed values*: `Incremental | Complete`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstExecutionFrom`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom"></a>
Specifies the date range for the records to import from the connector in the first flow run.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleEndTime`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime"></a>
Specifies the scheduled end time for a scheduled-trigger flow.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression"></a>
The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleOffset`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset"></a>
Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `36000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleStartTime`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime"></a>
Specifies the scheduled start time for a scheduled-trigger flow. The value must be a date/time value in EPOCH format.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-customerprofiles-integration-scheduledtriggerproperties-timezone"></a>
Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New\_York.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
