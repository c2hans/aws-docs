---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GeoMatchSet.html
---

# GeoMatchSet
<a name="API_wafRegional_GeoMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains one or more countries that AWS WAF will search for.

## Contents
<a name="API_wafRegional_GeoMatchSet_Contents"></a>

 ** GeoMatchConstraints **   <a name="WAF-Type-wafRegional_GeoMatchSet-GeoMatchConstraints"></a>
An array of [GeoMatchConstraint](API_wafRegional_GeoMatchConstraint.md) objects, which contain the country that you want AWS WAF to search for.
Type: Array of [GeoMatchConstraint](API_wafRegional_GeoMatchConstraint.md) objects
Required: Yes

 ** GeoMatchSetId **   <a name="WAF-Type-wafRegional_GeoMatchSet-GeoMatchSetId"></a>
The `GeoMatchSetId` for an `GeoMatchSet`. You use `GeoMatchSetId` to get information about a `GeoMatchSet` (see [GeoMatchSet](#API_wafRegional_GeoMatchSet)), update a `GeoMatchSet` (see [UpdateGeoMatchSet](API_wafRegional_UpdateGeoMatchSet.md)), insert a `GeoMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), and delete a `GeoMatchSet` from AWS WAF (see [DeleteGeoMatchSet](API_wafRegional_DeleteGeoMatchSet.md)).
 `GeoMatchSetId` is returned by [CreateGeoMatchSet](API_wafRegional_CreateGeoMatchSet.md) and by [ListGeoMatchSets](API_wafRegional_ListGeoMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_GeoMatchSet-Name"></a>
A friendly name or description of the [GeoMatchSet](#API_wafRegional_GeoMatchSet). You can't change the name of an `GeoMatchSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_wafRegional_GeoMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GeoMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GeoMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GeoMatchSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
