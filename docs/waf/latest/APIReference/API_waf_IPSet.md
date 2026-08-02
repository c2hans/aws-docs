---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_IPSet.html
---

# IPSet
<a name="API_waf_IPSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains one or more IP addresses or blocks of IP addresses specified in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128.

To specify an individual IP address, you specify the four-part IP address followed by a `/32`, for example, 192.0.2.0/32. To block a range of IP addresses, you can specify /8 or any range between /16 through /32 (for IPv4) or /24, /32, /48, /56, /64, or /128 (for IPv6). For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

## Contents
<a name="API_waf_IPSet_Contents"></a>

 ** IPSetDescriptors **   <a name="WAF-Type-waf_IPSet-IPSetDescriptors"></a>
The IP address type (`IPV4` or `IPV6`) and the IP address range (in CIDR notation) that web requests originate from. If the `WebACL` is associated with an Amazon CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.
Type: Array of [IPSetDescriptor](API_waf_IPSetDescriptor.md) objects
Required: Yes

 ** IPSetId **   <a name="WAF-Type-waf_IPSet-IPSetId"></a>
The `IPSetId` for an `IPSet`. You use `IPSetId` to get information about an `IPSet` (see [GetIPSet](API_waf_GetIPSet.md)), update an `IPSet` (see [UpdateIPSet](API_waf_UpdateIPSet.md)), insert an `IPSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), and delete an `IPSet` from AWS WAF (see [DeleteIPSet](API_waf_DeleteIPSet.md)).
 `IPSetId` is returned by [CreateIPSet](API_waf_CreateIPSet.md) and by [ListIPSets](API_waf_ListIPSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-waf_IPSet-Name"></a>
A friendly name or description of the [IPSet](#API_waf_IPSet). You can't change the name of an `IPSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_IPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/IPSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/IPSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/IPSet)
