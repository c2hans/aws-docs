---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DataSegmentSummary.html
---

# DataSegmentSummary
<a name="API_DataSegmentSummary"></a>

Contains summary information about a data segment, including its source dataset, time series, timestamp range, and enrichment status.

## Contents
<a name="API_DataSegmentSummary_Contents"></a>

 ** alias **   <a name="iotsitewise-Type-DataSegmentSummary-alias"></a>
The alias of the time series.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** dataType **   <a name="iotsitewise-Type-DataSegmentSummary-dataType"></a>
The data type of the time series.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`
Required: Yes

 ** endTimestamp **   <a name="iotsitewise-Type-DataSegmentSummary-endTimestamp"></a>
The nanosecond-precision end time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** sourceDatasetId **   <a name="iotsitewise-Type-DataSegmentSummary-sourceDatasetId"></a>
The ID of the source dataset that contains the data segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** startTimestamp **   <a name="iotsitewise-Type-DataSegmentSummary-startTimestamp"></a>
The nanosecond-precision start time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-DataSegmentSummary-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

 ** enrichment **   <a name="iotsitewise-Type-DataSegmentSummary-enrichment"></a>
The enrichment information for the data segment.
Type: [DataSegmentEnrichment](API_DataSegmentEnrichment.md) object
Required: No

## See Also
<a name="API_DataSegmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DataSegmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DataSegmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DataSegmentSummary)
