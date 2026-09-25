---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

Summary information about a rule.

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** ruleArn **   <a name="networksecuritymanager-Type-RuleSummary-ruleArn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** ruleId **   <a name="networksecuritymanager-Type-RuleSummary-ruleId"></a>
The service-generated id of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** ruleName **   <a name="networksecuritymanager-Type-RuleSummary-ruleName"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: Yes

 ** firewallType **   <a name="networksecuritymanager-Type-RuleSummary-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF`
Required: No

 ** hasPublishedVersion **   <a name="networksecuritymanager-Type-RuleSummary-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean
Required: No

 ** ruleType **   <a name="networksecuritymanager-Type-RuleSummary-ruleType"></a>
The type of the rule. `CONFIGURATION` rules contain firewall settings, and `INSPECTION` rules contain rule groups.
Type: String
Valid Values: `CONFIGURATION | INSPECTION`
Required: No

 ** status **   <a name="networksecuritymanager-Type-RuleSummary-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`
Required: No

 ** updatedAt **   <a name="networksecuritymanager-Type-RuleSummary-updatedAt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.
Type: Timestamp
Required: No

 ** version **   <a name="networksecuritymanager-Type-RuleSummary-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/RuleSummary)
