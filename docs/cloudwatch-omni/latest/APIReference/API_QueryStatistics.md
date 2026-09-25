---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_QueryStatistics.html
---

# QueryStatistics
<a name="API_QueryStatistics"></a>

Statistics about a telemetry query execution.

## Contents
<a name="API_QueryStatistics_Contents"></a>

 ** bytesScanned **   <a name="cloudwatchomni-Type-QueryStatistics-bytesScanned"></a>
The number of bytes scanned by the query.
Type: Double
Required: No

 ** partialResults **   <a name="cloudwatchomni-Type-QueryStatistics-partialResults"></a>
Information about whether the query returned partial results.
Type: [PartialResults](API_PartialResults.md) object
Required: No

 ** percentComplete **   <a name="cloudwatchomni-Type-QueryStatistics-percentComplete"></a>
The percentage of the query that has completed.
Type: Integer
Required: No

 ** recordsMatched **   <a name="cloudwatchomni-Type-QueryStatistics-recordsMatched"></a>
The number of records that matched the query criteria.
Type: Long
Required: No

 ** recordsScanned **   <a name="cloudwatchomni-Type-QueryStatistics-recordsScanned"></a>
The total number of records scanned.
Type: Long
Required: No

## See Also
<a name="API_QueryStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/QueryStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/QueryStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/QueryStatistics)
