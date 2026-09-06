---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Workload.html
---

# Workload
<a name="API_Workload"></a>

A workload return object.

## Contents
<a name="API_Workload_Contents"></a>

 ** AccountIds **   <a name="wellarchitected-Type-Workload-AccountIds"></a>
The list of AWS account IDs associated with the workload.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** Applications **   <a name="wellarchitected-Type-Workload-Applications"></a>
List of AppRegistry application ARNs associated to the workload.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
Required: No

 ** ArchitecturalDesign **   <a name="wellarchitected-Type-Workload-ArchitecturalDesign"></a>
The URL of the architectural design for the workload.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(|(https?|ftp):\/\/[^\s/$.?#].[^\s]*)$`
Required: No

 ** AwsRegions **   <a name="wellarchitected-Type-Workload-AwsRegions"></a>
The list of AWS Regions associated with the workload, for example, `us-east-2`, or `ca-central-1`.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Maximum length of 100.
Required: No

 ** Description **   <a name="wellarchitected-Type-Workload-Description"></a>
The description for the workload.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Required: No

 ** DiscoveryConfig **   <a name="wellarchitected-Type-Workload-DiscoveryConfig"></a>
Discovery configuration associated to the workload.
Type: [WorkloadDiscoveryConfig](API_WorkloadDiscoveryConfig.md) object
Required: No

 ** Environment **   <a name="wellarchitected-Type-Workload-Environment"></a>
The environment for the workload.
Type: String
Valid Values: `PRODUCTION | PREPRODUCTION`
Required: No

 ** ImprovementStatus **   <a name="wellarchitected-Type-Workload-ImprovementStatus"></a>
The improvement status for a workload.
Type: String
Valid Values: `NOT_APPLICABLE | NOT_STARTED | IN_PROGRESS | COMPLETE | RISK_ACKNOWLEDGED`
Required: No

 ** Industry **   <a name="wellarchitected-Type-Workload-Industry"></a>
The industry for the workload.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** IndustryType **   <a name="wellarchitected-Type-Workload-IndustryType"></a>
The industry type for the workload.
If specified, must be one of the following:
+  `Agriculture`
+  `Automobile`
+  `Defense`
+  `Design and Engineering`
+  `Digital Advertising`
+  `Education`
+  `Environmental Protection`
+  `Financial Services`
+  `Gaming`
+  `General Public Services`
+  `Healthcare`
+  `Hospitality`
+  `InfoTech`
+  `Justice and Public Safety`
+  `Life Sciences`
+  `Manufacturing`
+  `Media & Entertainment`
+  `Mining & Resources`
+  `Oil & Gas`
+  `Power & Utilities`
+  `Professional Services`
+  `Real Estate & Construction`
+  `Retail & Wholesale`
+  `Social Protection`
+  `Telecommunications`
+  `Travel, Transportation & Logistics`
+  `Other`
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** IsReviewOwnerUpdateAcknowledged **   <a name="wellarchitected-Type-Workload-IsReviewOwnerUpdateAcknowledged"></a>
Flag indicating whether the workload owner has acknowledged that the *Review owner* field is required.
If a **Review owner** is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.
Type: Boolean
Required: No

 ** JiraConfiguration **   <a name="wellarchitected-Type-Workload-JiraConfiguration"></a>
Jira configuration for a specific workload.
Type: [WorkloadJiraConfigurationOutput](API_WorkloadJiraConfigurationOutput.md) object
Required: No

 ** Lenses **   <a name="wellarchitected-Type-Workload-Lenses"></a>
The list of lenses associated with the workload. Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
If a review template that specifies lenses is applied to the workload, those lenses are applied to the workload in addition to these lenses.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** NonAwsRegions **   <a name="wellarchitected-Type-Workload-NonAwsRegions"></a>
 The list of non-AWS Regions associated with the workload.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 3. Maximum length of 25.
Required: No

 ** Notes **   <a name="wellarchitected-Type-Workload-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** Owner **   <a name="wellarchitected-Type-Workload-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** PillarPriorities **   <a name="wellarchitected-Type-Workload-PillarPriorities"></a>
The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** PrioritizedRiskCounts **   <a name="wellarchitected-Type-Workload-PrioritizedRiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** Profiles **   <a name="wellarchitected-Type-Workload-Profiles"></a>
Profile associated with a workload.
Type: Array of [WorkloadProfile](API_WorkloadProfile.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ReviewOwner **   <a name="wellarchitected-Type-Workload-ReviewOwner"></a>
The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** ReviewRestrictionDate **   <a name="wellarchitected-Type-Workload-ReviewRestrictionDate"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-Workload-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-Workload-ShareInvitationId"></a>
The ID assigned to the share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Tags **   <a name="wellarchitected-Type-Workload-Tags"></a>
The tags associated with the workload.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-Workload-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** WorkloadArn **   <a name="wellarchitected-Type-Workload-WorkloadArn"></a>
The ARN for the workload.
Type: String
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-Workload-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-Workload-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_Workload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Workload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Workload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Workload)
