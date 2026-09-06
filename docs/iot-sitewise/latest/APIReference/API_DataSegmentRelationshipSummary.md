---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DataSegmentRelationshipSummary.html
---

# DataSegmentRelationshipSummary
<a name="API_DataSegmentRelationshipSummary"></a>

Contains summary information about a data segment relationship between a source session dataset that contains the data and a curated dataset that references it, including the time series and timestamp range.

## Contents
<a name="API_DataSegmentRelationshipSummary_Contents"></a>

 ** endTimestamp **   <a name="iotsitewise-Type-DataSegmentRelationshipSummary-endTimestamp"></a>
The nanosecond-precision end time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** sourceDatasetId **   <a name="iotsitewise-Type-DataSegmentRelationshipSummary-sourceDatasetId"></a>
The ID of the source session dataset that contains the data segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** startTimestamp **   <a name="iotsitewise-Type-DataSegmentRelationshipSummary-startTimestamp"></a>
The nanosecond-precision start time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** targetDatasetId **   <a name="iotsitewise-Type-DataSegmentRelationshipSummary-targetDatasetId"></a>
The ID of the curated dataset that references the data segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-DataSegmentRelationshipSummary-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

## See Also
<a name="API_DataSegmentRelationshipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DataSegmentRelationshipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DataSegmentRelationshipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DataSegmentRelationshipSummary)
