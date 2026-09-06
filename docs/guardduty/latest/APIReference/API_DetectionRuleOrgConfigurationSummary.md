---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleOrgConfigurationSummary.html
---

# DetectionRuleOrgConfigurationSummary
<a name="API_DetectionRuleOrgConfigurationSummary"></a>

Contains summary information about an organization-level configuration for a custom detection rule.

## Contents
<a name="API_DetectionRuleOrgConfigurationSummary_Contents"></a>

 ** createdAt **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-createdAt"></a>
The timestamp when the organization configuration was created.
Type: Timestamp
Required: Yes

 ** mode **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-mode"></a>
The rule execution mode.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** ruleId **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-ruleId"></a>
The unique identifier for the custom detection rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** status **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-status"></a>
The configuration status.
Type: String
Valid Values: `ACTIVE | PROCESSING | FAILED`
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-updatedAt"></a>
The timestamp when the organization configuration was last updated.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-expiresAt"></a>
The timestamp when the organization configuration expires.
Type: Timestamp
Required: No

 ** statusReason **   <a name="guardduty-Type-DetectionRuleOrgConfigurationSummary-statusReason"></a>
The reason for the current configuration status.
Type: String
Required: No

## See Also
<a name="API_DetectionRuleOrgConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleOrgConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleOrgConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleOrgConfigurationSummary)
