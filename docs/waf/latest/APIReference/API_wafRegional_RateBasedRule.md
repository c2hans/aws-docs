---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RateBasedRule.html
---

# RateBasedRule
<a name="API_wafRegional_RateBasedRule"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A `RateBasedRule` is identical to a regular [Rule](API_wafRegional_Rule.md), with one addition: a `RateBasedRule` counts the number of requests that arrive from a specified IP address every five minutes. For example, based on recent requests that you've seen from an attacker, you might create a `RateBasedRule` that includes the following conditions:
+ The requests come from 192.0.2.44.
+ They contain the value `BadBot` in the `User-Agent` header.

In the rule, you also define the rate limit as 1,000.

Requests that meet both of these conditions and exceed 1,000 requests every five minutes trigger the rule's action (block or count), which is defined in the web ACL.

## Contents
<a name="API_wafRegional_RateBasedRule_Contents"></a>

 ** MetricName **   <a name="WAF-Type-wafRegional_RateBasedRule-MetricName"></a>
A friendly name or description for the metrics for a `RateBasedRule`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `RateBasedRule`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-wafRegional_RateBasedRule-Name"></a>
A friendly name or description for a `RateBasedRule`. You can't change the name of a `RateBasedRule` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** RateKey **   <a name="WAF-Type-wafRegional_RateBasedRule-RateKey"></a>
The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for `RateKey` is `IP`. `IP` indicates that requests arriving from the same IP address are subject to the `RateLimit` that is specified in the `RateBasedRule`.
Type: String
Valid Values: `IP`
Required: Yes

 ** RateLimit **   <a name="WAF-Type-wafRegional_RateBasedRule-RateLimit"></a>
The maximum number of requests, which have an identical value in the field specified by the `RateKey`, allowed in a five-minute period. If the number of requests exceeds the `RateLimit` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.
Type: Long
Valid Range: Minimum value of 100. Maximum value of 2000000000.
Required: Yes

 ** RuleId **   <a name="WAF-Type-wafRegional_RateBasedRule-RuleId"></a>
A unique identifier for a `RateBasedRule`. You use `RuleId` to get more information about a `RateBasedRule` (see [GetRateBasedRule](API_wafRegional_GetRateBasedRule.md)), update a `RateBasedRule` (see [UpdateRateBasedRule](API_wafRegional_UpdateRateBasedRule.md)), insert a `RateBasedRule` into a `WebACL` or delete one from a `WebACL` (see [UpdateWebACL](API_wafRegional_UpdateWebACL.md)), or delete a `RateBasedRule` from AWS WAF (see [DeleteRateBasedRule](API_wafRegional_DeleteRateBasedRule.md)).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** MatchPredicates **   <a name="WAF-Type-wafRegional_RateBasedRule-MatchPredicates"></a>
The `Predicates` object contains one `Predicate` element for each [ByteMatchSet](API_wafRegional_ByteMatchSet.md), [IPSet](API_wafRegional_IPSet.md), or [SqlInjectionMatchSet](API_wafRegional_SqlInjectionMatchSet.md) object that you want to include in a `RateBasedRule`.
Type: Array of [Predicate](API_wafRegional_Predicate.md) objects
Required: No

## See Also
<a name="API_wafRegional_RateBasedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RateBasedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RateBasedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RateBasedRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
