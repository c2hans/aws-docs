---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GeoMatchSet.html
---

# GeoMatchSet
<a name="API_waf_GeoMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains one or more countries that AWS WAF will search for.

## Contents
<a name="API_waf_GeoMatchSet_Contents"></a>

 ** GeoMatchConstraints **   <a name="WAF-Type-waf_GeoMatchSet-GeoMatchConstraints"></a>
An array of [GeoMatchConstraint](API_waf_GeoMatchConstraint.md) objects, which contain the country that you want AWS WAF to search for.
Type: Array of [GeoMatchConstraint](API_waf_GeoMatchConstraint.md) objects
Required: Yes

 ** GeoMatchSetId **   <a name="WAF-Type-waf_GeoMatchSet-GeoMatchSetId"></a>
The `GeoMatchSetId` for an `GeoMatchSet`. You use `GeoMatchSetId` to get information about a `GeoMatchSet` (see [GeoMatchSet](#API_waf_GeoMatchSet)), update a `GeoMatchSet` (see [UpdateGeoMatchSet](API_waf_UpdateGeoMatchSet.md)), insert a `GeoMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), and delete a `GeoMatchSet` from AWS WAF (see [DeleteGeoMatchSet](API_waf_DeleteGeoMatchSet.md)).
 `GeoMatchSetId` is returned by [CreateGeoMatchSet](API_waf_CreateGeoMatchSet.md) and by [ListGeoMatchSets](API_waf_ListGeoMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-waf_GeoMatchSet-Name"></a>
A friendly name or description of the [GeoMatchSet](#API_waf_GeoMatchSet). You can't change the name of an `GeoMatchSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_GeoMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GeoMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GeoMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GeoMatchSet)
