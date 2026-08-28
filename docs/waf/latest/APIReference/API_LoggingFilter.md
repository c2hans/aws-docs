---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_LoggingFilter.html
---

# LoggingFilter
<a name="API_LoggingFilter"></a>

Filtering that specifies which web requests are kept in the logs and which are dropped, defined for a web ACL's [LoggingConfiguration](API_LoggingConfiguration.md).

You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.

## Contents
<a name="API_LoggingFilter_Contents"></a>

 ** DefaultBehavior **   <a name="WAF-Type-LoggingFilter-DefaultBehavior"></a>
Default handling for logs that don't match any of the specified filtering conditions.
Type: String
Valid Values: `KEEP | DROP`
Required: Yes

 ** Filters **   <a name="WAF-Type-LoggingFilter-Filters"></a>
The filters that you want to apply to the logs.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_LoggingFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/LoggingFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/LoggingFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/LoggingFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
