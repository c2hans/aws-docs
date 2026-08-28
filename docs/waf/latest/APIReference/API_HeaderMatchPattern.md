---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_HeaderMatchPattern.html
---

# HeaderMatchPattern
<a name="API_HeaderMatchPattern"></a>

The filter to use to identify the subset of headers to inspect in a web request.

You must specify exactly one setting: either `All`, `IncludedHeaders`, or `ExcludedHeaders`.

Example JSON: `"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }`

## Contents
<a name="API_HeaderMatchPattern_Contents"></a>

 ** All **   <a name="WAF-Type-HeaderMatchPattern-All"></a>
Inspect all headers.
Type: [All](API_All.md) object
Required: No

 ** ExcludedHeaders **   <a name="WAF-Type-HeaderMatchPattern-ExcludedHeaders"></a>
Inspect only the headers whose keys don't match any of the strings specified here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 199 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** IncludedHeaders **   <a name="WAF-Type-HeaderMatchPattern-IncludedHeaders"></a>
Inspect only the headers that have a key that matches one of the strings specified here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 199 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_HeaderMatchPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/HeaderMatchPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/HeaderMatchPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/HeaderMatchPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
