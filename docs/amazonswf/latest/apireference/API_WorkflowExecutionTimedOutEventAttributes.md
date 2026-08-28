---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionTimedOutEventAttributes.html
---

# WorkflowExecutionTimedOutEventAttributes
<a name="API_WorkflowExecutionTimedOutEventAttributes"></a>

Provides the details of the `WorkflowExecutionTimedOut` event.

## Contents
<a name="API_WorkflowExecutionTimedOutEventAttributes_Contents"></a>

 ** childPolicy **   <a name="SWF-Type-WorkflowExecutionTimedOutEventAttributes-childPolicy"></a>
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: Yes

 ** timeoutType **   <a name="SWF-Type-WorkflowExecutionTimedOutEventAttributes-timeoutType"></a>
The type of timeout that caused this event.
Type: String
Valid Values: `START_TO_CLOSE`
Required: Yes

## See Also
<a name="API_WorkflowExecutionTimedOutEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionTimedOutEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionTimedOutEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionTimedOutEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
