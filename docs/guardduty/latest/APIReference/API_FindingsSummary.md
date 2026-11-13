---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingsSummary.html
---

# FindingsSummary
<a name="API_FindingsSummary"></a>

Contains a summary of findings.

## Contents
<a name="API_FindingsSummary_Contents"></a>

 ** byTimeWindow **   <a name="guardduty-Type-FindingsSummary-byTimeWindow"></a>
The number of findings in each time window.
Type: Array of [TimeWindowGroup](API_TimeWindowGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** severityBreakdown **   <a name="guardduty-Type-FindingsSummary-severityBreakdown"></a>
The number of findings at each severity level.
Type: [SeverityBreakdown](API_SeverityBreakdown.md) object
Required: No

 ** topFindingTypes **   <a name="guardduty-Type-FindingsSummary-topFindingTypes"></a>
The finding types that have the most findings, with counts.
Type: Array of [FindingTypeCount](API_FindingTypeCount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** totalFindings **   <a name="guardduty-Type-FindingsSummary-totalFindings"></a>
The total number of findings.
Type: Integer
Required: No

## See Also
<a name="API_FindingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingsSummary)
