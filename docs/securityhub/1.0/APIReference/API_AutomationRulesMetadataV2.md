---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesMetadataV2.html
---

# AutomationRulesMetadataV2
<a name="API_AutomationRulesMetadataV2"></a>

Includes essential metadata information about automation rules.

## Contents
<a name="API_AutomationRulesMetadataV2_Contents"></a>

 ** Actions **   <a name="securityhub-Type-AutomationRulesMetadataV2-Actions"></a>
The list of action to be performed when the rule criteria is met.
Type: Array of [AutomationRulesActionTypeObjectV2](API_AutomationRulesActionTypeObjectV2.md) objects
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AutomationRulesMetadataV2-CreatedAt"></a>
The timestamp for when the automation rule was created.
Type: Timestamp
Required: No

 ** Description **   <a name="securityhub-Type-AutomationRulesMetadataV2-Description"></a>
An explanation for the purpose and funcitonality of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleArn **   <a name="securityhub-Type-AutomationRulesMetadataV2-RuleArn"></a>
The ARN of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleId **   <a name="securityhub-Type-AutomationRulesMetadataV2-RuleId"></a>
The ID of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleName **   <a name="securityhub-Type-AutomationRulesMetadataV2-RuleName"></a>
The name of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleOrder **   <a name="securityhub-Type-AutomationRulesMetadataV2-RuleOrder"></a>
The value for the rule priority.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 1000.0.
Required: No

 ** RuleStatus **   <a name="securityhub-Type-AutomationRulesMetadataV2-RuleStatus"></a>
The status of the automation rule.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AutomationRulesMetadataV2-UpdatedAt"></a>
The timestamp for the most recent modification to the automation rule.
Type: Timestamp
Required: No

## See Also
<a name="API_AutomationRulesMetadataV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesMetadataV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesMetadataV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesMetadataV2)
