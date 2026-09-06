---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationDriverOptions.html
---

# WaypointOptimizationDriverOptions
<a name="API_WaypointOptimizationDriverOptions"></a>

Driver related options.

## Contents
<a name="API_WaypointOptimizationDriverOptions_Contents"></a>

 ** RestCycles **   <a name="location-Type-WaypointOptimizationDriverOptions-RestCycles"></a>
Driver work-rest schedules defined by a short and long cycle. A rest needs to be taken after the short work duration. The short cycle can be repeated until you hit the long work duration, at which point the long rest duration should be taken before restarting.
Type: [WaypointOptimizationRestCycles](API_WaypointOptimizationRestCycles.md) object
Required: No

 ** RestProfile **   <a name="location-Type-WaypointOptimizationDriverOptions-RestProfile"></a>
Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.
Type: [WaypointOptimizationRestProfile](API_WaypointOptimizationRestProfile.md) object
Required: No

 ** TreatServiceTimeAs **   <a name="location-Type-WaypointOptimizationDriverOptions-TreatServiceTimeAs"></a>
If the service time provided at a waypoint/destination should be considered as rest or work. This contributes to the total time breakdown returned within the response.
Type: String
Valid Values: `Rest | Work`
Required: No

## See Also
<a name="API_WaypointOptimizationDriverOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationDriverOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationDriverOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationDriverOptions)
