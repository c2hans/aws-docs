---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexPatternSetSummary.html
---

# RegexPatternSetSummary
<a name="API_wafRegional_RegexPatternSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Returned by [ListRegexPatternSets](API_wafRegional_ListRegexPatternSets.md). Each `RegexPatternSetSummary` object includes the `Name` and `RegexPatternSetId` for one [RegexPatternSet](API_wafRegional_RegexPatternSet.md).

## Contents
<a name="API_wafRegional_RegexPatternSetSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-wafRegional_RegexPatternSetSummary-Name"></a>
A friendly name or description of the [RegexPatternSet](API_wafRegional_RegexPatternSet.md). You can't change `Name` after you create a `RegexPatternSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RegexPatternSetId **   <a name="WAF-Type-wafRegional_RegexPatternSetSummary-RegexPatternSetId"></a>
The `RegexPatternSetId` for a `RegexPatternSet`. You use `RegexPatternSetId` to get information about a `RegexPatternSet`, update a `RegexPatternSet`, remove a `RegexPatternSet` from a `RegexMatchSet`, and delete a `RegexPatternSet` from AWS WAF.
 `RegexPatternSetId` is returned by [CreateRegexPatternSet](API_wafRegional_CreateRegexPatternSet.md) and by [ListRegexPatternSets](API_wafRegional_ListRegexPatternSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_RegexPatternSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RegexPatternSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RegexPatternSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RegexPatternSetSummary)
