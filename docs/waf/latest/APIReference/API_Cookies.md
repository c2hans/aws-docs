---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Cookies.html
---

# Cookies
<a name="API_Cookies"></a>

Inspect the cookies in the web request. You can specify the parts of the cookies to inspect and you can narrow the set of cookies to inspect by including or excluding specific keys.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

Example JSON: `"Cookies": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }`

## Contents
<a name="API_Cookies_Contents"></a>

 ** MatchPattern **   <a name="WAF-Type-Cookies-MatchPattern"></a>
The filter to use to identify the subset of cookies to inspect in a web request.
You must specify exactly one setting: either `All`, `IncludedCookies`, or `ExcludedCookies`.
Example JSON: `"MatchPattern": { "IncludedCookies": [ "session-id-time", "session-id" ] }`
Type: [CookieMatchPattern](API_CookieMatchPattern.md) object
Required: Yes

 ** MatchScope **   <a name="WAF-Type-Cookies-MatchScope"></a>
The parts of the cookies to inspect with the rule inspection criteria. If you specify `ALL`, AWS WAF inspects both keys and values.
 `All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.
Type: String
Valid Values: `ALL | KEY | VALUE`
Required: Yes

 ** OversizeHandling **   <a name="WAF-Type-Cookies-OversizeHandling"></a>
What AWS WAF should do if the cookies of the request are more numerous or larger than AWS WAF can inspect. AWS WAF does not support inspecting the entire contents of request cookies when they exceed 8 KB (8192 bytes) or 200 total cookies. The underlying host service forwards a maximum of 200 cookies and at most 8 KB of cookie contents to AWS WAF.
The options for oversize handling are the following:
+  `CONTINUE` - Inspect the available cookies normally, according to the rule inspection criteria.
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `CONTINUE | MATCH | NO_MATCH`
Required: Yes

## See Also
<a name="API_Cookies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Cookies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Cookies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Cookies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
