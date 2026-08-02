---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskScheduledEventAttributes.html
---

# ActivityTaskScheduledEventAttributes
<a name="API_ActivityTaskScheduledEventAttributes"></a>

Provides the details of the `ActivityTaskScheduled` event.

## Contents
<a name="API_ActivityTaskScheduledEventAttributes_Contents"></a>

 ** activityId **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-activityId"></a>
The unique ID of the activity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** activityType **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-activityType"></a>
The type of the activity task.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** taskList **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-taskList"></a>
The task list in which the activity task has been scheduled.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** control **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn't sent to the activity.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** heartbeatTimeout **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-heartbeatTimeout"></a>
The maximum time before which the worker processing this task must report progress by calling [RecordActivityTaskHeartbeat](API_RecordActivityTaskHeartbeat.md). If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** input **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-input"></a>
The input provided to the activity task.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** scheduleToCloseTimeout **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-scheduleToCloseTimeout"></a>
The maximum amount of time for this activity task.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** scheduleToStartTimeout **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-scheduleToStartTimeout"></a>
The maximum amount of time the activity task can wait to be assigned to a worker.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** startToCloseTimeout **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-startToCloseTimeout"></a>
The maximum amount of time a worker may take to process the activity task.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** taskPriority **   <a name="SWF-Type-ActivityTaskScheduledEventAttributes-taskPriority"></a>
 The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_ActivityTaskScheduledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskScheduledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskScheduledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskScheduledEventAttributes)
