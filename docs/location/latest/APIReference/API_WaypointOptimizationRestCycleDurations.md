---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationRestCycleDurations.html
---

# WaypointOptimizationRestCycleDurations
<a name="API_WaypointOptimizationRestCycleDurations"></a>

Driver work-rest schedules defined by a short and long cycle. A rest needs to be taken after the short work duration. The short cycle can be repeated until you hit the long work duration, at which point the long rest duration should be taken before restarting.

 **Unit**: `seconds`

## Contents
<a name="API_WaypointOptimizationRestCycleDurations_Contents"></a>

 ** RestDuration **   <a name="location-Type-WaypointOptimizationRestCycleDurations-RestDuration"></a>
Resting phase of the cycle.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** WorkDuration **   <a name="location-Type-WaypointOptimizationRestCycleDurations-WorkDuration"></a>
Working phase of the cycle.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_WaypointOptimizationRestCycleDurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationRestCycleDurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationRestCycleDurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationRestCycleDurations)
