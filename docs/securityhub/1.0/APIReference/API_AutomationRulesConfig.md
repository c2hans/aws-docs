---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesConfig.html
---

# AutomationRulesConfig
<a name="API_AutomationRulesConfig"></a>

 Defines the configuration of an automation rule.

## Contents
<a name="API_AutomationRulesConfig_Contents"></a>

 ** Actions **   <a name="securityhub-Type-AutomationRulesConfig-Actions"></a>
 One or more actions to update finding fields if a finding matches the defined criteria of the rule.
Type: Array of [AutomationRulesAction](API_AutomationRulesAction.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AutomationRulesConfig-CreatedAt"></a>
 A timestamp that indicates when the rule was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="securityhub-Type-AutomationRulesConfig-CreatedBy"></a>
 The principal that created a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Criteria **   <a name="securityhub-Type-AutomationRulesConfig-Criteria"></a>
 A set of [AWS Security Finding Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding.
Type: [AutomationRulesFindingFilters](API_AutomationRulesFindingFilters.md) object
Required: No

 ** Description **   <a name="securityhub-Type-AutomationRulesConfig-Description"></a>
 A description of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IsTerminal **   <a name="securityhub-Type-AutomationRulesConfig-IsTerminal"></a>
Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
Type: Boolean
Required: No

 ** RuleArn **   <a name="securityhub-Type-AutomationRulesConfig-RuleArn"></a>
 The Amazon Resource Name (ARN) of a rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleName **   <a name="securityhub-Type-AutomationRulesConfig-RuleName"></a>
 The name of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleOrder **   <a name="securityhub-Type-AutomationRulesConfig-RuleOrder"></a>
 An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** RuleStatus **   <a name="securityhub-Type-AutomationRulesConfig-RuleStatus"></a>
 Whether the rule is active after it is created. If this parameter is equal to `ENABLED`, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AutomationRulesConfig-UpdatedAt"></a>
 A timestamp that indicates when the rule was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

## See Also
<a name="API_AutomationRulesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
