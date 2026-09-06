---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_UriFragment.html
---

# UriFragment
<a name="API_UriFragment"></a>

Inspect fragments of the request URI. You can specify the parts of the URI fragment to inspect and you can narrow the set of URI fragments to inspect by including or excluding specific keys.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

Example JSON: `"UriFragment": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }`

## Contents
<a name="API_UriFragment_Contents"></a>

 ** FallbackBehavior **   <a name="WAF-Type-UriFragment-FallbackBehavior"></a>
What AWS WAF should do if it fails to completely parse the JSON body. The options are the following:
+  `EVALUATE_AS_STRING` - Inspect the body as plain text. AWS WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
If you don't provide this setting, AWS WAF parses and evaluates the content only up to the first parsing failure that it encounters.
Example JSON: `{ "UriFragment": { "FallbackBehavior": "MATCH"} }`
 AWS WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, AWS WAF doesn't apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the * AWS WAF Developer Guide*.
Type: String
Valid Values: `MATCH | NO_MATCH`
Required: No

## See Also
<a name="API_UriFragment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/UriFragment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/UriFragment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/UriFragment)
