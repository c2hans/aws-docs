---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowTypeConfiguration.html
---

# WorkflowTypeConfiguration
<a name="API_WorkflowTypeConfiguration"></a>

The configuration settings of a workflow type.

## Contents
<a name="API_WorkflowTypeConfiguration_Contents"></a>

 ** defaultChildPolicy **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultChildPolicy"></a>
 The default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the [StartWorkflowExecution](API_StartWorkflowExecution.md) action or the `StartChildWorkflowExecution` [Decision](API_Decision.md).
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: No

 ** defaultExecutionStartToCloseTimeout **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultExecutionStartToCloseTimeout"></a>
 The default maximum duration, specified when registering the workflow type, for executions of this workflow type. This default can be overridden when starting a workflow execution using the [StartWorkflowExecution](API_StartWorkflowExecution.md) action or the `StartChildWorkflowExecution` [Decision](API_Decision.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** defaultLambdaRole **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultLambdaRole"></a>
The default IAM role attached to this workflow type.
Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't specify an IAM role when starting this workflow type, the default Lambda role is attached to the execution. For more information, see [https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** defaultTaskList **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultTaskList"></a>
 The default task list, specified when registering the workflow type, for decisions tasks scheduled for workflow executions of this type. This default can be overridden when starting a workflow execution using the [StartWorkflowExecution](API_StartWorkflowExecution.md) action or the `StartChildWorkflowExecution` [Decision](API_Decision.md).
Type: [TaskList](API_TaskList.md) object
Required: No

 ** defaultTaskPriority **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultTaskPriority"></a>
 The default task priority, specified when registering the workflow type, for all decision tasks of this workflow type. This default can be overridden when starting a workflow execution using the [StartWorkflowExecution](API_StartWorkflowExecution.md) action or the `StartChildWorkflowExecution` decision.
Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

 ** defaultTaskStartToCloseTimeout **   <a name="SWF-Type-WorkflowTypeConfiguration-defaultTaskStartToCloseTimeout"></a>
 The default maximum duration, specified when registering the workflow type, that a decision task for executions of this workflow type might take before returning completion or failure. If the task doesn'tdo close in the specified time then the task is automatically timed out and rescheduled. If the decider eventually reports a completion or failure, it is ignored. This default can be overridden when starting a workflow execution using the [StartWorkflowExecution](API_StartWorkflowExecution.md) action or the `StartChildWorkflowExecution` [Decision](API_Decision.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_WorkflowTypeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowTypeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowTypeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowTypeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
