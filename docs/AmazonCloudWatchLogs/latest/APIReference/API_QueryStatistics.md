---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryStatistics.html
---

# QueryStatistics
<a name="API_QueryStatistics"></a>

Contains the number of log events scanned by the query, the number of log events that matched the query criteria, and the total number of bytes in the log events that were scanned.

If the query involved log groups that have field index policies, the estimated number of skipped log events and the total bytes of those skipped log events are included. Using field indexes to skip log events in queries reduces scan volume and improves performance. For more information, see [Create field indexes to improve query performance and reduce scan volume](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html).

## Contents
<a name="API_QueryStatistics_Contents"></a>

 ** bytesScanned **   <a name="CWL-Type-QueryStatistics-bytesScanned"></a>
The total number of bytes in the log events scanned during the query.
Type: Double
Required: No

 ** estimatedBytesSkipped **   <a name="CWL-Type-QueryStatistics-estimatedBytesSkipped"></a>
An estimate of the number of bytes in the log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html).
Type: Double
Required: No

 ** estimatedRecordsSkipped **   <a name="CWL-Type-QueryStatistics-estimatedRecordsSkipped"></a>
An estimate of the number of log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html).
Type: Double
Required: No

 ** logGroupsScanned **   <a name="CWL-Type-QueryStatistics-logGroupsScanned"></a>
The number of log groups that were scanned by this query.
Type: Double
Required: No

 ** recordsMatched **   <a name="CWL-Type-QueryStatistics-recordsMatched"></a>
The number of log events that matched the query string.
Type: Double
Required: No

 ** recordsScanned **   <a name="CWL-Type-QueryStatistics-recordsScanned"></a>
The total number of log events scanned during the query.
Type: Double
Required: No

 ** resultCount **   <a name="CWL-Type-QueryStatistics-resultCount"></a>
The number of rows in the final query result set. This value represents the total number of output rows across all pages. For queries that include post-aggregation filters (such as `stats count(*) by field | filter count > threshold`), this value might be less than `recordsMatched`. It reflects only the rows that survived all operations in the query.
Type: Double
Required: No

## See Also
<a name="API_QueryStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/QueryStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/QueryStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/QueryStatistics)
