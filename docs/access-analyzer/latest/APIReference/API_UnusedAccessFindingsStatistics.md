---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAccessFindingsStatistics.html
---

# UnusedAccessFindingsStatistics
<a name="API_UnusedAccessFindingsStatistics"></a>

Provides aggregate statistics about the findings for the specified unused access analyzer.

## Contents
<a name="API_UnusedAccessFindingsStatistics_Contents"></a>

 ** topAccounts **   <a name="accessanalyzer-Type-UnusedAccessFindingsStatistics-topAccounts"></a>
A list of one to ten AWS accounts that have the most active findings for the unused access analyzer.
Type: Array of [FindingAggregationAccountDetails](API_FindingAggregationAccountDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** totalActiveFindings **   <a name="accessanalyzer-Type-UnusedAccessFindingsStatistics-totalActiveFindings"></a>
The total number of active findings for the unused access analyzer.
Type: Integer
Required: No

 ** totalArchivedFindings **   <a name="accessanalyzer-Type-UnusedAccessFindingsStatistics-totalArchivedFindings"></a>
The total number of archived findings for the unused access analyzer.
Type: Integer
Required: No

 ** totalResolvedFindings **   <a name="accessanalyzer-Type-UnusedAccessFindingsStatistics-totalResolvedFindings"></a>
The total number of resolved findings for the unused access analyzer.
Type: Integer
Required: No

 ** unusedAccessTypeStatistics **   <a name="accessanalyzer-Type-UnusedAccessFindingsStatistics-unusedAccessTypeStatistics"></a>
A list of details about the total number of findings for each type of unused access for the analyzer.
Type: Array of [UnusedAccessTypeStatistics](API_UnusedAccessTypeStatistics.md) objects
Required: No

## See Also
<a name="API_UnusedAccessFindingsStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)
