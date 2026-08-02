---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_IPSetSummary.html
---

# IPSetSummary
<a name="API_wafRegional_IPSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the identifier and the name of the `IPSet`.

## Contents
<a name="API_wafRegional_IPSetSummary_Contents"></a>

 ** IPSetId **   <a name="WAF-Type-wafRegional_IPSetSummary-IPSetId"></a>
The `IPSetId` for an [IPSet](API_wafRegional_IPSet.md). You can use `IPSetId` in a [GetIPSet](API_wafRegional_GetIPSet.md) request to get detailed information about an [IPSet](API_wafRegional_IPSet.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_IPSetSummary-Name"></a>
A friendly name or description of the [IPSet](API_wafRegional_IPSet.md). You can't change the name of an `IPSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_IPSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/IPSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/IPSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/IPSetSummary)
