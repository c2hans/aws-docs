---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTrafficOptions.html
---

# RouteTrafficOptions
<a name="API_RouteTrafficOptions"></a>

Traffic options for the route.

## Contents
<a name="API_RouteTrafficOptions_Contents"></a>

 ** FlowEventThresholdOverride **   <a name="location-Type-RouteTrafficOptions-FlowEventThresholdOverride"></a>
Duration for which flow traffic is considered valid. For this period, the flow traffic is used over historical traffic data. Flow traffic refers to congestion, which changes very quickly. Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Usage **   <a name="location-Type-RouteTrafficOptions-Usage"></a>
Specifies how traffic data should be used when calculating routes.
Default Value: `UseTrafficData`
Traffic data usage depends on the time parameters in your route request:
+ When `Usage` is set to `UseTrafficData`:
  + If `DepartNow` is set to `true`, or if you specify `DepartureTime` or `ArrivalTime`, then all traffic data is considered (including live traffic and closures).
  + If `DepartNow`, `DepartureTime`, and `ArrivalTime` are all unspecified, then only long-term closures are considered, regardless of this setting.
+ When `Usage` is set to `IgnoreTrafficData`, then all traffic data is ignored regardless of the time parameters in your route request.
Type: String
Valid Values: `IgnoreTrafficData | UseTrafficData`
Required: No

## See Also
<a name="API_RouteTrafficOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTrafficOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTrafficOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTrafficOptions)
