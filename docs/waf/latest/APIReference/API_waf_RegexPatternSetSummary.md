---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexPatternSetSummary.html
---

# RegexPatternSetSummary
<a name="API_waf_RegexPatternSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Returned by [ListRegexPatternSets](API_waf_ListRegexPatternSets.md). Each `RegexPatternSetSummary` object includes the `Name` and `RegexPatternSetId` for one [RegexPatternSet](API_waf_RegexPatternSet.md).

## Contents
<a name="API_waf_RegexPatternSetSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-waf_RegexPatternSetSummary-Name"></a>
A friendly name or description of the [RegexPatternSet](API_waf_RegexPatternSet.md). You can't change `Name` after you create a `RegexPatternSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RegexPatternSetId **   <a name="WAF-Type-waf_RegexPatternSetSummary-RegexPatternSetId"></a>
The `RegexPatternSetId` for a `RegexPatternSet`. You use `RegexPatternSetId` to get information about a `RegexPatternSet`, update a `RegexPatternSet`, remove a `RegexPatternSet` from a `RegexMatchSet`, and delete a `RegexPatternSet` from AWS WAF.
 `RegexPatternSetId` is returned by [CreateRegexPatternSet](API_waf_CreateRegexPatternSet.md) and by [ListRegexPatternSets](API_waf_ListRegexPatternSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_RegexPatternSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/RegexPatternSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/RegexPatternSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/RegexPatternSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
