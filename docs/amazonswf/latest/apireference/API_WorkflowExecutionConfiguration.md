---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionConfiguration.html
---

# WorkflowExecutionConfiguration
<a name="API_WorkflowExecutionConfiguration"></a>

The configuration settings for a workflow execution including timeout values, tasklist etc. These configuration settings are determined from the defaults specified when registering the workflow type and those specified when starting the workflow execution.

## Contents
<a name="API_WorkflowExecutionConfiguration_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-WorkflowExecutionConfiguration-childPolicy"></a>
The policy to use for the child workflow executions if this workflow execution is terminated, by calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action explicitly or due to an expired timeout.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** executionStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionConfiguration-executionStartToCloseTimeout"></a>
The total duration for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: Yes

 ** taskList **   <a name="SWF-Type-WorkflowExecutionConfiguration-taskList"></a>
The task list used for the decision tasks generated for this workflow execution.
Type: [TaskList](API_TaskList.md) object
Required: Yes

 ** taskStartToCloseTimeout **   <a name="SWF-Type-WorkflowExecutionConfiguration-taskStartToCloseTimeout"></a>
The maximum duration allowed for decision tasks for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: Yes

 ** lambdaRole **   <a name="SWF-Type-WorkflowExecutionConfiguration-lambdaRole"></a>
The IAM role attached to the child workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** taskPriority **   <a name="SWF-Type-WorkflowExecutionConfiguration-taskPriority"></a>
The priority assigned to decision tasks for this workflow execution. Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_WorkflowExecutionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionConfiguration)
