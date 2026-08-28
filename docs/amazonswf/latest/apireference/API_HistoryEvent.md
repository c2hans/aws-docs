---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_HistoryEvent.html
---

# HistoryEvent
<a name="API_HistoryEvent"></a>

Event within a workflow execution. A history event can be one of these types:
+  `ActivityTaskCancelRequested` – A `RequestCancelActivityTask` decision was received by the system.
+  `ActivityTaskCanceled` – The activity task was successfully canceled.
+  `ActivityTaskCompleted` – An activity worker successfully completed an activity task by calling [RespondActivityTaskCompleted](API_RespondActivityTaskCompleted.md).
+  `ActivityTaskFailed` – An activity worker failed an activity task by calling [RespondActivityTaskFailed](API_RespondActivityTaskFailed.md).
+  `ActivityTaskScheduled` – An activity task was scheduled for execution.
+  `ActivityTaskStarted` – The scheduled activity task was dispatched to a worker.
+  `ActivityTaskTimedOut` – The activity task timed out.
+  `CancelTimerFailed` – Failed to process CancelTimer decision. This happens when the decision isn't configured properly, for example no timer exists with the specified timer Id.
+  `CancelWorkflowExecutionFailed` – A request to cancel a workflow execution failed.
+  `ChildWorkflowExecutionCanceled` – A child workflow execution, started by this workflow execution, was canceled and closed.
+  `ChildWorkflowExecutionCompleted` – A child workflow execution, started by this workflow execution, completed successfully and was closed.
+  `ChildWorkflowExecutionFailed` – A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.
+  `ChildWorkflowExecutionStarted` – A child workflow execution was successfully started.
+  `ChildWorkflowExecutionTerminated` – A child workflow execution, started by this workflow execution, was terminated.
+  `ChildWorkflowExecutionTimedOut` – A child workflow execution, started by this workflow execution, timed out and was closed.
+  `CompleteWorkflowExecutionFailed` – The workflow execution failed to complete.
+  `ContinueAsNewWorkflowExecutionFailed` – The workflow execution failed to complete after being continued as a new workflow execution.
+  `DecisionTaskCompleted` – The decider successfully completed a decision task by calling [RespondDecisionTaskCompleted](API_RespondDecisionTaskCompleted.md).
+  `DecisionTaskScheduled` – A decision task was scheduled for the workflow execution.
+  `DecisionTaskStarted` – The decision task was dispatched to a decider.
+  `DecisionTaskTimedOut` – The decision task timed out.
+  `ExternalWorkflowExecutionCancelRequested` – Request to cancel an external workflow execution was successfully delivered to the target execution.
+  `ExternalWorkflowExecutionSignaled` – A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.
+  `FailWorkflowExecutionFailed` – A request to mark a workflow execution as failed, itself failed.
+  `MarkerRecorded` – A marker was recorded in the workflow history as the result of a `RecordMarker` decision.
+  `RecordMarkerFailed` – A `RecordMarker` decision was returned as failed.
+  `RequestCancelActivityTaskFailed` – Failed to process RequestCancelActivityTask decision. This happens when the decision isn't configured properly.
+  `RequestCancelExternalWorkflowExecutionFailed` – Request to cancel an external workflow execution failed.
+  `RequestCancelExternalWorkflowExecutionInitiated` – A request was made to request the cancellation of an external workflow execution.
+  `ScheduleActivityTaskFailed` – Failed to process ScheduleActivityTask decision. This happens when the decision isn't configured properly, for example the activity type specified isn't registered.
+  `SignalExternalWorkflowExecutionFailed` – The request to signal an external workflow execution failed.
+  `SignalExternalWorkflowExecutionInitiated` – A request to signal an external workflow was made.
+  `StartActivityTaskFailed` – A scheduled activity task failed to start.
+  `StartChildWorkflowExecutionFailed` – Failed to process StartChildWorkflowExecution decision. This happens when the decision isn't configured properly, for example the workflow type specified isn't registered.
+  `StartChildWorkflowExecutionInitiated` – A request was made to start a child workflow execution.
+  `StartTimerFailed` – Failed to process StartTimer decision. This happens when the decision isn't configured properly, for example a timer already exists with the specified timer Id.
+  `TimerCanceled` – A timer, previously started for this workflow execution, was successfully canceled.
+  `TimerFired` – A timer, previously started for this workflow execution, fired.
+  `TimerStarted` – A timer was started for the workflow execution due to a `StartTimer` decision.
+  `WorkflowExecutionCancelRequested` – A request to cancel this workflow execution was made.
+  `WorkflowExecutionCanceled` – The workflow execution was successfully canceled and closed.
+  `WorkflowExecutionCompleted` – The workflow execution was closed due to successful completion.
+  `WorkflowExecutionContinuedAsNew` – The workflow execution was closed and a new execution of the same type was created with the same workflowId.
+  `WorkflowExecutionFailed` – The workflow execution closed due to a failure.
+  `WorkflowExecutionSignaled` – An external signal was received for the workflow execution.
+  `WorkflowExecutionStarted` – The workflow execution was started.
+  `WorkflowExecutionTerminated` – The workflow execution was terminated.
+  `WorkflowExecutionTimedOut` – The workflow execution was closed because a time out was exceeded.

