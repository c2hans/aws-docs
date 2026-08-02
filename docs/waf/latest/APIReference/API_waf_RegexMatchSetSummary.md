---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexMatchSetSummary.html
---

# RegexMatchSetSummary
<a name="API_waf_RegexMatchSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Returned by [ListRegexMatchSets](API_waf_ListRegexMatchSets.md). Each `RegexMatchSetSummary` object includes the `Name` and `RegexMatchSetId` for one [RegexMatchSet](API_waf_RegexMatchSet.md).

## Contents
<a name="API_waf_RegexMatchSetSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-waf_RegexMatchSetSummary-Name"></a>
A friendly name or description of the [RegexMatchSet](API_waf_RegexMatchSet.md). You can't change `Name` after you create a `RegexMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RegexMatchSetId **   <a name="WAF-Type-waf_RegexMatchSetSummary-RegexMatchSetId"></a>
The `RegexMatchSetId` for a `RegexMatchSet`. You use `RegexMatchSetId` to get information about a `RegexMatchSet`, update a `RegexMatchSet`, remove a `RegexMatchSet` from a `Rule`, and delete a `RegexMatchSet` from AWS WAF.
 `RegexMatchSetId` is returned by [CreateRegexMatchSet](API_waf_CreateRegexMatchSet.md) and by [ListRegexMatchSets](API_waf_ListRegexMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_RegexMatchSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/RegexMatchSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/RegexMatchSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/RegexMatchSetSummary)
