---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionInfo.html
---

# WorkflowExecutionInfo
<a name="API_WorkflowExecutionInfo"></a>

Contains information about a workflow execution.

## Contents
<a name="API_WorkflowExecutionInfo_Contents"></a>

 ** execution **   <a name="SWF-Type-WorkflowExecutionInfo-execution"></a>
The workflow execution this information is about.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** executionStatus **   <a name="SWF-Type-WorkflowExecutionInfo-executionStatus"></a>
The current status of the execution.
Type: String
Valid Values: `OPEN | CLOSED`
Required: Yes

 ** startTimestamp **   <a name="SWF-Type-WorkflowExecutionInfo-startTimestamp"></a>
The time when the execution was started.
Type: Timestamp
Required: Yes

 ** workflowType **   <a name="SWF-Type-WorkflowExecutionInfo-workflowType"></a>
The type of the workflow execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** cancelRequested **   <a name="SWF-Type-WorkflowExecutionInfo-cancelRequested"></a>
Set to true if a cancellation is requested for this workflow execution.
Type: Boolean
Required: No

 ** closeStatus **   <a name="SWF-Type-WorkflowExecutionInfo-closeStatus"></a>
If the execution status is closed then this specifies how the execution was closed:
+  `COMPLETED` – the execution was successfully completed.
+  `CANCELED` – the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.
+  `TERMINATED` – the execution was force terminated.
+  `FAILED` – the execution failed to complete.
+  `TIMED_OUT` – the execution did not complete in the alloted time and was automatically timed out.
+  `CONTINUED_AS_NEW` – the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.
Type: String
Valid Values: `COMPLETED | FAILED | CANCELED | TERMINATED | CONTINUED_AS_NEW | TIMED_OUT`
Required: No

 ** closeTimestamp **   <a name="SWF-Type-WorkflowExecutionInfo-closeTimestamp"></a>
The time when the workflow execution was closed. Set only if the execution status is CLOSED.
Type: Timestamp
Required: No

 ** parent **   <a name="SWF-Type-WorkflowExecutionInfo-parent"></a>
If this workflow execution is a child of another execution then contains the workflow execution that started this execution.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: No

 ** tagList **   <a name="SWF-Type-WorkflowExecutionInfo-tagList"></a>
The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_WorkflowExecutionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
