---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SizeConstraintSetSummary.html
---

# SizeConstraintSetSummary
<a name="API_waf_SizeConstraintSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The `Id` and `Name` of a `SizeConstraintSet`.

## Contents
<a name="API_waf_SizeConstraintSetSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-waf_SizeConstraintSetSummary-Name"></a>
The name of the `SizeConstraintSet`, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** SizeConstraintSetId **   <a name="WAF-Type-waf_SizeConstraintSetSummary-SizeConstraintSetId"></a>
A unique identifier for a `SizeConstraintSet`. You use `SizeConstraintSetId` to get information about a `SizeConstraintSet` (see [GetSizeConstraintSet](API_waf_GetSizeConstraintSet.md)), update a `SizeConstraintSet` (see [UpdateSizeConstraintSet](API_waf_UpdateSizeConstraintSet.md)), insert a `SizeConstraintSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), and delete a `SizeConstraintSet` from AWS WAF (see [DeleteSizeConstraintSet](API_waf_DeleteSizeConstraintSet.md)).
 `SizeConstraintSetId` is returned by [CreateSizeConstraintSet](API_waf_CreateSizeConstraintSet.md) and by [ListSizeConstraintSets](API_waf_ListSizeConstraintSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_SizeConstraintSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/SizeConstraintSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/SizeConstraintSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/SizeConstraintSetSummary)
