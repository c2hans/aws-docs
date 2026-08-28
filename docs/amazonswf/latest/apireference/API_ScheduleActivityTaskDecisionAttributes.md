---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ScheduleActivityTaskDecisionAttributes.html
---

# ScheduleActivityTaskDecisionAttributes
<a name="API_ScheduleActivityTaskDecisionAttributes"></a>

Provides the details of the `ScheduleActivityTask` decision.

 **Access Control**

You can use IAM policies to control this decision's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `activityType.name` – String constraint. The key is `swf:activityType.name`.
  +  `activityType.version` – String constraint. The key is `swf:activityType.version`.
  +  `taskList` – String constraint. The key is `swf:taskList.name`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Contents
<a name="API_ScheduleActivityTaskDecisionAttributes_Contents"></a>

 ** activityId **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-activityId"></a>
 The `activityId` of the activity task.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** activityType **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-activityType"></a>
 The type of the activity task to schedule.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** control **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn't sent to the activity.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** heartbeatTimeout **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-heartbeatTimeout"></a>
If set, specifies the maximum time before which a worker processing a task of this type must report progress by calling [RecordActivityTaskHeartbeat](API_RecordActivityTaskHeartbeat.md). If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or returns a result, it is ignored. This overrides the default heartbeat timeout specified when registering the activity type using [RegisterActivityType](API_RegisterActivityType.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** input **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-input"></a>
The input provided to the activity task.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** scheduleToCloseTimeout **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-scheduleToCloseTimeout"></a>
The maximum duration for this activity task.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
A schedule-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-close timeout was specified at registration time then a fault is returned.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** scheduleToStartTimeout **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-scheduleToStartTimeout"></a>
 If set, specifies the maximum duration the activity task can wait to be assigned to a worker. This overrides the default schedule-to-start timeout specified when registering the activity type using [RegisterActivityType](API_RegisterActivityType.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
A schedule-to-start timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-start timeout was specified at registration time then a fault is returned.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** startToCloseTimeout **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-startToCloseTimeout"></a>
If set, specifies the maximum duration a worker may take to process this activity task. This overrides the default start-to-close timeout specified when registering the activity type using [RegisterActivityType](API_RegisterActivityType.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
A start-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default start-to-close timeout was specified at registration time then a fault is returned.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** taskList **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-taskList"></a>
If set, specifies the name of the task list in which to schedule the activity task. If not specified, the `defaultTaskList` registered with the activity type is used.
A task list for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default task list was specified at registration time then a fault is returned.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: [TaskList](API_TaskList.md) object
Required: No

 ** taskPriority **   <a name="SWF-Type-ScheduleActivityTaskDecisionAttributes-taskPriority"></a>
 If set, specifies the priority with which the activity task is to be assigned to a worker. This overrides the defaultTaskPriority specified when registering the activity type using [RegisterActivityType](API_RegisterActivityType.md). Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_ScheduleActivityTaskDecisionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ScheduleActivityTaskDecisionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ScheduleActivityTaskDecisionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ScheduleActivityTaskDecisionAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
