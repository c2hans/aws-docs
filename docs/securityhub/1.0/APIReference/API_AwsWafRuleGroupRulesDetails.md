---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRuleGroupRulesDetails.html
---

# AwsWafRuleGroupRulesDetails
<a name="API_AwsWafRuleGroupRulesDetails"></a>

Provides information about the rules attached to the rule group. These rules identify the web requests that you want to allow, block, or count.

## Contents
<a name="API_AwsWafRuleGroupRulesDetails_Contents"></a>

 ** Action **   <a name="securityhub-Type-AwsWafRuleGroupRulesDetails-Action"></a>
Provides information about what action AWS WAF should take on a web request when it matches the criteria defined in the rule.
Type: [AwsWafRuleGroupRulesActionDetails](API_AwsWafRuleGroupRulesActionDetails.md) object
Required: No

 ** Priority **   <a name="securityhub-Type-AwsWafRuleGroupRulesDetails-Priority"></a>
If you define more than one rule in a web ACL, AWS WAF evaluates each request against the rules in order based on the value of `Priority`.
Type: Integer
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRuleGroupRulesDetails-RuleId"></a>
The rule ID for a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafRuleGroupRulesDetails-Type"></a>
The type of rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRuleGroupRulesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRuleGroupRulesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRuleGroupRulesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRuleGroupRulesDetails)
