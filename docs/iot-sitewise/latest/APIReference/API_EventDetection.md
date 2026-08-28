---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_EventDetection.html
---

# EventDetection
<a name="API_EventDetection"></a>

Configuration for event detection enrichment on video time-series data.

Event detection generates embeddings from video data enabling natural language similarity search on events. This allows customers to:
+ Query video events using semantic search after enrichment completes
+ Find relevant video segments through natural language queries
+ Search across video time-series data stored in IoT SiteWise

You must specify the dataset, exactly one time-series identifier (timeSeriesId OR propertyAlias), and trim settings defining the video time window to process.

## Contents
<a name="API_EventDetection_Contents"></a>

 ** datasetId **   <a name="iotsitewise-Type-EventDetection-datasetId"></a>
The IoT SiteWise dataset ID containing the video time-series data to analyze. Query IoT SiteWise to discover available datasets in your workspace.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** trimSettings **   <a name="iotsitewise-Type-EventDetection-trimSettings"></a>
Time range settings defining which portion of the video time-series data to process. Required to ensure predictable processing time and prevent analyzing unbounded datasets. Start and end times must be within the dataset's time bounds.
Type: [EnrichmentTrimSettings](API_EnrichmentTrimSettings.md) object
Required: Yes

 ** propertyAlias **   <a name="iotsitewise-Type-EventDetection-propertyAlias"></a>
Human-readable alias for the video time series to analyze (e.g., /camera/warehouse/zone-a). Specify either propertyAlias or timeSeriesId, but not both. Use this when you have configured friendly aliases in IoT SiteWise for better readability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** timeSeriesId **   <a name="iotsitewise-Type-EventDetection-timeSeriesId"></a>
Unique system identifier for the video time series to analyze. Specify either timeSeriesId or propertyAlias, but not both. Use this when you have the system-generated time series identifier from IoT SiteWise.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: No

## See Also
<a name="API_EventDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/EventDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/EventDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/EventDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
