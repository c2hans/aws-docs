---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryTravelStep.html
---

# RouteFerryTravelStep
<a name="API_RouteFerryTravelStep"></a>

Steps of a leg that must be performed during the travel portion of the leg.

## Contents
<a name="API_RouteFerryTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteFerryTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteFerryTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Depart | Continue | Arrive`
Required: Yes

 ** Distance **   <a name="location-Type-RouteFerryTravelStep-Distance"></a>
Distance of the step.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteFerryTravelStep-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Instruction **   <a name="location-Type-RouteFerryTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Only available when the TravelStepType is Default.
Type: String
Required: No

## See Also
<a name="API_RouteFerryTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteFerryTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteFerryTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteFerryTravelStep)
