---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateLimitJA4Fingerprint.html
---

# RateLimitJA4Fingerprint
<a name="API_RateLimitJA4Fingerprint"></a>

Use the request's JA4 fingerprint derived from the TLS Client Hello of an incoming request as an aggregate key. If you use a single JA4 fingerprint as your custom key, then each value fully defines an aggregation instance.

## Contents
<a name="API_RateLimitJA4Fingerprint_Contents"></a>

 ** FallbackBehavior **   <a name="WAF-Type-RateLimitJA4Fingerprint-FallbackBehavior"></a>
The match status to assign to the web request if there is insufficient TSL Client Hello information to compute the JA4 fingerprint.
You can specify the following fallback behaviors:
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `MATCH | NO_MATCH`
Required: Yes

## See Also
<a name="API_RateLimitJA4Fingerprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateLimitJA4Fingerprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateLimitJA4Fingerprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateLimitJA4Fingerprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
