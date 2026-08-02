---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSetForwardedIPConfig.html
---

# IPSetForwardedIPConfig
<a name="API_IPSetForwardedIPConfig"></a>

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

**Note**
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.

This configuration is used only for [IPSetReferenceStatement](API_IPSetReferenceStatement.md). For [GeoMatchStatement](API_GeoMatchStatement.md) and [RateBasedStatement](API_RateBasedStatement.md), use [ForwardedIPConfig](API_ForwardedIPConfig.md) instead.

## Contents
<a name="API_IPSetForwardedIPConfig_Contents"></a>

 ** FallbackBehavior **   <a name="WAF-Type-IPSetForwardedIPConfig-FallbackBehavior"></a>
The match status to assign to the web request if the request doesn't have a valid IP address in the specified position.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
You can specify the following fallback behaviors:
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `MATCH | NO_MATCH`
Required: Yes

 ** HeaderName **   <a name="WAF-Type-IPSetForwardedIPConfig-HeaderName"></a>
The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to `X-Forwarded-For`.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** Position **   <a name="WAF-Type-IPSetForwardedIPConfig-Position"></a>
The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be `10.1.1.1, 127.0.0.0, 10.10.10.10` where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:
+ FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the client's original IP.
+ LAST - Inspect the last IP address in the list of IP addresses in the header.
+ ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.
Type: String
Valid Values: `FIRST | LAST | ANY`
Required: Yes

## See Also
<a name="API_IPSetForwardedIPConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/IPSetForwardedIPConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/IPSetForwardedIPConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/IPSetForwardedIPConfig)
