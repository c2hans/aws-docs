---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafWebAclRule.html
---

# AwsWafWebAclRule
<a name="API_AwsWafWebAclRule"></a>

Details for a rule in an AWS WAF web ACL.

## Contents
<a name="API_AwsWafWebAclRule_Contents"></a>

 ** Action **   <a name="securityhub-Type-AwsWafWebAclRule-Action"></a>
Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.
Type: [WafAction](API_WafAction.md) object
Required: No

 ** ExcludedRules **   <a name="securityhub-Type-AwsWafWebAclRule-ExcludedRules"></a>
Rules to exclude from a rule group.
Type: Array of [WafExcludedRule](API_WafExcludedRule.md) objects
Required: No

 ** OverrideAction **   <a name="securityhub-Type-AwsWafWebAclRule-OverrideAction"></a>
Use the `OverrideAction` to test your `RuleGroup`.
Any rule in a `RuleGroup` can potentially block a request. If you set the `OverrideAction` to `None`, the `RuleGroup` blocks a request if any individual rule in the `RuleGroup` matches the request and is configured to block that request.
However, if you first want to test the `RuleGroup`, set the `OverrideAction` to `Count`. The `RuleGroup` then overrides any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests are counted.
 `ActivatedRule`\|`OverrideAction` applies only when updating or adding a `RuleGroup` to a web ACL. In this case you don't use `ActivatedRule` `Action`. For all other update requests, `ActivatedRule` `Action` is used instead of `ActivatedRule` `OverrideAction`.
Type: [WafOverrideAction](API_WafOverrideAction.md) object
Required: No

 ** Priority **   <a name="securityhub-Type-AwsWafWebAclRule-Priority"></a>
Specifies the order in which the rules in a web ACL are evaluated. Rules with a lower value for `Priority` are evaluated before rules with a higher value. The value must be a unique integer. If you add multiple rules to a web ACL, the values don't need to be consecutive.
Type: Integer
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafWebAclRule-RuleId"></a>
The identifier for a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafWebAclRule-Type"></a>
The rule type.
Valid values: `REGULAR` \| `RATE_BASED` \| `GROUP`
The default is `REGULAR`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafWebAclRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafWebAclRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafWebAclRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafWebAclRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
