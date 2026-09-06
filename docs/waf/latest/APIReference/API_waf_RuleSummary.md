---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleSummary.html
---

# RuleSummary
<a name="API_waf_RuleSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the identifier and the friendly name or description of the `Rule`.

## Contents
<a name="API_waf_RuleSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-waf_RuleSummary-Name"></a>
A friendly name or description of the [Rule](API_waf_Rule.md). You can't change the name of a `Rule` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RuleId **   <a name="WAF-Type-waf_RuleSummary-RuleId"></a>
A unique identifier for a `Rule`. You use `RuleId` to get more information about a `Rule` (see [GetRule](API_waf_GetRule.md)), update a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), insert a `Rule` into a `WebACL` or delete one from a `WebACL` (see [UpdateWebACL](API_waf_UpdateWebACL.md)), or delete a `Rule` from AWS WAF (see [DeleteRule](API_waf_DeleteRule.md)).
 `RuleId` is returned by [CreateRule](API_waf_CreateRule.md) and by [ListRules](API_waf_ListRules.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/RuleSummary)
