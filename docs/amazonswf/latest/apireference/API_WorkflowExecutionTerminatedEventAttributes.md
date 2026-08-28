---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionTerminatedEventAttributes.html
---

# WorkflowExecutionTerminatedEventAttributes
<a name="API_WorkflowExecutionTerminatedEventAttributes"></a>

Provides the details of the `WorkflowExecutionTerminated` event.

## Contents
<a name="API_WorkflowExecutionTerminatedEventAttributes_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-WorkflowExecutionTerminatedEventAttributes-childPolicy"></a>
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** cause **   <a name="SWF-Type-WorkflowExecutionTerminatedEventAttributes-cause"></a>
If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.
Type: String
Valid Values: `CHILD_POLICY_APPLIED | EVENT_LIMIT_EXCEEDED | OPERATOR_INITIATED`
Required: No

 ** details **   <a name="SWF-Type-WorkflowExecutionTerminatedEventAttributes-details"></a>
The details provided for the termination.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** reason **   <a name="SWF-Type-WorkflowExecutionTerminatedEventAttributes-reason"></a>
The reason provided for the termination.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_WorkflowExecutionTerminatedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionTerminatedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionTerminatedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionTerminatedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
