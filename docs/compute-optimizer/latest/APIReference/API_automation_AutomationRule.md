---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationRule.html
---

# AutomationRule
<a name="API_automation_AutomationRule"></a>

Represents a complete automation rule configuration including criteria, schedule, and execution settings.

## Contents
<a name="API_automation_AutomationRule_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-automation_AutomationRule-accountId"></a>
The 12-digit AWS account ID that owns this automation rule.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** createdTimestamp **   <a name="computeoptimizer-Type-automation_AutomationRule-createdTimestamp"></a>
The timestamp when the automation rule was created.
Type: Timestamp
Required: No

 ** description **   <a name="computeoptimizer-Type-automation_AutomationRule-description"></a>
A description of the automation rule.
Type: String
Required: No

 ** lastUpdatedTimestamp **   <a name="computeoptimizer-Type-automation_AutomationRule-lastUpdatedTimestamp"></a>
The timestamp when the automation rule was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="computeoptimizer-Type-automation_AutomationRule-name"></a>
The name of the automation rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]*`
Required: No

 ** organizationConfiguration **   <a name="computeoptimizer-Type-automation_AutomationRule-organizationConfiguration"></a>
Configuration settings for organization-wide rules.
Type: [OrganizationConfiguration](API_automation_OrganizationConfiguration.md) object
Required: No

 ** priority **   <a name="computeoptimizer-Type-automation_AutomationRule-priority"></a>
A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules.
Type: String
Required: No

 ** recommendedActionTypes **   <a name="computeoptimizer-Type-automation_AutomationRule-recommendedActionTypes"></a>
List of recommended action types that this rule can execute.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: No

 ** ruleArn **   <a name="computeoptimizer-Type-automation_AutomationRule-ruleArn"></a>
The Amazon Resource Name (ARN) of the automation rule.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`
Required: No

 ** ruleId **   <a name="computeoptimizer-Type-automation_AutomationRule-ruleId"></a>
The unique identifier of the automation rule.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** ruleRevision **   <a name="computeoptimizer-Type-automation_AutomationRule-ruleRevision"></a>
The revision number of the automation rule.
Type: Long
Required: No

 ** ruleType **   <a name="computeoptimizer-Type-automation_AutomationRule-ruleType"></a>
The type of automation rule (OrganizationRule or AccountRule).
Type: String
Valid Values: `OrganizationRule | AccountRule`
Required: No

 ** schedule **   <a name="computeoptimizer-Type-automation_AutomationRule-schedule"></a>
The schedule configuration for when the automation rule should execute.
Type: [Schedule](API_automation_Schedule.md) object
Required: No

 ** status **   <a name="computeoptimizer-Type-automation_AutomationRule-status"></a>
The current status of the automation rule (Active or Inactive).
Type: String
Valid Values: `Active | Inactive`
Required: No

## See Also
<a name="API_automation_AutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AutomationRule)
