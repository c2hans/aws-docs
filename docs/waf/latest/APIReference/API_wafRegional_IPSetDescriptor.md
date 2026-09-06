---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_IPSetDescriptor.html
---

# IPSetDescriptor
<a name="API_wafRegional_IPSetDescriptor"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the IP address type (`IPV4` or `IPV6`) and the IP address range (in CIDR format) that web requests originate from.

## Contents
<a name="API_wafRegional_IPSetDescriptor_Contents"></a>

 ** Type **   <a name="WAF-Type-wafRegional_IPSetDescriptor-Type"></a>
Specify `IPV4` or `IPV6`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: Yes

 ** Value **   <a name="WAF-Type-wafRegional_IPSetDescriptor-Value"></a>
Specify an IPv4 address by using CIDR notation. For example:
+ To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
Specify an IPv6 address by using CIDR notation. For example:
+ To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_IPSetDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/IPSetDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/IPSetDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/IPSetDescriptor)
