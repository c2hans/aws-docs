---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationFindingsSummary.html
---

# OrganizationFindingsSummary
<a name="API_OrganizationFindingsSummary"></a>

Contains a summary of findings across an organization.

## Contents
<a name="API_OrganizationFindingsSummary_Contents"></a>

 ** affectedAccountCount **   <a name="guardduty-Type-OrganizationFindingsSummary-affectedAccountCount"></a>
The number of accounts that have findings.
Type: Integer
Required: No

 ** byTimeWindow **   <a name="guardduty-Type-OrganizationFindingsSummary-byTimeWindow"></a>
The number of findings in each time window.
Type: Array of [TimeWindowGroup](API_TimeWindowGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** severityBreakdown **   <a name="guardduty-Type-OrganizationFindingsSummary-severityBreakdown"></a>
The number of findings at each severity level across the organization.
Type: [SeverityBreakdown](API_SeverityBreakdown.md) object
Required: No

 ** topFindingTypes **   <a name="guardduty-Type-OrganizationFindingsSummary-topFindingTypes"></a>
The finding types that have the most findings, with counts.
Type: Array of [FindingTypeCount](API_FindingTypeCount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** totalAccountCount **   <a name="guardduty-Type-OrganizationFindingsSummary-totalAccountCount"></a>
The total number of accounts in the organization.
Type: Integer
Required: No

 ** totalFindings **   <a name="guardduty-Type-OrganizationFindingsSummary-totalFindings"></a>
The total number of findings across the organization.
Type: Integer
Required: No

## See Also
<a name="API_OrganizationFindingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationFindingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationFindingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationFindingsSummary)
