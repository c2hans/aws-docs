---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TelemetrySinkConfig.html
---

# TelemetrySinkConfig
<a name="API_TelemetrySinkConfig"></a>

Information about a telemetry sink `Config`.

## Contents
<a name="API_TelemetrySinkConfig_Contents"></a>

 ** telemetrySinkData **   <a name="groundstation-Type-TelemetrySinkConfig-telemetrySinkData"></a>
Information about the telemetry sink specified by the `telemetrySinkType`.
Type: [TelemetrySinkData](API_TelemetrySinkData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** telemetrySinkType **   <a name="groundstation-Type-TelemetrySinkConfig-telemetrySinkType"></a>
The type of telemetry sink.
Type: String
Valid Values: `KINESIS_DATA_STREAM`
Required: Yes

## See Also
<a name="API_TelemetrySinkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/TelemetrySinkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/TelemetrySinkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/TelemetrySinkConfig)
