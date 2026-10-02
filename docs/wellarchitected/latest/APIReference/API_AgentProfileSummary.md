---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentProfileSummary.html
---

# AgentProfileSummary
<a name="API_AgentProfileSummary"></a>

Summary of an optimization profile, including its configuration, metadata, and audit information.

## Contents
<a name="API_AgentProfileSummary_Contents"></a>

 ** arn **   <a name="wellarchitected-Type-AgentProfileSummary-arn"></a>
The Amazon Resource Name (ARN) of the optimization profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** createdAt **   <a name="wellarchitected-Type-AgentProfileSummary-createdAt"></a>
The timestamp when the profile was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-AgentProfileSummary-createdBy"></a>
The identifier of the user or system that created this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** name **   <a name="wellarchitected-Type-AgentProfileSummary-name"></a>
The system name of the profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** aggregationConfiguration **   <a name="wellarchitected-Type-AgentProfileSummary-aggregationConfiguration"></a>
The aggregation configuration that defines which AWS accounts and Regions to analyze. Not present for basic profiles.
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** businessOverview **   <a name="wellarchitected-Type-AgentProfileSummary-businessOverview"></a>
The business overview for this profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** deletionProtection **   <a name="wellarchitected-Type-AgentProfileSummary-deletionProtection"></a>
Indicates whether deletion protection is enabled for the profile.
Type: Boolean
Required: No

 ** description **   <a name="wellarchitected-Type-AgentProfileSummary-description"></a>
A description of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: No

 ** displayName **   <a name="wellarchitected-Type-AgentProfileSummary-displayName"></a>
The display name of the profile shown to users.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** eligibleForArchitectureGeneration **   <a name="wellarchitected-Type-AgentProfileSummary-eligibleForArchitectureGeneration"></a>
Indicates whether the profile is valid for manual architecture generation.
Type: Boolean
Required: No

 ** eligibleForScheduledGeneration **   <a name="wellarchitected-Type-AgentProfileSummary-eligibleForScheduledGeneration"></a>
Indicates whether the profile is valid for scheduled recommendation generation.
Type: Boolean
Required: No

 ** executionRoleArn **   <a name="wellarchitected-Type-AgentProfileSummary-executionRoleArn"></a>
The ARN of the IAM execution role used for recommendation actions. Not present for basic profiles.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:([a-z\-]+):iam::\d{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+`
Required: No

 ** fieldErrors **   <a name="wellarchitected-Type-AgentProfileSummary-fieldErrors"></a>
A map of field paths to error messages for invalid or missing input fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-AgentProfileSummary-lastModifiedAt"></a>
The timestamp when the profile was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-AgentProfileSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** organizationalAggregationConfiguration **   <a name="wellarchitected-Type-AgentProfileSummary-organizationalAggregationConfiguration"></a>
This is not available during the preview release.
The organizational monitoring boundary. Present only for organizational profiles.
Type: [OrganizationalAggregationConfiguration](API_OrganizationalAggregationConfiguration.md) object
Required: No

 ** pillars **   <a name="wellarchitected-Type-AgentProfileSummary-pillars"></a>
The AWS Well-Architected Framework pillars associated with this profile. Not present for basic profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: No

 ** profileType **   <a name="wellarchitected-Type-AgentProfileSummary-profileType"></a>
The type of the profile. `ORGANIZATIONAL` is not available during the preview release.
Type: String
Valid Values: `STANDARD | BASIC | ORGANIZATIONAL`
Required: No

 ** tags **   <a name="wellarchitected-Type-AgentProfileSummary-tags"></a>
The tags associated with the profile.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_AgentProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AgentProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AgentProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AgentProfileSummary)
