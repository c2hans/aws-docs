---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_Rule.html
---

# Rule
<a name="API_waf_Rule"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A combination of [ByteMatchSet](API_waf_ByteMatchSet.md), [IPSet](API_waf_IPSet.md), and/or [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md) objects that identify the web requests that you want to allow, block, or count. For example, you might create a `Rule` that includes the following predicates:
+ An `IPSet` that causes AWS WAF to search for web requests that originate from the IP address `192.0.2.44`
+ A `ByteMatchSet` that causes AWS WAF to search for web requests for which the value of the `User-Agent` header is `BadBot`.

To match the settings in this `Rule`, a request must originate from `192.0.2.44` AND include a `User-Agent` header for which the value is `BadBot`.

## Contents
<a name="API_waf_Rule_Contents"></a>

 ** Predicates **   <a name="WAF-Type-waf_Rule-Predicates"></a>
The `Predicates` object contains one `Predicate` element for each [ByteMatchSet](API_waf_ByteMatchSet.md), [IPSet](API_waf_IPSet.md), or [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md) object that you want to include in a `Rule`.
Type: Array of [Predicate](API_waf_Predicate.md) objects
Required: Yes

 ** RuleId **   <a name="WAF-Type-waf_Rule-RuleId"></a>
A unique identifier for a `Rule`. You use `RuleId` to get more information about a `Rule` (see [GetRule](API_waf_GetRule.md)), update a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), insert a `Rule` into a `WebACL` or delete a one from a `WebACL` (see [UpdateWebACL](API_waf_UpdateWebACL.md)), or delete a `Rule` from AWS WAF (see [DeleteRule](API_waf_DeleteRule.md)).
 `RuleId` is returned by [CreateRule](API_waf_CreateRule.md) and by [ListRules](API_waf_ListRules.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** MetricName **   <a name="WAF-Type-waf_Rule-MetricName"></a>
A friendly name or description for the metrics for this `Rule`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change `MetricName` after you create the `Rule`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="WAF-Type-waf_Rule-Name"></a>
The friendly name or description for the `Rule`. You can't change the name of a `Rule` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/Rule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
