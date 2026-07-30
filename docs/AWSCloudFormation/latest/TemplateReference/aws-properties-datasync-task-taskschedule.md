---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-taskschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task TaskSchedule
<a name="aws-properties-datasync-task-taskschedule"></a>

Configures your AWS DataSync task to run on a [schedule](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html) (at a minimum interval of 1 hour).

## Syntax
<a name="aws-properties-datasync-task-taskschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-taskschedule-syntax.json"></a>

```
{
  "[ScheduleExpression](#cfn-datasync-task-taskschedule-scheduleexpression)" : {{String}},
  "[Status](#cfn-datasync-task-taskschedule-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-task-taskschedule-syntax.yaml"></a>

```
  [ScheduleExpression](#cfn-datasync-task-taskschedule-scheduleexpression): {{String}}
  [Status](#cfn-datasync-task-taskschedule-status): {{String}}
```

## Properties
<a name="aws-properties-datasync-task-taskschedule-properties"></a>

`ScheduleExpression`  <a name="cfn-datasync-task-taskschedule-scheduleexpression"></a>
Specifies your task schedule by using a cron or rate expression.
Use cron expressions for task schedules that run on a specific time and day. For example, the following cron expression creates a task schedule that runs at 8 AM on the first Wednesday of every month:
 `cron(0 8 * * 3#1)`
Use rate expressions for task schedules that run on a regular interval. For example, the following rate expression creates a task schedule that runs every 12 hours:
 `rate(12 hours)`
For information about cron and rate expression syntax, see the [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\ \_\*\?\,\|\^\-\/\#\s\(\)\+]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-datasync-task-taskschedule-status"></a>
Specifies whether to enable or disable your task schedule. Your schedule is enabled by default, but there can be situations where you need to disable it. For example, you might need to pause a recurring transfer to fix an issue with your task or perform maintenance on your storage system.
DataSync might disable your schedule automatically if your task fails repeatedly with the same error. For more information, see [TaskScheduleDetails](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskScheduleDetails.html).
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
