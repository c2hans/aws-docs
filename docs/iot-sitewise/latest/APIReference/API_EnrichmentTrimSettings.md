---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_EnrichmentTrimSettings.html
---

# EnrichmentTrimSettings
<a name="API_EnrichmentTrimSettings"></a>

Time range settings for extracting a specific window of video time-series data to process.

Trim settings define the time bounds for enrichment and must satisfy:
+ Start and end times must be within the dataset's time bounds
+ Trim settings retrieve fully contained data segments within the specified time range
+ endTime must be greater than startTime
+ Both times should represent valid data ranges in the dataset

Trim settings are required to:
+ Prevent accidentally analyzing unbounded datasets
+ Ensure predictable processing time and costs
+ Allow focused analysis on specific time periods of interest

## Contents
<a name="API_EnrichmentTrimSettings_Contents"></a>

 ** endTime **   <a name="iotsitewise-Type-EnrichmentTrimSettings-endTime"></a>
End time for the video analysis time range in nanoseconds since Unix epoch (TimeInNanos format). Data segments at or before this time are included in the enrichment. Must be greater than startTime and within the dataset's time bounds.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** startTime **   <a name="iotsitewise-Type-EnrichmentTrimSettings-startTime"></a>
Start time for the video analysis time range in nanoseconds since Unix epoch (TimeInNanos format). Data segments at or after this time are included in the enrichment. Must be within the dataset's time bounds.
Example (JavaScript): Date.parse('2024-01-01T00:00:00Z') \* 1000000 Example (Python): int(datetime.timestamp() \* 1e9)
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

## See Also
<a name="API_EnrichmentTrimSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/EnrichmentTrimSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/EnrichmentTrimSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/EnrichmentTrimSettings)
