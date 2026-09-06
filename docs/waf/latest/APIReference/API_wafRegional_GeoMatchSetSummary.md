---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GeoMatchSetSummary.html
---

# GeoMatchSetSummary
<a name="API_wafRegional_GeoMatchSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the identifier and the name of the `GeoMatchSet`.

## Contents
<a name="API_wafRegional_GeoMatchSetSummary_Contents"></a>

 ** GeoMatchSetId **   <a name="WAF-Type-wafRegional_GeoMatchSetSummary-GeoMatchSetId"></a>
The `GeoMatchSetId` for an [GeoMatchSet](API_wafRegional_GeoMatchSet.md). You can use `GeoMatchSetId` in a [GetGeoMatchSet](API_wafRegional_GetGeoMatchSet.md) request to get detailed information about an [GeoMatchSet](API_wafRegional_GeoMatchSet.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_GeoMatchSetSummary-Name"></a>
A friendly name or description of the [GeoMatchSet](API_wafRegional_GeoMatchSet.md). You can't change the name of an `GeoMatchSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_GeoMatchSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GeoMatchSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GeoMatchSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GeoMatchSetSummary)
