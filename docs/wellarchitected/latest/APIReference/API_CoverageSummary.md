---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CoverageSummary.html
---

# CoverageSummary
<a name="API_CoverageSummary"></a>

**Important**
This is not available during the preview release.

Counts describing the coverage of a completed Organizational Report. Includes the number of accounts in scope, how many had a profile, how many failed, and aggregated recommendation counts by pillar and priority. Returned only by GetAgentOrganizationalReport after the report reaches COMPLETED status. Not returned on the list response.

## Contents
<a name="API_CoverageSummary_Contents"></a>

 ** accountsWithoutProfile **   <a name="wellarchitected-Type-CoverageSummary-accountsWithoutProfile"></a>
Number of in-scope accounts that had no Agent Profile at the time of the snapshot.
Type: Long
Required: Yes

 ** accountsWithProfile **   <a name="wellarchitected-Type-CoverageSummary-accountsWithProfile"></a>
Number of in-scope accounts that had an Agent Profile and were successfully processed.
Type: Long
Required: Yes

 ** failedAccountCount **   <a name="wellarchitected-Type-CoverageSummary-failedAccountCount"></a>
Number of in-scope accounts that errored during processing. Equal to the length of failedAccounts.
Type: Long
Required: Yes

 ** totalAccountsInScope **   <a name="wellarchitected-Type-CoverageSummary-totalAccountsInScope"></a>
Total number of accounts that were in scope for the report after applying all filters and AWS Organizations membership validation.
Type: Long
Required: Yes

 ** totalProfiles **   <a name="wellarchitected-Type-CoverageSummary-totalProfiles"></a>
Total number of Agent Profiles contributing to the report.
Type: Long
Required: Yes

 ** totalRecommendations **   <a name="wellarchitected-Type-CoverageSummary-totalRecommendations"></a>
Total number of recommendations included in the report across all profiles and all pillars.
Type: Long
Required: Yes

 ** failedAccounts **   <a name="wellarchitected-Type-CoverageSummary-failedAccounts"></a>
Accounts that errored during processing and the reason they failed.
Type: Array of [FailedAccount](API_FailedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** failedOrganizationalUnits **   <a name="wellarchitected-Type-CoverageSummary-failedOrganizationalUnits"></a>
Organizational units named in the report's filters that could not be expanded into their member accounts, along with the reason each failed. A failed OU means the report is missing whatever accounts it contained. Absent or empty when every requested OU expanded successfully.
Type: Array of [FailedOrganizationalUnit](API_FailedOrganizationalUnit.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** recommendationCountByPillar **   <a name="wellarchitected-Type-CoverageSummary-recommendationCountByPillar"></a>
Recommendation count grouped by Well-Architected pillar. Each entry pairs a Pillar enum value with a non-negative long. The counts sum to totalRecommendations.
Type: Array of [PillarCount](API_PillarCount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** recommendationCountByPriority **   <a name="wellarchitected-Type-CoverageSummary-recommendationCountByPriority"></a>
Recommendation count grouped by Priority. Each entry pairs a Priority enum value with a non-negative long. The counts sum to totalRecommendations.
Type: Array of [PriorityCount](API_PriorityCount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CoverageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CoverageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CoverageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CoverageSummary)
