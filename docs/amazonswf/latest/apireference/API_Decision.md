---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html
---

# Decision
<a name="API_Decision"></a>

Specifies a decision made by the decider. A decision can be one of these types:
+  `CancelTimer` – Cancels a previously started timer and records a `TimerCanceled` event in the history.
+  `CancelWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionCanceled` event in the history.
+  `CompleteWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionCompleted` event in the history .
+  `ContinueAsNewWorkflowExecution` – Closes the workflow execution and starts a new workflow execution of the same type using the same workflow ID and a unique run Id. A `WorkflowExecutionContinuedAsNew` event is recorded in the history.
+  `FailWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionFailed` event in the history.
+  `RecordMarker` – Records a `MarkerRecorded` event in the history. Markers can be used for adding custom information in the history for instance to let deciders know that they don't need to look at the history beyond the marker event.
+  `RequestCancelActivityTask` – Attempts to cancel a previously scheduled activity task. If the activity task was scheduled but has not been assigned to a worker, then it is canceled. If the activity task was already assigned to a worker, then the worker is informed that cancellation has been requested in the response to [RecordActivityTaskHeartbeat](API_RecordActivityTaskHeartbeat.md).
+  `RequestCancelExternalWorkflowExecution` – Requests that a request be made to cancel the specified external workflow execution and records a `RequestCancelExternalWorkflowExecutionInitiated` event in the history.
+  `ScheduleActivityTask` – Schedules an activity task.
+  `SignalExternalWorkflowExecution` – Requests a signal to be delivered to the specified external workflow execution and records a `SignalExternalWorkflowExecutionInitiated` event in the history.
+  `StartChildWorkflowExecution` – Requests that a child workflow execution be started and records a `StartChildWorkflowExecutionInitiated` event in the history. The child workflow execution is a separate workflow execution with its own history.
+  `StartTimer` – Starts a timer for this workflow execution and records a `TimerStarted` event in the history. This timer fires after the specified delay and record a `TimerFired` event.

 **Access Control**

If you grant permission to use `RespondDecisionTaskCompleted`, you can use IAM policies to express permissions for the list of decisions returned by this action as if they were members of the API. Treating decisions as a pseudo API maintains a uniform conceptual model and helps keep policies readable. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

 **Decision Failure**

Decisions can fail for several reasons
+ The ordering of decisions should follow a logical flow. Some decisions might not make sense in the current context of the workflow execution and therefore fails.
+ A limit on your account was reached.
+ The decision lacks sufficient permissions.

One of the following events might be added to the history to indicate an error. The event attribute's `cause` parameter indicates the cause. If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.
+  `ScheduleActivityTaskFailed` – A `ScheduleActivityTask` decision failed. This could happen if the activity type specified in the decision isn't registered, is in a deprecated state, or the decision isn't properly configured.
+  `RequestCancelActivityTaskFailed` – A `RequestCancelActivityTask` decision failed. This could happen if there is no open activity task with the specified activityId.
+  `StartTimerFailed` – A `StartTimer` decision failed. This could happen if there is another open timer with the same timerId.
+  `CancelTimerFailed` – A `CancelTimer` decision failed. This could happen if there is no open timer with the specified timerId.
+  `StartChildWorkflowExecutionFailed` – A `StartChildWorkflowExecution` decision failed. This could happen if the workflow type specified isn't registered, is deprecated, or the decision isn't properly configured.
+  `SignalExternalWorkflowExecutionFailed` – A `SignalExternalWorkflowExecution` decision failed. This could happen if the `workflowID` specified in the decision was incorrect.
+  `RequestCancelExternalWorkflowExecutionFailed` – A `RequestCancelExternalWorkflowExecution` decision failed. This could happen if the `workflowID` specified in the decision was incorrect.
+  `CancelWorkflowExecutionFailed` – A `CancelWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.
+  `CompleteWorkflowExecutionFailed` – A `CompleteWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.
+  `ContinueAsNewWorkflowExecutionFailed` – A `ContinueAsNewWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution or the ContinueAsNewWorkflowExecution decision was not configured correctly.
+  `FailWorkflowExecutionFailed` – A `FailWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.

The preceding error events might occur due to an error in the decider logic, which might put the workflow execution in an unstable state The cause field in the event structure for the error event indicates the cause of the error.

**Note**
A workflow execution may be closed by the decider by returning one of the following decisions when completing a decision task: `CompleteWorkflowExecution`, `FailWorkflowExecution`, `CancelWorkflowExecution` and `ContinueAsNewWorkflowExecution`. An `UnhandledDecision` fault is returned if a workflow closing decision is specified and a signal or activity event had been added to the history while the decision task was being performed by the decider. Unlike the above situations which are logic issues, this fault is always possible because of race conditions in a distributed system. The right action here is to call [RespondDecisionTaskCompleted](API_RespondDecisionTaskCompleted.md) without any decisions. This would result in another decision task with these new events included in the history. The decider should handle the new events and may decide to close the workflow execution.

 **How to Code a Decision**

