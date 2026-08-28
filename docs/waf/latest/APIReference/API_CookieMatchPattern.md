---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CookieMatchPattern.html
---

# CookieMatchPattern
<a name="API_CookieMatchPattern"></a>

The filter to use to identify the subset of cookies to inspect in a web request.

You must specify exactly one setting: either `All`, `IncludedCookies`, or `ExcludedCookies`.

Example JSON: `"MatchPattern": { "IncludedCookies": [ "session-id-time", "session-id" ] }`

## Contents
<a name="API_CookieMatchPattern_Contents"></a>

 ** All **   <a name="WAF-Type-CookieMatchPattern-All"></a>
Inspect all cookies.
Type: [All](API_All.md) object
Required: No

 ** ExcludedCookies **   <a name="WAF-Type-CookieMatchPattern-ExcludedCookies"></a>
Inspect only the cookies whose keys don't match any of the strings specified here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 199 items.
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `.*\S.*`
Required: No

 ** IncludedCookies **   <a name="WAF-Type-CookieMatchPattern-IncludedCookies"></a>
Inspect only the cookies that have a key that matches one of the strings specified here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 199 items.
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_CookieMatchPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CookieMatchPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CookieMatchPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CookieMatchPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
