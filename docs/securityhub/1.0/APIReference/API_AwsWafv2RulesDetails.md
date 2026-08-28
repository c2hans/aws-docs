---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2RulesDetails.html
---

# AwsWafv2RulesDetails
<a name="API_AwsWafv2RulesDetails"></a>

 Provides details about rules in a rule group. A rule identifies web requests that you want to allow, block, or count. Each rule includes one top-level Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

## Contents
<a name="API_AwsWafv2RulesDetails_Contents"></a>

 ** Action **   <a name="securityhub-Type-AwsWafv2RulesDetails-Action"></a>
 The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
Type: [AwsWafv2RulesActionDetails](API_AwsWafv2RulesActionDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafv2RulesDetails-Name"></a>
 The name of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OverrideAction **   <a name="securityhub-Type-AwsWafv2RulesDetails-OverrideAction"></a>
 The action to use in the place of the action that results from the rule group evaluation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Priority **   <a name="securityhub-Type-AwsWafv2RulesDetails-Priority"></a>
 If you define more than one Rule in a WebACL, AWS WAF evaluates each request against the Rules in order based on the value of `Priority`. AWS WAF processes rules with lower priority first. The priorities don't need to be consecutive, but they must all be different.
Type: Integer
Required: No

 ** VisibilityConfig **   <a name="securityhub-Type-AwsWafv2RulesDetails-VisibilityConfig"></a>
 Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [AwsWafv2VisibilityConfigDetails](API_AwsWafv2VisibilityConfigDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2RulesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2RulesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2RulesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2RulesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