## Contents
<a name="API_HistoryEvent_Contents"></a>

 ** eventId **   <a name="SWF-Type-HistoryEvent-eventId"></a>
The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.
Type: Long
Required: Yes

 ** eventTimestamp **   <a name="SWF-Type-HistoryEvent-eventTimestamp"></a>
The date and time when the event occurred.
Type: Timestamp
Required: Yes

 ** eventType **   <a name="SWF-Type-HistoryEvent-eventType"></a>
The type of the history event.
Type: String
Valid Values: `WorkflowExecutionStarted | WorkflowExecutionCancelRequested | WorkflowExecutionCompleted | CompleteWorkflowExecutionFailed | WorkflowExecutionFailed | FailWorkflowExecutionFailed | WorkflowExecutionTimedOut | WorkflowExecutionCanceled | CancelWorkflowExecutionFailed | WorkflowExecutionContinuedAsNew | ContinueAsNewWorkflowExecutionFailed | WorkflowExecutionTerminated | DecisionTaskScheduled | DecisionTaskStarted | DecisionTaskCompleted | DecisionTaskTimedOut | ActivityTaskScheduled | ScheduleActivityTaskFailed | ActivityTaskStarted | ActivityTaskCompleted | ActivityTaskFailed | ActivityTaskTimedOut | ActivityTaskCanceled | ActivityTaskCancelRequested | RequestCancelActivityTaskFailed | WorkflowExecutionSignaled | MarkerRecorded | RecordMarkerFailed | TimerStarted | StartTimerFailed | TimerFired | TimerCanceled | CancelTimerFailed | StartChildWorkflowExecutionInitiated | StartChildWorkflowExecutionFailed | ChildWorkflowExecutionStarted | ChildWorkflowExecutionCompleted | ChildWorkflowExecutionFailed | ChildWorkflowExecutionTimedOut | ChildWorkflowExecutionCanceled | ChildWorkflowExecutionTerminated | SignalExternalWorkflowExecutionInitiated | SignalExternalWorkflowExecutionFailed | ExternalWorkflowExecutionSignaled | RequestCancelExternalWorkflowExecutionInitiated | RequestCancelExternalWorkflowExecutionFailed | ExternalWorkflowExecutionCancelRequested | LambdaFunctionScheduled | LambdaFunctionStarted | LambdaFunctionCompleted | LambdaFunctionFailed | LambdaFunctionTimedOut | ScheduleLambdaFunctionFailed | StartLambdaFunctionFailed`
Required: Yes

 ** activityTaskCanceledEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskCanceledEventAttributes"></a>
If the event is of type `ActivityTaskCanceled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskCanceledEventAttributes](API_ActivityTaskCanceledEventAttributes.md) object
Required: No

 ** activityTaskCancelRequestedEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskCancelRequestedEventAttributes"></a>
If the event is of type `ActivityTaskcancelRequested` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskCancelRequestedEventAttributes](API_ActivityTaskCancelRequestedEventAttributes.md) object
Required: No

 ** activityTaskCompletedEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskCompletedEventAttributes"></a>
If the event is of type `ActivityTaskCompleted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskCompletedEventAttributes](API_ActivityTaskCompletedEventAttributes.md) object
Required: No

 ** activityTaskFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskFailedEventAttributes"></a>
If the event is of type `ActivityTaskFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskFailedEventAttributes](API_ActivityTaskFailedEventAttributes.md) object
Required: No

 ** activityTaskScheduledEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskScheduledEventAttributes"></a>
If the event is of type `ActivityTaskScheduled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskScheduledEventAttributes](API_ActivityTaskScheduledEventAttributes.md) object
Required: No

 ** activityTaskStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskStartedEventAttributes"></a>
