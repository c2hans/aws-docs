---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartChildWorkflowExecutionInitiatedEventAttributes.html
---

# StartChildWorkflowExecutionInitiatedEventAttributes
<a name="API_StartChildWorkflowExecutionInitiatedEventAttributes"></a>

Provides the details of the `StartChildWorkflowExecutionInitiated` event.

## Contents
<a name="API_StartChildWorkflowExecutionInitiatedEventAttributes_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-childPolicy"></a>
The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action or due to an expired timeout.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartChildWorkflowExecution` [Decision](API_Decision.md) to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.
Type: Long
Required: Yes

 ** taskList **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-taskList"></a>
The name of the task list used for the decision tasks of the child workflow execution.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** workflowId **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-workflowId"></a>
The `workflowId` of the child workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** workflowType **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-workflowType"></a>
The type of the child workflow execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** control **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn't sent to the activity.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** executionStartToCloseTimeout **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-executionStartToCloseTimeout"></a>
The maximum duration for the child workflow execution. If the workflow execution isn't closed within this duration, it is timed out and force-terminated.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** input **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-input"></a>
The inputs provided to the child workflow execution.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** lambdaRole **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-lambdaRole"></a>
The IAM role to attach to the child workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** tagList **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-tagList"></a>
The list of tags to associated with the child workflow execution.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** taskPriority **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-taskPriority"></a>
 The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

 ** taskStartToCloseTimeout **   <a name="SWF-Type-StartChildWorkflowExecutionInitiatedEventAttributes-taskStartToCloseTimeout"></a>
The maximum duration allowed for the decision tasks for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_StartChildWorkflowExecutionInitiatedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/StartChildWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/StartChildWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/StartChildWorkflowExecutionInitiatedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
