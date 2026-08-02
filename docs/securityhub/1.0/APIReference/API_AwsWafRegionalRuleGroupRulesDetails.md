---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalRuleGroupRulesDetails.html
---

# AwsWafRegionalRuleGroupRulesDetails
<a name="API_AwsWafRegionalRuleGroupRulesDetails"></a>

Provides information about the rules attached to a rule group

## Contents
<a name="API_AwsWafRegionalRuleGroupRulesDetails_Contents"></a>

 ** Action **   <a name="securityhub-Type-AwsWafRegionalRuleGroupRulesDetails-Action"></a>
The action that AWS WAF should take on a web request when it matches the criteria defined in the rule.
Type: [AwsWafRegionalRuleGroupRulesActionDetails](API_AwsWafRegionalRuleGroupRulesActionDetails.md) object
Required: No

 ** Priority **   <a name="securityhub-Type-AwsWafRegionalRuleGroupRulesDetails-Priority"></a>
If you define more than one rule in a web ACL, AWS WAF evaluates each request against the rules in order based on the value of `Priority`.
Type: Integer
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRegionalRuleGroupRulesDetails-RuleId"></a>
The ID for a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafRegionalRuleGroupRulesDetails-Type"></a>
The type of rule in the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalRuleGroupRulesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalRuleGroupRulesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalRuleGroupRulesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalRuleGroupRulesDetails)
