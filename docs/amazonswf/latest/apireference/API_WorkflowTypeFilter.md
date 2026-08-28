---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowTypeFilter.html
---

# WorkflowTypeFilter
<a name="API_WorkflowTypeFilter"></a>

Used to filter workflow execution query results by type. Each parameter, if specified, defines a rule that must be satisfied by each returned result.

## Contents
<a name="API_WorkflowTypeFilter_Contents"></a>

 ** name **   <a name="SWF-Type-WorkflowTypeFilter-name"></a>
 Name of the workflow type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** version **   <a name="SWF-Type-WorkflowTypeFilter-version"></a>
Version of the workflow type.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_WorkflowTypeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowTypeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowTypeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowTypeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
