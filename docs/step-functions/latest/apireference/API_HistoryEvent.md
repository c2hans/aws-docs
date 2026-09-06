---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_HistoryEvent.html
---

# HistoryEvent
<a name="API_HistoryEvent"></a>

Contains details about the events of an execution.

## Contents
<a name="API_HistoryEvent_Contents"></a>

 ** id **   <a name="StepFunctions-Type-HistoryEvent-id"></a>
The id of the event. Events are numbered sequentially, starting at one.
Type: Long
Required: Yes

 ** timestamp **   <a name="StepFunctions-Type-HistoryEvent-timestamp"></a>
The date and time the event occurred, expressed in seconds and fractional milliseconds since the Unix epoch, which is defined as January 1, 1970, at 00:00:00 Coordinated Universal Time (UTC).
Type: Timestamp
Required: Yes

 ** type **   <a name="StepFunctions-Type-HistoryEvent-type"></a>
The type of the event.
Type: String
Valid Values: `ActivityFailed | ActivityScheduled | ActivityScheduleFailed | ActivityStarted | ActivitySucceeded | ActivityTimedOut | ChoiceStateEntered | ChoiceStateExited | ExecutionAborted | ExecutionFailed | ExecutionStarted | ExecutionSucceeded | ExecutionTimedOut | FailStateEntered | LambdaFunctionFailed | LambdaFunctionScheduled | LambdaFunctionScheduleFailed | LambdaFunctionStarted | LambdaFunctionStartFailed | LambdaFunctionSucceeded | LambdaFunctionTimedOut | MapIterationAborted | MapIterationFailed | MapIterationStarted | MapIterationSucceeded | MapStateAborted | MapStateEntered | MapStateExited | MapStateFailed | MapStateStarted | MapStateSucceeded | ParallelStateAborted | ParallelStateEntered | ParallelStateExited | ParallelStateFailed | ParallelStateStarted | ParallelStateSucceeded | PassStateEntered | PassStateExited | SucceedStateEntered | SucceedStateExited | TaskFailed | TaskScheduled | TaskStarted | TaskStartFailed | TaskStateAborted | TaskStateEntered | TaskStateExited | TaskSubmitFailed | TaskSubmitted | TaskSucceeded | TaskTimedOut | WaitStateAborted | WaitStateEntered | WaitStateExited | MapRunAborted | MapRunFailed | MapRunStarted | MapRunSucceeded | ExecutionRedriven | MapRunRedriven | EvaluationFailed`
Required: Yes

 ** activityFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activityFailedEventDetails"></a>
Type: [ActivityFailedEventDetails](API_ActivityFailedEventDetails.md) object
Required: No

 ** activityScheduledEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activityScheduledEventDetails"></a>
Type: [ActivityScheduledEventDetails](API_ActivityScheduledEventDetails.md) object
Required: No

 ** activityScheduleFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activityScheduleFailedEventDetails"></a>
Contains details about an activity schedule event that failed during an execution.
Type: [ActivityScheduleFailedEventDetails](API_ActivityScheduleFailedEventDetails.md) object
Required: No

 ** activityStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activityStartedEventDetails"></a>
Type: [ActivityStartedEventDetails](API_ActivityStartedEventDetails.md) object
Required: No

 ** activitySucceededEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activitySucceededEventDetails"></a>
Type: [ActivitySucceededEventDetails](API_ActivitySucceededEventDetails.md) object
Required: No

 ** activityTimedOutEventDetails **   <a name="StepFunctions-Type-HistoryEvent-activityTimedOutEventDetails"></a>
Type: [ActivityTimedOutEventDetails](API_ActivityTimedOutEventDetails.md) object
Required: No

 ** evaluationFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-evaluationFailedEventDetails"></a>
Contains details about an evaluation failure that occurred while processing a state.
Type: [EvaluationFailedEventDetails](API_EvaluationFailedEventDetails.md) object
Required: No

 ** executionAbortedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionAbortedEventDetails"></a>
Type: [ExecutionAbortedEventDetails](API_ExecutionAbortedEventDetails.md) object
Required: No

 ** executionFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionFailedEventDetails"></a>
Type: [ExecutionFailedEventDetails](API_ExecutionFailedEventDetails.md) object
Required: No

 ** executionRedrivenEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionRedrivenEventDetails"></a>
Contains details about the redrive attempt of an execution.
Type: [ExecutionRedrivenEventDetails](API_ExecutionRedrivenEventDetails.md) object
Required: No

 ** executionStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionStartedEventDetails"></a>
Type: [ExecutionStartedEventDetails](API_ExecutionStartedEventDetails.md) object
Required: No

 ** executionSucceededEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionSucceededEventDetails"></a>
Type: [ExecutionSucceededEventDetails](API_ExecutionSucceededEventDetails.md) object
Required: No

 ** executionTimedOutEventDetails **   <a name="StepFunctions-Type-HistoryEvent-executionTimedOutEventDetails"></a>
Type: [ExecutionTimedOutEventDetails](API_ExecutionTimedOutEventDetails.md) object
Required: No

 ** lambdaFunctionFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionFailedEventDetails"></a>
Type: [LambdaFunctionFailedEventDetails](API_LambdaFunctionFailedEventDetails.md) object
Required: No

 ** lambdaFunctionScheduledEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionScheduledEventDetails"></a>
