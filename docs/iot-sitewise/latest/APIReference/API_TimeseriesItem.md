---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeseriesItem.html
---

# TimeseriesItem
<a name="API_TimeseriesItem"></a>

A single timeseries item to process. Exactly one of timeSeriesId or propertyAlias must be provided.

## Contents
<a name="API_TimeseriesItem_Contents"></a>

 ** formatSettings **   <a name="iotsitewise-Type-TimeseriesItem-formatSettings"></a>
The optional format settings for the output.
Type: [FormatSettings](API_FormatSettings.md) object
Required: No

 ** propertyAlias **   <a name="iotsitewise-Type-TimeseriesItem-propertyAlias"></a>
The customer-friendly alias for the timeseries. Mutually exclusive with timeSeriesId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** timeSeriesId **   <a name="iotsitewise-Type-TimeseriesItem-timeSeriesId"></a>
The unique identifier for the timeseries. Mutually exclusive with propertyAlias.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: No

 ** trimSettings **   <a name="iotsitewise-Type-TimeseriesItem-trimSettings"></a>
The trim settings for the time range to export. Required for VIDEO and TELEMETRY data types; optional for ANNOTATION data types.
Type: [TrimSettings](API_TrimSettings.md) object
Required: No

## See Also
<a name="API_TimeseriesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TimeseriesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TimeseriesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TimeseriesItem)
