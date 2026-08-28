---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleGroupUpdate.html
---

# RuleGroupUpdate
<a name="API_wafRegional_RuleGroupUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies an `ActivatedRule` and indicates whether you want to add it to a `RuleGroup` or delete it from a `RuleGroup`.

## Contents
<a name="API_wafRegional_RuleGroupUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-wafRegional_RuleGroupUpdate-Action"></a>
Specify `INSERT` to add an `ActivatedRule` to a `RuleGroup`. Use `DELETE` to remove an `ActivatedRule` from a `RuleGroup`.
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** ActivatedRule **   <a name="WAF-Type-wafRegional_RuleGroupUpdate-ActivatedRule"></a>
The `ActivatedRule` object specifies a `Rule` that you want to insert or delete, the priority of the `Rule` in the `WebACL`, and the action that you want AWS WAF to take when a web request matches the `Rule` (`ALLOW`, `BLOCK`, or `COUNT`).
Type: [ActivatedRule](API_wafRegional_ActivatedRule.md) object
Required: Yes

## See Also
<a name="API_wafRegional_RuleGroupUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RuleGroupUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RuleGroupUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RuleGroupUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
