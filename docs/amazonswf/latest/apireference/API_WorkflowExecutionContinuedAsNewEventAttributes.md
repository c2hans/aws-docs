---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionContinuedAsNewEventAttributes.html
---

# WorkflowExecutionContinuedAsNewEventAttributes
<a name="API_WorkflowExecutionContinuedAsNewEventAttributes"></a>

Provides the details of the `WorkflowExecutionContinuedAsNew` event.

## Contents
<a name="API_WorkflowExecutionContinuedAsNewEventAttributes_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-childPolicy"></a>
The policy to use for the child workflow executions of the new execution if it is terminated by calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action explicitly or due to an expired timeout.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `ContinueAsNewWorkflowExecution` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** newExecutionRunId **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-newExecutionRunId"></a>
The `runId` of the new workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** taskList **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-taskList"></a>
The task list to use for the decisions of the new (continued) workflow execution.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-workflowType"></a>
The workflow type of this execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** executionStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-executionStartToCloseTimeout"></a>
The total duration allowed for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** input **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-input"></a>
The input provided to the new workflow execution.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** lambdaRole **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-lambdaRole"></a>
The IAM role to attach to the new (continued) workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** tagList **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-tagList"></a>
The list of tags associated with the new workflow execution.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** taskPriority **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-taskPriority"></a>
The priority of the task to use for the decisions of the new (continued) workflow execution.
Type: String
Required: No

 ** taskStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionContinuedAsNewEventAttributes-taskStartToCloseTimeout"></a>
The maximum duration of decision tasks for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_WorkflowExecutionContinuedAsNewEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionContinuedAsNewEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionContinuedAsNewEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionContinuedAsNewEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
