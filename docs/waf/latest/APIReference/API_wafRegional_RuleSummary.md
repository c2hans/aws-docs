---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleSummary.html
---

# RuleSummary
<a name="API_wafRegional_RuleSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the identifier and the friendly name or description of the `Rule`.

## Contents
<a name="API_wafRegional_RuleSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-wafRegional_RuleSummary-Name"></a>
A friendly name or description of the [Rule](API_wafRegional_Rule.md). You can't change the name of a `Rule` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RuleId **   <a name="WAF-Type-wafRegional_RuleSummary-RuleId"></a>
A unique identifier for a `Rule`. You use `RuleId` to get more information about a `Rule` (see [GetRule](API_wafRegional_GetRule.md)), update a `Rule` (see [UpdateRule](API_wafRegional_UpdateRule.md)), insert a `Rule` into a `WebACL` or delete one from a `WebACL` (see [UpdateWebACL](API_wafRegional_UpdateWebACL.md)), or delete a `Rule` from AWS WAF (see [DeleteRule](API_wafRegional_DeleteRule.md)).
 `RuleId` is returned by [CreateRule](API_wafRegional_CreateRule.md) and by [ListRules](API_wafRegional_ListRules.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_wafRegional_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RuleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
