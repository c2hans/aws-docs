---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SqlInjectionMatchSetSummary.html
---

# SqlInjectionMatchSetSummary
<a name="API_wafRegional_SqlInjectionMatchSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The `Id` and `Name` of a `SqlInjectionMatchSet`.

## Contents
<a name="API_wafRegional_SqlInjectionMatchSetSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-wafRegional_SqlInjectionMatchSetSummary-Name"></a>
The name of the `SqlInjectionMatchSet`, if any, specified by `Id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** SqlInjectionMatchSetId **   <a name="WAF-Type-wafRegional_SqlInjectionMatchSetSummary-SqlInjectionMatchSetId"></a>
A unique identifier for a `SqlInjectionMatchSet`. You use `SqlInjectionMatchSetId` to get information about a `SqlInjectionMatchSet` (see [GetSqlInjectionMatchSet](API_wafRegional_GetSqlInjectionMatchSet.md)), update a `SqlInjectionMatchSet` (see [UpdateSqlInjectionMatchSet](API_wafRegional_UpdateSqlInjectionMatchSet.md)), insert a `SqlInjectionMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), and delete a `SqlInjectionMatchSet` from AWS WAF (see [DeleteSqlInjectionMatchSet](API_wafRegional_DeleteSqlInjectionMatchSet.md)).
 `SqlInjectionMatchSetId` is returned by [CreateSqlInjectionMatchSet](API_wafRegional_CreateSqlInjectionMatchSet.md) and by [ListSqlInjectionMatchSets](API_wafRegional_ListSqlInjectionMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_SqlInjectionMatchSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/SqlInjectionMatchSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/SqlInjectionMatchSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/SqlInjectionMatchSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
