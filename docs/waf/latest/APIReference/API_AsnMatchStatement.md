---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AsnMatchStatement.html
---

# AsnMatchStatement
<a name="API_AsnMatchStatement"></a>

A rule statement that inspects web traffic based on the Autonomous System Number (ASN) associated with the request's IP address.

For additional details, see [ASN match rule statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-asn-match.html) in the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

## Contents
<a name="API_AsnMatchStatement_Contents"></a>

 ** AsnList **   <a name="WAF-Type-AsnMatchStatement-AsnList"></a>
Contains one or more Autonomous System Numbers (ASNs). ASNs are unique identifiers assigned to large internet networks managed by organizations such as internet service providers, enterprises, universities, or government agencies.
Type: Array of longs
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** ForwardedIPConfig **   <a name="WAF-Type-AsnMatchStatement-ForwardedIPConfig"></a>
The configuration for inspecting IP addresses to match against an ASN in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.
Type: [ForwardedIPConfig](API_ForwardedIPConfig.md) object
Required: No

## See Also
<a name="API_AsnMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AsnMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AsnMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AsnMatchStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
