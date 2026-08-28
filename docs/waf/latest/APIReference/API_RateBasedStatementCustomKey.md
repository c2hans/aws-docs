---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedStatementCustomKey.html
---

# RateBasedStatementCustomKey
<a name="API_RateBasedStatementCustomKey"></a>

Specifies a single custom aggregate key for a rate-base rule.

**Note**
Web requests that are missing any of the components specified in the aggregation keys are omitted from the rate-based rule evaluation and handling.

## Contents
<a name="API_RateBasedStatementCustomKey_Contents"></a>

 ** ASN **   <a name="WAF-Type-RateBasedStatementCustomKey-ASN"></a>
Use an Autonomous System Number (ASN) derived from the request's originating or forwarded IP address as an aggregate key. Each distinct ASN contributes to the aggregation instance.
Type: [RateLimitAsn](API_RateLimitAsn.md) object
Required: No

 ** Cookie **   <a name="WAF-Type-RateBasedStatementCustomKey-Cookie"></a>
Use the value of a cookie in the request as an aggregate key. Each distinct value in the cookie contributes to the aggregation instance. If you use a single cookie as your custom key, then each value fully defines an aggregation instance.
Type: [RateLimitCookie](API_RateLimitCookie.md) object
Required: No

 ** ForwardedIP **   <a name="WAF-Type-RateBasedStatementCustomKey-ForwardedIP"></a>
Use the first IP address in an HTTP header as an aggregate key. Each distinct forwarded IP address contributes to the aggregation instance.
When you specify an IP or forwarded IP in the custom key settings, you must also specify at least one other key to use. You can aggregate on only the forwarded IP address by specifying `FORWARDED_IP` in your rate-based statement's `AggregateKeyType`.
With this option, you must specify the header to use in the rate-based rule's `ForwardedIPConfig` property.
Type: [RateLimitForwardedIP](API_RateLimitForwardedIP.md) object
Required: No

 ** Header **   <a name="WAF-Type-RateBasedStatementCustomKey-Header"></a>
Use the value of a header in the request as an aggregate key. Each distinct value in the header contributes to the aggregation instance. If you use a single header as your custom key, then each value fully defines an aggregation instance.
Type: [RateLimitHeader](API_RateLimitHeader.md) object
Required: No

 ** HTTPMethod **   <a name="WAF-Type-RateBasedStatementCustomKey-HTTPMethod"></a>
Use the request's HTTP method as an aggregate key. Each distinct HTTP method contributes to the aggregation instance. If you use just the HTTP method as your custom key, then each method fully defines an aggregation instance.
Type: [RateLimitHTTPMethod](API_RateLimitHTTPMethod.md) object
Required: No

 ** IP **   <a name="WAF-Type-RateBasedStatementCustomKey-IP"></a>
Use the request's originating IP address as an aggregate key. Each distinct IP address contributes to the aggregation instance.
When you specify an IP or forwarded IP in the custom key settings, you must also specify at least one other key to use. You can aggregate on only the IP address by specifying `IP` in your rate-based statement's `AggregateKeyType`.
Type: [RateLimitIP](API_RateLimitIP.md) object
Required: No

 ** JA3Fingerprint **   <a name="WAF-Type-RateBasedStatementCustomKey-JA3Fingerprint"></a>
 Use the request's JA3 fingerprint as an aggregate key. If you use a single JA3 fingerprint as your custom key, then each value fully defines an aggregation instance.
Type: [RateLimitJA3Fingerprint](API_RateLimitJA3Fingerprint.md) object
Required: No

 ** JA4Fingerprint **   <a name="WAF-Type-RateBasedStatementCustomKey-JA4Fingerprint"></a>
Use the request's JA4 fingerprint as an aggregate key. If you use a single JA4 fingerprint as your custom key, then each value fully defines an aggregation instance.
Type: [RateLimitJA4Fingerprint](API_RateLimitJA4Fingerprint.md) object
Required: No

 ** LabelNamespace **   <a name="WAF-Type-RateBasedStatementCustomKey-LabelNamespace"></a>
Use the specified label namespace as an aggregate key. Each distinct fully qualified label name that has the specified label namespace contributes to the aggregation instance. If you use just one label namespace as your custom key, then each label name fully defines an aggregation instance.
This uses only labels that have been added to the request by rules that are evaluated before this rate-based rule in the web ACL.
For information about label namespaces and names, see [Label syntax and naming requirements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-requirements.html) in the * AWS WAF Developer Guide*.
Type: [RateLimitLabelNamespace](API_RateLimitLabelNamespace.md) object
Required: No

 ** QueryArgument **   <a name="WAF-Type-RateBasedStatementCustomKey-QueryArgument"></a>
Use the specified query argument as an aggregate key. Each distinct value for the named query argument contributes to the aggregation instance. If you use a single query argument as your custom key, then each value fully defines an aggregation instance.
Type: [RateLimitQueryArgument](API_RateLimitQueryArgument.md) object
Required: No

 ** QueryString **   <a name="WAF-Type-RateBasedStatementCustomKey-QueryString"></a>
Use the request's query string as an aggregate key. Each distinct string contributes to the aggregation instance. If you use just the query string as your custom key, then each string fully defines an aggregation instance.
Type: [RateLimitQueryString](API_RateLimitQueryString.md) object
Required: No

 ** UriPath **   <a name="WAF-Type-RateBasedStatementCustomKey-UriPath"></a>
Use the request's URI path as an aggregate key. Each distinct URI path contributes to the aggregation instance. If you use just the URI path as your custom key, then each URI path fully defines an aggregation instance.
Type: [RateLimitUriPath](API_RateLimitUriPath.md) object
Required: No

## See Also
<a name="API_RateBasedStatementCustomKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateBasedStatementCustomKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateBasedStatementCustomKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateBasedStatementCustomKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
