---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SqlInjectionMatchSet.html
---

# SqlInjectionMatchSet
<a name="API_wafRegional_SqlInjectionMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A complex type that contains `SqlInjectionMatchTuple` objects, which specify the parts of web requests that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header. If a `SqlInjectionMatchSet` contains more than one `SqlInjectionMatchTuple` object, a request needs to include snippets of SQL code in only one of the specified parts of the request to be considered a match.

## Contents
<a name="API_wafRegional_SqlInjectionMatchSet_Contents"></a>

 ** SqlInjectionMatchSetId **   <a name="WAF-Type-wafRegional_SqlInjectionMatchSet-SqlInjectionMatchSetId"></a>
A unique identifier for a `SqlInjectionMatchSet`. You use `SqlInjectionMatchSetId` to get information about a `SqlInjectionMatchSet` (see [GetSqlInjectionMatchSet](API_wafRegional_GetSqlInjectionMatchSet.md)), update a `SqlInjectionMatchSet` (see [UpdateSqlInjectionMatchSet](API_wafRegional_UpdateSqlInjectionMatchSet.md)), insert a `SqlInjectionMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), and delete a `SqlInjectionMatchSet` from AWS WAF (see [DeleteSqlInjectionMatchSet](API_wafRegional_DeleteSqlInjectionMatchSet.md)).
 `SqlInjectionMatchSetId` is returned by [CreateSqlInjectionMatchSet](API_wafRegional_CreateSqlInjectionMatchSet.md) and by [ListSqlInjectionMatchSets](API_wafRegional_ListSqlInjectionMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** SqlInjectionMatchTuples **   <a name="WAF-Type-wafRegional_SqlInjectionMatchSet-SqlInjectionMatchTuples"></a>
Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.
Type: Array of [SqlInjectionMatchTuple](API_wafRegional_SqlInjectionMatchTuple.md) objects
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_SqlInjectionMatchSet-Name"></a>
The name, if any, of the `SqlInjectionMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_wafRegional_SqlInjectionMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/SqlInjectionMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/SqlInjectionMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/SqlInjectionMatchSet)
