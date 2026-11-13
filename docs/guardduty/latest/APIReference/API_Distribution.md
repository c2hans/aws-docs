---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Distribution.html
---

# Distribution
<a name="API_Distribution"></a>

Contains a breakdown of findings along a dimension, such as severity or finding type.

## Contents
<a name="API_Distribution_Contents"></a>

 ** dimension **   <a name="guardduty-Type-Distribution-dimension"></a>
The dimension of the breakdown. The value identifies the breakdown that the record describes: `SEVERITY` (`SeverityBreakdown`), `TYPE` (`FindingTypes` or `TopFindingTypes`), `RESOURCE` (`Resources`), `ATTACK_VECTOR` (`AttackVectors`), and `ARCHIVE` (`Archive`).
Type: String
Valid Values: `SEVERITY | TYPE | RESOURCE | ATTACK_VECTOR | ARCHIVE`
Required: Yes

 ** archive **   <a name="guardduty-Type-Distribution-archive"></a>
The number and percentage of archived and unarchived findings.
Type: [ArchiveDistribution](API_ArchiveDistribution.md) object
Required: No

 ** attackVectors **   <a name="guardduty-Type-Distribution-attackVectors"></a>
The findings broken down by MITRE ATT&CK tactic.
Type: Array of [TacticCoverage](API_TacticCoverage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** findingTypes **   <a name="guardduty-Type-Distribution-findingTypes"></a>
The findings broken down by finding type, with counts and percentages.
Type: Array of [TypeDistribution](API_TypeDistribution.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** resources **   <a name="guardduty-Type-Distribution-resources"></a>
The findings broken down by affected resource.
Type: Array of [ResourceDistribution](API_ResourceDistribution.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** severityBreakdown **   <a name="guardduty-Type-Distribution-severityBreakdown"></a>
The number of findings at each severity level.
Type: [SeverityBreakdown](API_SeverityBreakdown.md) object
Required: No

 ** topFindingTypes **   <a name="guardduty-Type-Distribution-topFindingTypes"></a>
The finding types that have the most findings, with counts.
Type: Array of [FindingTypeCount](API_FindingTypeCount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** totalFindings **   <a name="guardduty-Type-Distribution-totalFindings"></a>
The total number of findings in the breakdown.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Distribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Distribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Distribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Distribution)
