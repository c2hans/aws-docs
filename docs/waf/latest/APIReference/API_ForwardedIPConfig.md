---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ForwardedIPConfig.html
---

# ForwardedIPConfig
<a name="API_ForwardedIPConfig"></a>

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

**Note**
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.

This configuration is used for [GeoMatchStatement](API_GeoMatchStatement.md), [AsnMatchStatement](API_AsnMatchStatement.md), and [RateBasedStatement](API_RateBasedStatement.md). For [IPSetReferenceStatement](API_IPSetReferenceStatement.md), use [IPSetForwardedIPConfig](API_IPSetForwardedIPConfig.md) instead.

 AWS WAF only evaluates the first IP address found in the specified HTTP header.

## Contents
<a name="API_ForwardedIPConfig_Contents"></a>

 ** FallbackBehavior **   <a name="WAF-Type-ForwardedIPConfig-FallbackBehavior"></a>
The match status to assign to the web request if the request doesn't have a valid IP address in the specified position.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
You can specify the following fallback behaviors:
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `MATCH | NO_MATCH`
Required: Yes

 ** HeaderName **   <a name="WAF-Type-ForwardedIPConfig-HeaderName"></a>
The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to `X-Forwarded-For`.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

## See Also
<a name="API_ForwardedIPConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ForwardedIPConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ForwardedIPConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ForwardedIPConfig)