Type: [LambdaFunctionScheduledEventDetails](API_LambdaFunctionScheduledEventDetails.md) object
Required: No

 ** lambdaFunctionScheduleFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionScheduleFailedEventDetails"></a>
Type: [LambdaFunctionScheduleFailedEventDetails](API_LambdaFunctionScheduleFailedEventDetails.md) object
Required: No

 ** lambdaFunctionStartFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionStartFailedEventDetails"></a>
Contains details about a lambda function that failed to start during an execution.
Type: [LambdaFunctionStartFailedEventDetails](API_LambdaFunctionStartFailedEventDetails.md) object
Required: No

 ** lambdaFunctionSucceededEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionSucceededEventDetails"></a>
Contains details about a Lambda function that terminated successfully during an execution.
Type: [LambdaFunctionSucceededEventDetails](API_LambdaFunctionSucceededEventDetails.md) object
Required: No

 ** lambdaFunctionTimedOutEventDetails **   <a name="StepFunctions-Type-HistoryEvent-lambdaFunctionTimedOutEventDetails"></a>
Type: [LambdaFunctionTimedOutEventDetails](API_LambdaFunctionTimedOutEventDetails.md) object
Required: No

 ** mapIterationAbortedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapIterationAbortedEventDetails"></a>
Contains details about an iteration of a Map state that was aborted.
Type: [MapIterationEventDetails](API_MapIterationEventDetails.md) object
Required: No

 ** mapIterationFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapIterationFailedEventDetails"></a>
Contains details about an iteration of a Map state that failed.
Type: [MapIterationEventDetails](API_MapIterationEventDetails.md) object
Required: No

 ** mapIterationStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapIterationStartedEventDetails"></a>
Contains details about an iteration of a Map state that was started.
Type: [MapIterationEventDetails](API_MapIterationEventDetails.md) object
Required: No

 ** mapIterationSucceededEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapIterationSucceededEventDetails"></a>
Contains details about an iteration of a Map state that succeeded.
Type: [MapIterationEventDetails](API_MapIterationEventDetails.md) object
Required: No

 ** mapRunFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapRunFailedEventDetails"></a>
Contains error and cause details about a Map Run that failed.
Type: [MapRunFailedEventDetails](API_MapRunFailedEventDetails.md) object
Required: No

 ** mapRunRedrivenEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapRunRedrivenEventDetails"></a>
Contains details about the redrive attempt of a Map Run.
Type: [MapRunRedrivenEventDetails](API_MapRunRedrivenEventDetails.md) object
Required: No

 ** mapRunStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapRunStartedEventDetails"></a>
Contains details, such as `mapRunArn`, and the start date and time of a Map Run. `mapRunArn` is the Amazon Resource Name (ARN) of the Map Run that was started.
Type: [MapRunStartedEventDetails](API_MapRunStartedEventDetails.md) object
Required: No

 ** mapStateStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-mapStateStartedEventDetails"></a>
Contains details about Map state that was started.
Type: [MapStateStartedEventDetails](API_MapStateStartedEventDetails.md) object
Required: No

 ** previousEventId **   <a name="StepFunctions-Type-HistoryEvent-previousEventId"></a>
The id of the previous event.
Type: Long
Required: No

 ** stateEnteredEventDetails **   <a name="StepFunctions-Type-HistoryEvent-stateEnteredEventDetails"></a>
Type: [StateEnteredEventDetails](API_StateEnteredEventDetails.md) object
Required: No

 ** stateExitedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-stateExitedEventDetails"></a>
Type: [StateExitedEventDetails](API_StateExitedEventDetails.md) object
Required: No

 ** taskFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskFailedEventDetails"></a>
Contains details about the failure of a task.
Type: [TaskFailedEventDetails](API_TaskFailedEventDetails.md) object
Required: No

 ** taskScheduledEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskScheduledEventDetails"></a>
Contains details about a task that was scheduled.
Type: [TaskScheduledEventDetails](API_TaskScheduledEventDetails.md) object
Required: No

 ** taskStartedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskStartedEventDetails"></a>
Contains details about a task that was started.
Type: [TaskStartedEventDetails](API_TaskStartedEventDetails.md) object
Required: No

 ** taskStartFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskStartFailedEventDetails"></a>
Contains details about a task that failed to start.
Type: [TaskStartFailedEventDetails](API_TaskStartFailedEventDetails.md) object
Required: No

 ** taskSubmitFailedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskSubmitFailedEventDetails"></a>
Contains details about a task that where the submit failed.
Type: [TaskSubmitFailedEventDetails](API_TaskSubmitFailedEventDetails.md) object
Required: No

 ** taskSubmittedEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskSubmittedEventDetails"></a>
Contains details about a submitted task.
Type: [TaskSubmittedEventDetails](API_TaskSubmittedEventDetails.md) object
Required: No

 ** taskSucceededEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskSucceededEventDetails"></a>
Contains details about a task that succeeded.
Type: [TaskSucceededEventDetails](API_TaskSucceededEventDetails.md) object
Required: No

 ** taskTimedOutEventDetails **   <a name="StepFunctions-Type-HistoryEvent-taskTimedOutEventDetails"></a>
Contains details about a task that timed out.
Type: [TaskTimedOutEventDetails](API_TaskTimedOutEventDetails.md) object
Required: No

## See Also
<a name="API_HistoryEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/HistoryEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/HistoryEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/HistoryEvent)
