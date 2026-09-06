---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexPatternSet.html
---

# RegexPatternSet
<a name="API_waf_RegexPatternSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The `RegexPatternSet` specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

## Contents
<a name="API_waf_RegexPatternSet_Contents"></a>

 ** RegexPatternSetId **   <a name="WAF-Type-waf_RegexPatternSet-RegexPatternSetId"></a>
The identifier for the `RegexPatternSet`. You use `RegexPatternSetId` to get information about a `RegexPatternSet`, update a `RegexPatternSet`, remove a `RegexPatternSet` from a `RegexMatchSet`, and delete a `RegexPatternSet` from AWS WAF.
 `RegexMatchSetId` is returned by [CreateRegexPatternSet](API_waf_CreateRegexPatternSet.md) and by [ListRegexPatternSets](API_waf_ListRegexPatternSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RegexPatternStrings **   <a name="WAF-Type-waf_RegexPatternSet-RegexPatternStrings"></a>
Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** Name **   <a name="WAF-Type-waf_RegexPatternSet-Name"></a>
A friendly name or description of the [RegexPatternSet](#API_waf_RegexPatternSet). You can't change `Name` after you create a `RegexPatternSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_RegexPatternSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/RegexPatternSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/RegexPatternSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/RegexPatternSet)
