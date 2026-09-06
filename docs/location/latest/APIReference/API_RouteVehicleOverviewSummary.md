---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleOverviewSummary.html
---

# RouteVehicleOverviewSummary
<a name="API_RouteVehicleOverviewSummary"></a>

Summary including duration and distance for the entire leg.

## Contents
<a name="API_RouteVehicleOverviewSummary_Contents"></a>

 ** Distance **   <a name="location-Type-RouteVehicleOverviewSummary-Distance"></a>
Distance of the entire leg.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Duration **   <a name="location-Type-RouteVehicleOverviewSummary-Duration"></a>
Duration of the entire leg.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** BestCaseDuration **   <a name="location-Type-RouteVehicleOverviewSummary-BestCaseDuration"></a>
Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TypicalDuration **   <a name="location-Type-RouteVehicleOverviewSummary-TypicalDuration"></a>
Duration of the leg under typical traffic congestion.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_RouteVehicleOverviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleOverviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleOverviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleOverviewSummary)
