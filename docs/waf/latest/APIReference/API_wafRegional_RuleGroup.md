---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleGroup.html
---

# RuleGroup
<a name="API_wafRegional_RuleGroup"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A collection of predefined rules that you can add to a web ACL.

Rule groups are subject to the following limits:
+ Three rule groups per account. You can request an increase to this limit by contacting customer support.
+ One rule group per web ACL.
+ Ten rules per rule group.

## Contents
<a name="API_wafRegional_RuleGroup_Contents"></a>

 ** RuleGroupId **   <a name="WAF-Type-wafRegional_RuleGroup-RuleGroupId"></a>
A unique identifier for a `RuleGroup`. You use `RuleGroupId` to get more information about a `RuleGroup` (see [GetRuleGroup](API_wafRegional_GetRuleGroup.md)), update a `RuleGroup` (see [UpdateRuleGroup](API_wafRegional_UpdateRuleGroup.md)), insert a `RuleGroup` into a `WebACL` or delete a one from a `WebACL` (see [UpdateWebACL](API_wafRegional_UpdateWebACL.md)), or delete a `RuleGroup` from AWS WAF (see [DeleteRuleGroup](API_wafRegional_DeleteRuleGroup.md)).
 `RuleGroupId` is returned by [CreateRuleGroup](API_wafRegional_CreateRuleGroup.md) and by [ListRuleGroups](API_wafRegional_ListRuleGroups.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** MetricName **   <a name="WAF-Type-wafRegional_RuleGroup-MetricName"></a>
A friendly name or description for the metrics for this `RuleGroup`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `RuleGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="WAF-Type-wafRegional_RuleGroup-Name"></a>
The friendly name or description for the `RuleGroup`. You can't change the name of a `RuleGroup` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_wafRegional_RuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
