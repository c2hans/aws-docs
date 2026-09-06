---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexMatchSet.html
---

# RegexMatchSet
<a name="API_wafRegional_RegexMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In a [GetRegexMatchSet](API_wafRegional_GetRegexMatchSet.md) request, `RegexMatchSet` is a complex type that contains the `RegexMatchSetId` and `Name` of a `RegexMatchSet`, and the values that you specified when you updated the `RegexMatchSet`.

 The values are contained in a `RegexMatchTuple` object, which specify the parts of web requests that you want AWS WAF to inspect and the values that you want AWS WAF to search for. If a `RegexMatchSet` contains more than one `RegexMatchTuple` object, a request needs to match the settings in only one `ByteMatchTuple` to be considered a match.

## Contents
<a name="API_wafRegional_RegexMatchSet_Contents"></a>

 ** Name **   <a name="WAF-Type-wafRegional_RegexMatchSet-Name"></a>
A friendly name or description of the [RegexMatchSet](#API_wafRegional_RegexMatchSet). You can't change `Name` after you create a `RegexMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** RegexMatchSetId **   <a name="WAF-Type-wafRegional_RegexMatchSet-RegexMatchSetId"></a>
The `RegexMatchSetId` for a `RegexMatchSet`. You use `RegexMatchSetId` to get information about a `RegexMatchSet` (see [GetRegexMatchSet](API_wafRegional_GetRegexMatchSet.md)), update a `RegexMatchSet` (see [UpdateRegexMatchSet](API_wafRegional_UpdateRegexMatchSet.md)), insert a `RegexMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), and delete a `RegexMatchSet` from AWS WAF (see [DeleteRegexMatchSet](API_wafRegional_DeleteRegexMatchSet.md)).
 `RegexMatchSetId` is returned by [CreateRegexMatchSet](API_wafRegional_CreateRegexMatchSet.md) and by [ListRegexMatchSets](API_wafRegional_ListRegexMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** RegexMatchTuples **   <a name="WAF-Type-wafRegional_RegexMatchSet-RegexMatchTuples"></a>
Contains an array of [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md) objects. Each `RegexMatchTuple` object contains:
+ The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.
+ The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see [RegexPatternSet](API_wafRegional_RegexPatternSet.md).
+ Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.
Type: Array of [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md) objects
Required: No

## See Also
<a name="API_wafRegional_RegexMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RegexMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RegexMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RegexMatchSet)
