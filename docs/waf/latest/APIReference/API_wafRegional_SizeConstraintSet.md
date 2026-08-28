---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SizeConstraintSet.html
---

# SizeConstraintSet
<a name="API_wafRegional_SizeConstraintSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A complex type that contains `SizeConstraint` objects, which specify the parts of web requests that you want AWS WAF to inspect the size of. If a `SizeConstraintSet` contains more than one `SizeConstraint` object, a request only needs to match one constraint to be considered a match.

## Contents
<a name="API_wafRegional_SizeConstraintSet_Contents"></a>

 ** SizeConstraints **   <a name="WAF-Type-wafRegional_SizeConstraintSet-SizeConstraints"></a>
Specifies the parts of web requests that you want to inspect the size of.
Type: Array of [SizeConstraint](API_wafRegional_SizeConstraint.md) objects
Required: Yes

 ** SizeConstraintSetId **   <a name="WAF-Type-wafRegional_SizeConstraintSet-SizeConstraintSetId"></a>
A unique identifier for a `SizeConstraintSet`. You use `SizeConstraintSetId` to get information about a `SizeConstraintSet` (see [GetSizeConstraintSet](API_wafRegional_GetSizeConstraintSet.md)), update a `SizeConstraintSet` (see [UpdateSizeConstraintSet](API_wafRegional_UpdateSizeConstraintSet.md)), insert a `SizeConstraintSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), and delete a `SizeConstraintSet` from AWS WAF (see [DeleteSizeConstraintSet](API_wafRegional_DeleteSizeConstraintSet.md)).
 `SizeConstraintSetId` is returned by [CreateSizeConstraintSet](API_wafRegional_CreateSizeConstraintSet.md) and by [ListSizeConstraintSets](API_wafRegional_ListSizeConstraintSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_SizeConstraintSet-Name"></a>
The name, if any, of the `SizeConstraintSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_wafRegional_SizeConstraintSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/SizeConstraintSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/SizeConstraintSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/SizeConstraintSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
