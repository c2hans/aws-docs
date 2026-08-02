---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTrafficOptions.html
---

# IsolineTrafficOptions
<a name="API_IsolineTrafficOptions"></a>

Controls how real-time and historical traffic data is used when calculating reachable areas. This affects both the size and shape of isolines by accounting for expected travel speeds based on congestion patterns.

## Contents
<a name="API_IsolineTrafficOptions_Contents"></a>

 ** FlowEventThresholdOverride **   <a name="location-Type-IsolineTrafficOptions-FlowEventThresholdOverride"></a>
The duration in seconds that real-time congestion data is considered valid before reverting to historical traffic patterns. This helps balance between using current conditions and more predictable historical data when calculating travel times.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Usage **   <a name="location-Type-IsolineTrafficOptions-Usage"></a>
Controls whether traffic data is used in calculations. `UseTrafficData` considers both real-time congestion and historical patterns, while `IgnoreTrafficData` calculates routes based solely on road types and speed limits. Using traffic data provides more accurate real-world estimates but may produce different results at different times of day.
Default value: `UseTrafficData`
Type: String
Valid Values: `IgnoreTrafficData | UseTrafficData`
Required: No

## See Also
<a name="API_IsolineTrafficOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineTrafficOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineTrafficOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineTrafficOptions)
