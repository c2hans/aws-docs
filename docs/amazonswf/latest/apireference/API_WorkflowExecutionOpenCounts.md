---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionOpenCounts.html
---

# WorkflowExecutionOpenCounts
<a name="API_WorkflowExecutionOpenCounts"></a>

Contains the counts of open tasks, child workflow executions and timers for a workflow execution.

## Contents
<a name="API_WorkflowExecutionOpenCounts_Contents"></a>

 ** openActivityTasks **   <a name="SWF-Type-WorkflowExecutionOpenCounts-openActivityTasks"></a>
The count of activity tasks whose status is `OPEN`.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** openChildWorkflowExecutions **   <a name="SWF-Type-WorkflowExecutionOpenCounts-openChildWorkflowExecutions"></a>
The count of child workflow executions whose status is `OPEN`.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** openDecisionTasks **   <a name="SWF-Type-WorkflowExecutionOpenCounts-openDecisionTasks"></a>
The count of decision tasks whose status is OPEN. A workflow execution can have at most one open decision task.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** openTimers **   <a name="SWF-Type-WorkflowExecutionOpenCounts-openTimers"></a>
The count of timers started by this workflow execution that have not fired yet.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** openLambdaFunctions **   <a name="SWF-Type-WorkflowExecutionOpenCounts-openLambdaFunctions"></a>
The count of Lambda tasks whose status is `OPEN`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_WorkflowExecutionOpenCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionOpenCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionOpenCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionOpenCounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
