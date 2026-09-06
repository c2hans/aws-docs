---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingStatistics.html
---

# FindingStatistics
<a name="API_FindingStatistics"></a>

Contains information about finding statistics.

## Contents
<a name="API_FindingStatistics_Contents"></a>

 ** countBySeverity **   <a name="guardduty-Type-FindingStatistics-countBySeverity"></a>
 *This member has been deprecated.*
Represents a list of map of severity to count statistics for a set of findings.
Type: String to integer map
Required: No

 ** groupedByAccount **   <a name="guardduty-Type-FindingStatistics-groupedByAccount"></a>
Represents a list of map of accounts with a findings count associated with each account.
Type: Array of [AccountStatistics](API_AccountStatistics.md) objects
Required: No

 ** groupedByDate **   <a name="guardduty-Type-FindingStatistics-groupedByDate"></a>
Represents a list of map of dates with a count of total findings generated on each date per severity level.
Type: Array of [DateStatistics](API_DateStatistics.md) objects
Required: No

 ** groupedByFindingType **   <a name="guardduty-Type-FindingStatistics-groupedByFindingType"></a>
Represents a list of map of finding types with a count of total findings generated for each type.
Based on the `orderBy` parameter, this request returns either the most occurring finding types or the least occurring finding types. If the `orderBy` parameter is `ASC`, this will represent the least occurring finding types in your account; otherwise, this will represent the most occurring finding types. The default value of `orderBy` is `DESC`.
Type: Array of [FindingTypeStatistics](API_FindingTypeStatistics.md) objects
Required: No

 ** groupedByResource **   <a name="guardduty-Type-FindingStatistics-groupedByResource"></a>
Represents a list of map of top resources with a count of total findings.
Type: Array of [ResourceStatistics](API_ResourceStatistics.md) objects
Required: No

 ** groupedBySeverity **   <a name="guardduty-Type-FindingStatistics-groupedBySeverity"></a>
Represents a list of map of total findings for each severity level.
Type: Array of [SeverityStatistics](API_SeverityStatistics.md) objects
Required: No

## See Also
<a name="API_FindingStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingStatistics)