You code a decision by first setting the decision type field to one of the above decision values, and then set the corresponding attributes field shown below:
+  ` ScheduleActivityTaskDecisionAttributes `
+  ` RequestCancelActivityTaskDecisionAttributes `
+  ` CompleteWorkflowExecutionDecisionAttributes `
+  ` FailWorkflowExecutionDecisionAttributes `
+  ` CancelWorkflowExecutionDecisionAttributes `
+  ` ContinueAsNewWorkflowExecutionDecisionAttributes `
+  ` RecordMarkerDecisionAttributes `
+  ` StartTimerDecisionAttributes `
+  ` CancelTimerDecisionAttributes `
+  ` SignalExternalWorkflowExecutionDecisionAttributes `
+  ` RequestCancelExternalWorkflowExecutionDecisionAttributes `
+  ` StartChildWorkflowExecutionDecisionAttributes `

## Contents
<a name="API_Decision_Contents"></a>

 ** decisionType **   <a name="SWF-Type-Decision-decisionType"></a>
Specifies the type of the decision.
Type: String
Valid Values: `ScheduleActivityTask | RequestCancelActivityTask | CompleteWorkflowExecution | FailWorkflowExecution | CancelWorkflowExecution | ContinueAsNewWorkflowExecution | RecordMarker | StartTimer | CancelTimer | SignalExternalWorkflowExecution | RequestCancelExternalWorkflowExecution | StartChildWorkflowExecution | ScheduleLambdaFunction`
Required: Yes

 ** cancelTimerDecisionAttributes **   <a name="SWF-Type-Decision-cancelTimerDecisionAttributes"></a>
Provides the details of the `CancelTimer` decision. It isn't set for other decision types.
Type: [CancelTimerDecisionAttributes](API_CancelTimerDecisionAttributes.md) object
Required: No

 ** cancelWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-cancelWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `CancelWorkflowExecution` decision. It isn't set for other decision types.
Type: [CancelWorkflowExecutionDecisionAttributes](API_CancelWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** completeWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-completeWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `CompleteWorkflowExecution` decision. It isn't set for other decision types.
Type: [CompleteWorkflowExecutionDecisionAttributes](API_CompleteWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** continueAsNewWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-continueAsNewWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `ContinueAsNewWorkflowExecution` decision. It isn't set for other decision types.
Type: [ContinueAsNewWorkflowExecutionDecisionAttributes](API_ContinueAsNewWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** failWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-failWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `FailWorkflowExecution` decision. It isn't set for other decision types.
Type: [FailWorkflowExecutionDecisionAttributes](API_FailWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** recordMarkerDecisionAttributes **   <a name="SWF-Type-Decision-recordMarkerDecisionAttributes"></a>
Provides the details of the `RecordMarker` decision. It isn't set for other decision types.
Type: [RecordMarkerDecisionAttributes](API_RecordMarkerDecisionAttributes.md) object
Required: No

 ** requestCancelActivityTaskDecisionAttributes **   <a name="SWF-Type-Decision-requestCancelActivityTaskDecisionAttributes"></a>
Provides the details of the `RequestCancelActivityTask` decision. It isn't set for other decision types.
Type: [RequestCancelActivityTaskDecisionAttributes](API_RequestCancelActivityTaskDecisionAttributes.md) object
Required: No

 ** requestCancelExternalWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-requestCancelExternalWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `RequestCancelExternalWorkflowExecution` decision. It isn't set for other decision types.
Type: [RequestCancelExternalWorkflowExecutionDecisionAttributes](API_RequestCancelExternalWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** scheduleActivityTaskDecisionAttributes **   <a name="SWF-Type-Decision-scheduleActivityTaskDecisionAttributes"></a>
Provides the details of the `ScheduleActivityTask` decision. It isn't set for other decision types.
Type: [ScheduleActivityTaskDecisionAttributes](API_ScheduleActivityTaskDecisionAttributes.md) object
Required: No

 ** scheduleLambdaFunctionDecisionAttributes **   <a name="SWF-Type-Decision-scheduleLambdaFunctionDecisionAttributes"></a>
Provides the details of the `ScheduleLambdaFunction` decision. It isn't set for other decision types.
Type: [ScheduleLambdaFunctionDecisionAttributes](API_ScheduleLambdaFunctionDecisionAttributes.md) object
Required: No

 ** signalExternalWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-signalExternalWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `SignalExternalWorkflowExecution` decision. It isn't set for other decision types.
Type: [SignalExternalWorkflowExecutionDecisionAttributes](API_SignalExternalWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** startChildWorkflowExecutionDecisionAttributes **   <a name="SWF-Type-Decision-startChildWorkflowExecutionDecisionAttributes"></a>
Provides the details of the `StartChildWorkflowExecution` decision. It isn't set for other decision types.
Type: [StartChildWorkflowExecutionDecisionAttributes](API_StartChildWorkflowExecutionDecisionAttributes.md) object
Required: No

 ** startTimerDecisionAttributes **   <a name="SWF-Type-Decision-startTimerDecisionAttributes"></a>
Provides the details of the `StartTimer` decision. It isn't set for other decision types.
Type: [StartTimerDecisionAttributes](API_StartTimerDecisionAttributes.md) object
Required: No

## See Also
<a name="API_Decision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/Decision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/Decision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/Decision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
