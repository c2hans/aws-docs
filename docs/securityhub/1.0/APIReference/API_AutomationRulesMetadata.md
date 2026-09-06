---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesMetadata.html
---

# AutomationRulesMetadata
<a name="API_AutomationRulesMetadata"></a>

 Metadata for automation rules in the calling account. The response includes rules with a `RuleStatus` of `ENABLED` and `DISABLED`.

## Contents
<a name="API_AutomationRulesMetadata_Contents"></a>

 ** CreatedAt **   <a name="securityhub-Type-AutomationRulesMetadata-CreatedAt"></a>
 A timestamp that indicates when the rule was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="securityhub-Type-AutomationRulesMetadata-CreatedBy"></a>
 The principal that created a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AutomationRulesMetadata-Description"></a>
 A description of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IsTerminal **   <a name="securityhub-Type-AutomationRulesMetadata-IsTerminal"></a>
Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
Type: Boolean
Required: No

 ** RuleArn **   <a name="securityhub-Type-AutomationRulesMetadata-RuleArn"></a>
 The Amazon Resource Name (ARN) for the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleName **   <a name="securityhub-Type-AutomationRulesMetadata-RuleName"></a>
 The name of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleOrder **   <a name="securityhub-Type-AutomationRulesMetadata-RuleOrder"></a>
An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** RuleStatus **   <a name="securityhub-Type-AutomationRulesMetadata-RuleStatus"></a>
 Whether the rule is active after it is created. If this parameter is equal to `ENABLED`, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use [`BatchUpdateAutomationRules`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AutomationRulesMetadata-UpdatedAt"></a>
 A timestamp that indicates when the rule was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

## See Also
<a name="API_AutomationRulesMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesMetadata)
