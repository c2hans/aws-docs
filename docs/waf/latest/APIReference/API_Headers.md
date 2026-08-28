---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Headers.html
---

# Headers
<a name="API_Headers"></a>

Inspect all headers in the web request. You can specify the parts of the headers to inspect and you can narrow the set of headers to inspect by including or excluding specific keys.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

If you want to inspect just the value of a single header, use the `SingleHeader` `FieldToMatch` setting instead.

Example JSON: `"Headers": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }`

## Contents
<a name="API_Headers_Contents"></a>

 ** MatchPattern **   <a name="WAF-Type-Headers-MatchPattern"></a>
The filter to use to identify the subset of headers to inspect in a web request.
You must specify exactly one setting: either `All`, `IncludedHeaders`, or `ExcludedHeaders`.
Example JSON: `"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }`
Type: [HeaderMatchPattern](API_HeaderMatchPattern.md) object
Required: Yes

 ** MatchScope **   <a name="WAF-Type-Headers-MatchScope"></a>
The parts of the headers to match with the rule inspection criteria. If you specify `ALL`, AWS WAF inspects both keys and values.
 `All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.
Type: String
Valid Values: `ALL | KEY | VALUE`
Required: Yes

 ** OversizeHandling **   <a name="WAF-Type-Headers-OversizeHandling"></a>
What AWS WAF should do if the headers determined by your match scope are more numerous or larger than AWS WAF can inspect. AWS WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to AWS WAF.
The options for oversize handling are the following:
+  `CONTINUE` - Inspect the available headers normally, according to the rule inspection criteria.
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `CONTINUE | MATCH | NO_MATCH`
Required: Yes

## See Also
<a name="API_Headers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Headers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Headers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Headers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
