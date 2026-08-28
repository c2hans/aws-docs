---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecution.html
---

# WorkflowExecution
<a name="API_WorkflowExecution"></a>

Represents a workflow execution.

## Contents
<a name="API_WorkflowExecution_Contents"></a>

 ** runId **   <a name="SWF-Type-WorkflowExecution-runId"></a>
A system-generated unique identifier for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** workflowId **   <a name="SWF-Type-WorkflowExecution-workflowId"></a>
The user defined identifier associated with the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_WorkflowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
