---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_WorkloadSummary.html
---

# WorkloadSummary
<a name="API_WorkloadSummary"></a>

A workload summary return object.

## Contents
<a name="API_WorkloadSummary_Contents"></a>

 ** ImprovementStatus **   <a name="wellarchitected-Type-WorkloadSummary-ImprovementStatus"></a>
The improvement status for a workload.
Type: String
Valid Values: `NOT_APPLICABLE | NOT_STARTED | IN_PROGRESS | COMPLETE | RISK_ACKNOWLEDGED`
Required: No

 ** Lenses **   <a name="wellarchitected-Type-WorkloadSummary-Lenses"></a>
The list of lenses associated with the workload. Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
If a review template that specifies lenses is applied to the workload, those lenses are applied to the workload in addition to these lenses.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Owner **   <a name="wellarchitected-Type-WorkloadSummary-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** PrioritizedRiskCounts **   <a name="wellarchitected-Type-WorkloadSummary-PrioritizedRiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** Profiles **   <a name="wellarchitected-Type-WorkloadSummary-Profiles"></a>
Profile associated with a workload.
Type: Array of [WorkloadProfile](API_WorkloadProfile.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-WorkloadSummary-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-WorkloadSummary-UpdatedAt"></a>
The date and time when the workload was last updated.
Type: Timestamp
Required: No

 ** WorkloadArn **   <a name="wellarchitected-Type-WorkloadSummary-WorkloadArn"></a>
The ARN for the workload.
Type: String
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-WorkloadSummary-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-WorkloadSummary-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_WorkloadSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/WorkloadSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/WorkloadSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/WorkloadSummary)
