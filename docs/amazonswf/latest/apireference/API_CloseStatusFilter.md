---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CloseStatusFilter.html
---

# CloseStatusFilter
<a name="API_CloseStatusFilter"></a>

Used to filter the closed workflow executions in visibility APIs by their close status.

## Contents
<a name="API_CloseStatusFilter_Contents"></a>

 ** status **   <a name="SWF-Type-CloseStatusFilter-status"></a>
 The close status that must match the close status of an execution for it to meet the criteria of this filter.
Type: String
Valid Values: `COMPLETED | FAILED | CANCELED | TERMINATED | CONTINUED_AS_NEW | TIMED_OUT`
Required: Yes

## See Also
<a name="API_CloseStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/CloseStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/CloseStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/CloseStatusFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
