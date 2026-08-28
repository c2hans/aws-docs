---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-scheduledtriggerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow ScheduledTriggerProperties
<a name="aws-properties-appflow-flow-scheduledtriggerproperties"></a>

 Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the `Scheduled` trigger type.

## Syntax
<a name="aws-properties-appflow-flow-scheduledtriggerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-scheduledtriggerproperties-syntax.json"></a>

```
{
  "[DataPullMode](#cfn-appflow-flow-scheduledtriggerproperties-datapullmode)" : {{String}},
  "[FirstExecutionFrom](#cfn-appflow-flow-scheduledtriggerproperties-firstexecutionfrom)" : {{Number}},
  "[FlowErrorDeactivationThreshold](#cfn-appflow-flow-scheduledtriggerproperties-flowerrordeactivationthreshold)" : {{Integer}},
  "[ScheduleEndTime](#cfn-appflow-flow-scheduledtriggerproperties-scheduleendtime)" : {{Number}},
  "[ScheduleExpression](#cfn-appflow-flow-scheduledtriggerproperties-scheduleexpression)" : {{String}},
  "[ScheduleOffset](#cfn-appflow-flow-scheduledtriggerproperties-scheduleoffset)" : {{Number}},
  "[ScheduleStartTime](#cfn-appflow-flow-scheduledtriggerproperties-schedulestarttime)" : {{Number}},
  "[TimeZone](#cfn-appflow-flow-scheduledtriggerproperties-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-scheduledtriggerproperties-syntax.yaml"></a>

```
  [DataPullMode](#cfn-appflow-flow-scheduledtriggerproperties-datapullmode): {{String}}
  [FirstExecutionFrom](#cfn-appflow-flow-scheduledtriggerproperties-firstexecutionfrom): {{Number}}
  [FlowErrorDeactivationThreshold](#cfn-appflow-flow-scheduledtriggerproperties-flowerrordeactivationthreshold): {{Integer}}
  [ScheduleEndTime](#cfn-appflow-flow-scheduledtriggerproperties-scheduleendtime): {{Number}}
  [ScheduleExpression](#cfn-appflow-flow-scheduledtriggerproperties-scheduleexpression): {{String}}
  [ScheduleOffset](#cfn-appflow-flow-scheduledtriggerproperties-scheduleoffset): {{Number}}
  [ScheduleStartTime](#cfn-appflow-flow-scheduledtriggerproperties-schedulestarttime): {{Number}}
  [TimeZone](#cfn-appflow-flow-scheduledtriggerproperties-timezone): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-scheduledtriggerproperties-properties"></a>

`DataPullMode`  <a name="cfn-appflow-flow-scheduledtriggerproperties-datapullmode"></a>
 Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
*Required*: No
*Type*: String
*Allowed values*: `Incremental | Complete`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstExecutionFrom`  <a name="cfn-appflow-flow-scheduledtriggerproperties-firstexecutionfrom"></a>
 Specifies the date range for the records to import from the connector in the first flow run.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowErrorDeactivationThreshold`  <a name="cfn-appflow-flow-scheduledtriggerproperties-flowerrordeactivationthreshold"></a>
Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleEndTime`  <a name="cfn-appflow-flow-scheduledtriggerproperties-scheduleendtime"></a>
The time at which the scheduled flow ends. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-27T13:00:00-07:00`.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-appflow-flow-scheduledtriggerproperties-scheduleexpression"></a>
 The scheduling expression that determines the rate at which the schedule will run, for example `rate(5minutes)`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleOffset`  <a name="cfn-appflow-flow-scheduledtriggerproperties-scheduleoffset"></a>
 Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `36000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleStartTime`  <a name="cfn-appflow-flow-scheduledtriggerproperties-schedulestarttime"></a>
The time at which the scheduled flow starts. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-26T13:00:00-07:00`.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-appflow-flow-scheduledtriggerproperties-timezone"></a>
Specifies the time zone used when referring to the dates and times of a scheduled flow, such as `America/New_York`. This time zone is only a descriptive label. It doesn't affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow.
If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the `America/New_York` timezone are `-04:00` EDT and `-05:00 EST`.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-scheduledtriggerproperties--seealso"></a>
+ [ScheduledTriggerProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ScheduledTriggerProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