If the event is of type `ActivityTaskStarted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskStartedEventAttributes](API_ActivityTaskStartedEventAttributes.md) object
Required: No

 ** activityTaskTimedOutEventAttributes **   <a name="SWF-Type-HistoryEvent-activityTaskTimedOutEventAttributes"></a>
If the event is of type `ActivityTaskTimedOut` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ActivityTaskTimedOutEventAttributes](API_ActivityTaskTimedOutEventAttributes.md) object
Required: No

 ** cancelTimerFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-cancelTimerFailedEventAttributes"></a>
If the event is of type `CancelTimerFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [CancelTimerFailedEventAttributes](API_CancelTimerFailedEventAttributes.md) object
Required: No

 ** cancelWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-cancelWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `CancelWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [CancelWorkflowExecutionFailedEventAttributes](API_CancelWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** childWorkflowExecutionCanceledEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionCanceledEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionCanceled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionCanceledEventAttributes](API_ChildWorkflowExecutionCanceledEventAttributes.md) object
Required: No

 ** childWorkflowExecutionCompletedEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionCompletedEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionCompleted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionCompletedEventAttributes](API_ChildWorkflowExecutionCompletedEventAttributes.md) object
Required: No

 ** childWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionFailedEventAttributes](API_ChildWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** childWorkflowExecutionStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionStartedEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionStarted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionStartedEventAttributes](API_ChildWorkflowExecutionStartedEventAttributes.md) object
Required: No

 ** childWorkflowExecutionTerminatedEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionTerminatedEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionTerminated` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionTerminatedEventAttributes](API_ChildWorkflowExecutionTerminatedEventAttributes.md) object
Required: No

 ** childWorkflowExecutionTimedOutEventAttributes **   <a name="SWF-Type-HistoryEvent-childWorkflowExecutionTimedOutEventAttributes"></a>
If the event is of type `ChildWorkflowExecutionTimedOut` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ChildWorkflowExecutionTimedOutEventAttributes](API_ChildWorkflowExecutionTimedOutEventAttributes.md) object
Required: No

 ** completeWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-completeWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `CompleteWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [CompleteWorkflowExecutionFailedEventAttributes](API_CompleteWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** continueAsNewWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-continueAsNewWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `ContinueAsNewWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ContinueAsNewWorkflowExecutionFailedEventAttributes](API_ContinueAsNewWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** decisionTaskCompletedEventAttributes **   <a name="SWF-Type-HistoryEvent-decisionTaskCompletedEventAttributes"></a>
If the event is of type `DecisionTaskCompleted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [DecisionTaskCompletedEventAttributes](API_DecisionTaskCompletedEventAttributes.md) object
Required: No

 ** decisionTaskScheduledEventAttributes **   <a name="SWF-Type-HistoryEvent-decisionTaskScheduledEventAttributes"></a>
If the event is of type `DecisionTaskScheduled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [DecisionTaskScheduledEventAttributes](API_DecisionTaskScheduledEventAttributes.md) object
Required: No

 ** decisionTaskStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-decisionTaskStartedEventAttributes"></a>
If the event is of type `DecisionTaskStarted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [DecisionTaskStartedEventAttributes](API_DecisionTaskStartedEventAttributes.md) object
Required: No

 ** decisionTaskTimedOutEventAttributes **   <a name="SWF-Type-HistoryEvent-decisionTaskTimedOutEventAttributes"></a>
If the event is of type `DecisionTaskTimedOut` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [DecisionTaskTimedOutEventAttributes](API_DecisionTaskTimedOutEventAttributes.md) object
Required: No

 ** externalWorkflowExecutionCancelRequestedEventAttributes **   <a name="SWF-Type-HistoryEvent-externalWorkflowExecutionCancelRequestedEventAttributes"></a>
If the event is of type `ExternalWorkflowExecutionCancelRequested` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ExternalWorkflowExecutionCancelRequestedEventAttributes](API_ExternalWorkflowExecutionCancelRequestedEventAttributes.md) object
Required: No

 ** externalWorkflowExecutionSignaledEventAttributes **   <a name="SWF-Type-HistoryEvent-externalWorkflowExecutionSignaledEventAttributes"></a>
If the event is of type `ExternalWorkflowExecutionSignaled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ExternalWorkflowExecutionSignaledEventAttributes](API_ExternalWorkflowExecutionSignaledEventAttributes.md) object
Required: No

 ** failWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-failWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `FailWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [FailWorkflowExecutionFailedEventAttributes](API_FailWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** lambdaFunctionCompletedEventAttributes **   <a name="SWF-Type-HistoryEvent-lambdaFunctionCompletedEventAttributes"></a>
Provides the details of the `LambdaFunctionCompleted` event. It isn't set for other event types.
Type: [LambdaFunctionCompletedEventAttributes](API_LambdaFunctionCompletedEventAttributes.md) object
Required: No

 ** lambdaFunctionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-lambdaFunctionFailedEventAttributes"></a>
Provides the details of the `LambdaFunctionFailed` event. It isn't set for other event types.
Type: [LambdaFunctionFailedEventAttributes](API_LambdaFunctionFailedEventAttributes.md) object
Required: No

 ** lambdaFunctionScheduledEventAttributes **   <a name="SWF-Type-HistoryEvent-lambdaFunctionScheduledEventAttributes"></a>
Provides the details of the `LambdaFunctionScheduled` event. It isn't set for other event types.
Type: [LambdaFunctionScheduledEventAttributes](API_LambdaFunctionScheduledEventAttributes.md) object
Required: No

 ** lambdaFunctionStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-lambdaFunctionStartedEventAttributes"></a>
Provides the details of the `LambdaFunctionStarted` event. It isn't set for other event types.
Type: [LambdaFunctionStartedEventAttributes](API_LambdaFunctionStartedEventAttributes.md) object
Required: No

 ** lambdaFunctionTimedOutEventAttributes **   <a name="SWF-Type-HistoryEvent-lambdaFunctionTimedOutEventAttributes"></a>
Provides the details of the `LambdaFunctionTimedOut` event. It isn't set for other event types.
Type: [LambdaFunctionTimedOutEventAttributes](API_LambdaFunctionTimedOutEventAttributes.md) object
Required: No

 ** markerRecordedEventAttributes **   <a name="SWF-Type-HistoryEvent-markerRecordedEventAttributes"></a>
If the event is of type `MarkerRecorded` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [MarkerRecordedEventAttributes](API_MarkerRecordedEventAttributes.md) object
Required: No

 ** recordMarkerFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-recordMarkerFailedEventAttributes"></a>
If the event is of type `DecisionTaskFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [RecordMarkerFailedEventAttributes](API_RecordMarkerFailedEventAttributes.md) object
Required: No

 ** requestCancelActivityTaskFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-requestCancelActivityTaskFailedEventAttributes"></a>
If the event is of type `RequestCancelActivityTaskFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [RequestCancelActivityTaskFailedEventAttributes](API_RequestCancelActivityTaskFailedEventAttributes.md) object
Required: No

 ** requestCancelExternalWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-requestCancelExternalWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `RequestCancelExternalWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [RequestCancelExternalWorkflowExecutionFailedEventAttributes](API_RequestCancelExternalWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** requestCancelExternalWorkflowExecutionInitiatedEventAttributes **   <a name="SWF-Type-HistoryEvent-requestCancelExternalWorkflowExecutionInitiatedEventAttributes"></a>
If the event is of type `RequestCancelExternalWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [RequestCancelExternalWorkflowExecutionInitiatedEventAttributes](API_RequestCancelExternalWorkflowExecutionInitiatedEventAttributes.md) object
Required: No

 ** scheduleActivityTaskFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-scheduleActivityTaskFailedEventAttributes"></a>
If the event is of type `ScheduleActivityTaskFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [ScheduleActivityTaskFailedEventAttributes](API_ScheduleActivityTaskFailedEventAttributes.md) object
Required: No

 ** scheduleLambdaFunctionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-scheduleLambdaFunctionFailedEventAttributes"></a>
Provides the details of the `ScheduleLambdaFunctionFailed` event. It isn't set for other event types.
Type: [ScheduleLambdaFunctionFailedEventAttributes](API_ScheduleLambdaFunctionFailedEventAttributes.md) object
Required: No

 ** signalExternalWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-signalExternalWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `SignalExternalWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [SignalExternalWorkflowExecutionFailedEventAttributes](API_SignalExternalWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** signalExternalWorkflowExecutionInitiatedEventAttributes **   <a name="SWF-Type-HistoryEvent-signalExternalWorkflowExecutionInitiatedEventAttributes"></a>
If the event is of type `SignalExternalWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [SignalExternalWorkflowExecutionInitiatedEventAttributes](API_SignalExternalWorkflowExecutionInitiatedEventAttributes.md) object
Required: No

 ** startChildWorkflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-startChildWorkflowExecutionFailedEventAttributes"></a>
If the event is of type `StartChildWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [StartChildWorkflowExecutionFailedEventAttributes](API_StartChildWorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** startChildWorkflowExecutionInitiatedEventAttributes **   <a name="SWF-Type-HistoryEvent-startChildWorkflowExecutionInitiatedEventAttributes"></a>
If the event is of type `StartChildWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [StartChildWorkflowExecutionInitiatedEventAttributes](API_StartChildWorkflowExecutionInitiatedEventAttributes.md) object
Required: No

 ** startLambdaFunctionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-startLambdaFunctionFailedEventAttributes"></a>
Provides the details of the `StartLambdaFunctionFailed` event. It isn't set for other event types.
Type: [StartLambdaFunctionFailedEventAttributes](API_StartLambdaFunctionFailedEventAttributes.md) object
Required: No

 ** startTimerFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-startTimerFailedEventAttributes"></a>
If the event is of type `StartTimerFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [StartTimerFailedEventAttributes](API_StartTimerFailedEventAttributes.md) object
Required: No

 ** timerCanceledEventAttributes **   <a name="SWF-Type-HistoryEvent-timerCanceledEventAttributes"></a>
If the event is of type `TimerCanceled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [TimerCanceledEventAttributes](API_TimerCanceledEventAttributes.md) object
Required: No

 ** timerFiredEventAttributes **   <a name="SWF-Type-HistoryEvent-timerFiredEventAttributes"></a>
If the event is of type `TimerFired` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [TimerFiredEventAttributes](API_TimerFiredEventAttributes.md) object
Required: No

 ** timerStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-timerStartedEventAttributes"></a>
If the event is of type `TimerStarted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [TimerStartedEventAttributes](API_TimerStartedEventAttributes.md) object
Required: No

 ** workflowExecutionCanceledEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionCanceledEventAttributes"></a>
If the event is of type `WorkflowExecutionCanceled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionCanceledEventAttributes](API_WorkflowExecutionCanceledEventAttributes.md) object
Required: No

 ** workflowExecutionCancelRequestedEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionCancelRequestedEventAttributes"></a>
