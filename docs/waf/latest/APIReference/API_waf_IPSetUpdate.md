---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_IPSetUpdate.html
---

# IPSetUpdate
<a name="API_waf_IPSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the type of update to perform to an [IPSet](API_waf_IPSet.md) with [UpdateIPSet](API_waf_UpdateIPSet.md).

## Contents
<a name="API_waf_IPSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-waf_IPSetUpdate-Action"></a>
Specifies whether to insert or delete an IP address with [UpdateIPSet](API_waf_UpdateIPSet.md).
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** IPSetDescriptor **   <a name="WAF-Type-waf_IPSetUpdate-IPSetDescriptor"></a>
The IP address type (`IPV4` or `IPV6`) and the IP address range (in CIDR notation) that web requests originate from.
Type: [IPSetDescriptor](API_waf_IPSetDescriptor.md) object
Required: Yes

## See Also
<a name="API_waf_IPSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/IPSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/IPSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/IPSetUpdate)
