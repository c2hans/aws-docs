---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DecisionTaskScheduledEventAttributes.html
---

# DecisionTaskScheduledEventAttributes
<a name="API_DecisionTaskScheduledEventAttributes"></a>

Provides details about the `DecisionTaskScheduled` event.

## Contents
<a name="API_DecisionTaskScheduledEventAttributes_Contents"></a>

 ** taskList **   <a name="SWF-Type-DecisionTaskScheduledEventAttributes-taskList"></a>
The name of the task list in which the decision task was scheduled.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** scheduleToStartTimeout **   <a name="SWF-Type-DecisionTaskScheduledEventAttributes-scheduleToStartTimeout"></a>
The maximum amount of time the decision task can wait to be assigned to a worker.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** startToCloseTimeout **   <a name="SWF-Type-DecisionTaskScheduledEventAttributes-startToCloseTimeout"></a>
The maximum duration for this decision task. The task is considered timed out if it doesn't completed within this duration.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** taskPriority **   <a name="SWF-Type-DecisionTaskScheduledEventAttributes-taskPriority"></a>
 A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_DecisionTaskScheduledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DecisionTaskScheduledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DecisionTaskScheduledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DecisionTaskScheduledEventAttributes)
