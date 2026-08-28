---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_Statistics.html
---

# Statistics
<a name="API_Statistics"></a>

Contains statistics information. The DFE engine uses information about the data in your Neptune graph to make effective trade-offs when planning query execution. This information takes the form of statistics that include so-called characteristic sets and predicate statistics that can guide query planning. See [Managing statistics for the Neptune DFE to use](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html).

## Contents
<a name="API_Statistics_Contents"></a>

 ** active **   <a name="neptunedata-Type-Statistics-active"></a>
Indicates whether or not DFE statistics generation is enabled at all.
Type: Boolean
Required: No

 ** autoCompute **   <a name="neptunedata-Type-Statistics-autoCompute"></a>
Indicates whether or not automatic statistics generation is enabled.
Type: Boolean
Required: No

 ** date **   <a name="neptunedata-Type-Statistics-date"></a>
The UTC time at which DFE statistics have most recently been generated.
Type: Timestamp
Required: No

 ** note **   <a name="neptunedata-Type-Statistics-note"></a>
A note about problems in the case where statistics are invalid.
Type: String
Required: No

 ** signatureInfo **   <a name="neptunedata-Type-Statistics-signatureInfo"></a>
A StatisticsSummary structure that contains:
+  `signatureCount` - The total number of signatures across all characteristic sets.
+  `instanceCount` - The total number of characteristic-set instances.
+  `predicateCount` - The total number of unique predicates.
Type: [StatisticsSummary](API_StatisticsSummary.md) object
Required: No

 ** statisticsId **   <a name="neptunedata-Type-Statistics-statisticsId"></a>
Reports the ID of the current statistics generation run. A value of -1 indicates that no statistics have been generated.
Type: String
Required: No

## See Also
<a name="API_Statistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/Statistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/Statistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/Statistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
