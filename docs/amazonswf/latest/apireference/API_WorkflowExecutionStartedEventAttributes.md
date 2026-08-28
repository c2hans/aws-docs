---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionStartedEventAttributes.html
---

# WorkflowExecutionStartedEventAttributes
<a name="API_WorkflowExecutionStartedEventAttributes"></a>

Provides details of `WorkflowExecutionStarted` event.

## Contents
<a name="API_WorkflowExecutionStartedEventAttributes_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-childPolicy"></a>
The policy to use for the child workflow executions if this workflow execution is terminated, by calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action explicitly or due to an expired timeout.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** taskList **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-taskList"></a>
The name of the task list for scheduling the decision tasks for this workflow execution.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-workflowType"></a>
The workflow type of this execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** continuedExecutionRunId **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-continuedExecutionRunId"></a>
If this workflow execution was started due to a `ContinueAsNewWorkflowExecution` decision, then it contains the `runId` of the previous workflow execution that was closed and continued as this execution.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** executionStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-executionStartToCloseTimeout"></a>
The maximum duration for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** input **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-input"></a>
The input provided to the workflow execution.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** lambdaRole **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-lambdaRole"></a>
The IAM role attached to the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** parentInitiatedEventId **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-parentInitiatedEventId"></a>
The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution` [Decision](API_Decision.md) to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: No

 ** parentWorkflowExecution **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-parentWorkflowExecution"></a>
The source workflow execution that started this workflow execution. The member isn't set if the workflow execution was not started by a workflow.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: No

 ** tagList **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-tagList"></a>
The list of tags associated with this workflow execution. An execution can have up to 5 tags.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** taskPriority **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-taskPriority"></a>
The priority of the decision tasks in the workflow execution.
Type: String
Required: No

 ** taskStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionStartedEventAttributes-taskStartToCloseTimeout"></a>
The maximum duration of decision tasks for this workflow type.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_WorkflowExecutionStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionStartedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