If the event is of type `WorkflowExecutionCancelRequested` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionCancelRequestedEventAttributes](API_WorkflowExecutionCancelRequestedEventAttributes.md) object
Required: No

 ** workflowExecutionCompletedEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionCompletedEventAttributes"></a>
If the event is of type `WorkflowExecutionCompleted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionCompletedEventAttributes](API_WorkflowExecutionCompletedEventAttributes.md) object
Required: No

 ** workflowExecutionContinuedAsNewEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionContinuedAsNewEventAttributes"></a>
If the event is of type `WorkflowExecutionContinuedAsNew` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionContinuedAsNewEventAttributes](API_WorkflowExecutionContinuedAsNewEventAttributes.md) object
Required: No

 ** workflowExecutionFailedEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionFailedEventAttributes"></a>
If the event is of type `WorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionFailedEventAttributes](API_WorkflowExecutionFailedEventAttributes.md) object
Required: No

 ** workflowExecutionSignaledEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionSignaledEventAttributes"></a>
If the event is of type `WorkflowExecutionSignaled` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionSignaledEventAttributes](API_WorkflowExecutionSignaledEventAttributes.md) object
Required: No

 ** workflowExecutionStartedEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionStartedEventAttributes"></a>
If the event is of type `WorkflowExecutionStarted` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionStartedEventAttributes](API_WorkflowExecutionStartedEventAttributes.md) object
Required: No

 ** workflowExecutionTerminatedEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionTerminatedEventAttributes"></a>
If the event is of type `WorkflowExecutionTerminated` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionTerminatedEventAttributes](API_WorkflowExecutionTerminatedEventAttributes.md) object
Required: No

 ** workflowExecutionTimedOutEventAttributes **   <a name="SWF-Type-HistoryEvent-workflowExecutionTimedOutEventAttributes"></a>
If the event is of type `WorkflowExecutionTimedOut` then this member is set and provides detailed information about the event. It isn't set for other event types.
Type: [WorkflowExecutionTimedOutEventAttributes](API_WorkflowExecutionTimedOutEventAttributes.md) object
Required: No

## See Also
<a name="API_HistoryEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/HistoryEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/HistoryEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/HistoryEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
