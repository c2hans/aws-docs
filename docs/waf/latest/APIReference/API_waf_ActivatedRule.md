---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ActivatedRule.html
---

# ActivatedRule
<a name="API_waf_ActivatedRule"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The `ActivatedRule` object in an [UpdateWebACL](API_waf_UpdateWebACL.md) request specifies a `Rule` that you want to insert or delete, the priority of the `Rule` in the `WebACL`, and the action that you want AWS WAF to take when a web request matches the `Rule` (`ALLOW`, `BLOCK`, or `COUNT`).

To specify whether to insert or delete a `Rule`, use the `Action` parameter in the [WebACLUpdate](API_waf_WebACLUpdate.md) data type.

## Contents
<a name="API_waf_ActivatedRule_Contents"></a>

 ** Priority **   <a name="WAF-Type-waf_ActivatedRule-Priority"></a>
Specifies the order in which the `Rules` in a `WebACL` are evaluated. Rules with a lower value for `Priority` are evaluated before `Rules` with a higher value. The value must be a unique integer. If you add multiple `Rules` to a `WebACL`, the values don't need to be consecutive.
Type: Integer
Required: Yes

 ** RuleId **   <a name="WAF-Type-waf_ActivatedRule-RuleId"></a>
The `RuleId` for a `Rule`. You use `RuleId` to get more information about a `Rule` (see [GetRule](API_waf_GetRule.md)), update a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), insert a `Rule` into a `WebACL` or delete a one from a `WebACL` (see [UpdateWebACL](API_waf_UpdateWebACL.md)), or delete a `Rule` from AWS WAF (see [DeleteRule](API_waf_DeleteRule.md)).
 `RuleId` is returned by [CreateRule](API_waf_CreateRule.md) and by [ListRules](API_waf_ListRules.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Action **   <a name="WAF-Type-waf_ActivatedRule-Action"></a>
Specifies the action that Amazon CloudFront or AWS WAF takes when a web request matches the conditions in the `Rule`. Valid values for `Action` include the following:
+  `ALLOW`: CloudFront responds with the requested object.
+  `BLOCK`: CloudFront responds with an HTTP 403 (Forbidden) status code.
+  `COUNT`: AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.
 `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL`. In this case, you do not use `ActivatedRule|Action`. For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.
Type: [WafAction](API_waf_WafAction.md) object
Required: No

 ** ExcludedRules **   <a name="WAF-Type-waf_ActivatedRule-ExcludedRules"></a>
An array of rules to exclude from a rule group. This is applicable only when the `ActivatedRule` refers to a `RuleGroup`.
Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
Specifying `ExcludedRules` does not remove those rules from the rule group. Rather, it changes the action for the rules to `COUNT`. Therefore, requests that match an `ExcludedRule` are counted but not blocked. The `RuleGroup` owner will receive COUNT metrics for each `ExcludedRule`.
If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

1. Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html).

1. Submit an [UpdateWebACL](API_waf_UpdateWebACL.md) request that has two actions:
   + The first action deletes the existing rule group from the web ACL. That is, in the [UpdateWebACL](API_waf_UpdateWebACL.md) request, the first `Updates:Action` should be `DELETE` and `Updates:ActivatedRule:RuleId` should be the rule group that contains the rules that you want to exclude.
   + The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second `Updates:Action` should be `INSERT`, `Updates:ActivatedRule:RuleId` should be the rule group that you just removed, and `ExcludedRules` should contain the rules that you want to exclude.
Type: Array of [ExcludedRule](API_waf_ExcludedRule.md) objects
Required: No

 ** OverrideAction **   <a name="WAF-Type-waf_ActivatedRule-OverrideAction"></a>
Use the `OverrideAction` to test your `RuleGroup`.
Any rule in a `RuleGroup` can potentially block a request. If you set the `OverrideAction` to `None`, the `RuleGroup` will block a request if any individual rule in the `RuleGroup` matches the request and is configured to block that request. However if you first want to test the `RuleGroup`, set the `OverrideAction` to `Count`. The `RuleGroup` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using [GetSampledRequests](API_waf_GetSampledRequests.md).
 `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL`. In this case you do not use `ActivatedRule|Action`. For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.
Type: [WafOverrideAction](API_waf_WafOverrideAction.md) object
Required: No

 ** Type **   <a name="WAF-Type-waf_ActivatedRule-Type"></a>
The rule type, either `REGULAR`, as defined by [Rule](API_waf_Rule.md), `RATE_BASED`, as defined by [RateBasedRule](API_waf_RateBasedRule.md), or `GROUP`, as defined by [RuleGroup](API_waf_RuleGroup.md). The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE\_BASED rule to a web ACL without setting the type, the [UpdateWebACL](API_waf_UpdateWebACL.md) request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.
Type: String
Valid Values: `REGULAR | RATE_BASED | GROUP`
Required: No

## See Also
<a name="API_waf_ActivatedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ActivatedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ActivatedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ActivatedRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
