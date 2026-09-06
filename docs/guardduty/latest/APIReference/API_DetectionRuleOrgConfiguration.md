---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleOrgConfiguration.html
---

# DetectionRuleOrgConfiguration
<a name="API_DetectionRuleOrgConfiguration"></a>

Contains the organization-level configuration for a custom detection rule.

## Contents
<a name="API_DetectionRuleOrgConfiguration_Contents"></a>

 ** createdAt **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-createdAt"></a>
The timestamp when the organization configuration was created.
Type: Timestamp
Required: Yes

 ** excludeAccountIds **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-excludeAccountIds"></a>
A list of member account IDs excluded from the organization configuration. Mutually exclusive with `IncludeAccountIds`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50000 items.
Length Constraints: Fixed length of 12.
Required: Yes

 ** includeAccountIds **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-includeAccountIds"></a>
A list of member account IDs included in the organization configuration. Mutually exclusive with `ExcludeAccountIds`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50000 items.
Length Constraints: Fixed length of 12.
Required: Yes

 ** mode **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-mode"></a>
The execution mode of the organization configuration. Valid values: `LIVE` \| `DRY_RUN`.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** ruleId **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-ruleId"></a>
The unique identifier for the custom detection rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** status **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-status"></a>
The configuration status. Valid values: `ACTIVE` \| `PROCESSING` \| `FAILED`.
Type: String
Valid Values: `ACTIVE | PROCESSING | FAILED`
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-updatedAt"></a>
The timestamp when the organization configuration was last updated.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-expiresAt"></a>
The timestamp when the organization configuration expires.
Type: Timestamp
Required: No

 ** statusReason **   <a name="guardduty-Type-DetectionRuleOrgConfiguration-statusReason"></a>
The reason for the current configuration status.
Type: String
Required: No

## See Also
<a name="API_DetectionRuleOrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleOrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleOrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleOrgConfiguration)
