---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SubscribedRuleGroupSummary.html
---

# SubscribedRuleGroupSummary
<a name="API_waf_SubscribedRuleGroupSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A summary of the rule groups you are subscribed to.

## Contents
<a name="API_waf_SubscribedRuleGroupSummary_Contents"></a>

 ** MetricName **   <a name="WAF-Type-waf_SubscribedRuleGroupSummary-MetricName"></a>
A friendly name or description for the metrics for this `RuleGroup`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `RuleGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-waf_SubscribedRuleGroupSummary-Name"></a>
A friendly name or description of the `RuleGroup`. You can't change the name of a `RuleGroup` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RuleGroupId **   <a name="WAF-Type-waf_SubscribedRuleGroupSummary-RuleGroupId"></a>
A unique identifier for a `RuleGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_SubscribedRuleGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/SubscribedRuleGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/SubscribedRuleGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/SubscribedRuleGroupSummary)
