---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianTravelStep.html
---

# RoutePedestrianTravelStep
<a name="API_RoutePedestrianTravelStep"></a>

Steps of a leg that must be performed during the travel portion of the leg.

## Contents
<a name="API_RoutePedestrianTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RoutePedestrianTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RoutePedestrianTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Arrive | Continue | Depart | Keep | RoundaboutEnter | RoundaboutExit | RoundaboutPass | Turn`
Required: Yes

 ** ContinueStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-ContinueStepDetails"></a>
Details related to the continue step.
Type: [RouteContinueStepDetails](API_RouteContinueStepDetails.md) object
Required: No

 ** CurrentRoad **   <a name="location-Type-RoutePedestrianTravelStep-CurrentRoad"></a>
Details of the current road. See RouteRoad for details of sub-attributes.
Type: [RouteRoad](API_RouteRoad.md) object
Required: No

 ** Distance **   <a name="location-Type-RoutePedestrianTravelStep-Distance"></a>
Distance of the step.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** ExitNumber **   <a name="location-Type-RoutePedestrianTravelStep-ExitNumber"></a>
Exit number of the road exit, if applicable.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: No

 ** GeometryOffset **   <a name="location-Type-RoutePedestrianTravelStep-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Instruction **   <a name="location-Type-RoutePedestrianTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Only available when the TravelStepType is Default.
Type: String
Required: No

 ** KeepStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-KeepStepDetails"></a>
Details that are specific to a Keep step.
Type: [RouteKeepStepDetails](API_RouteKeepStepDetails.md) object
Required: No

 ** NextRoad **   <a name="location-Type-RoutePedestrianTravelStep-NextRoad"></a>
Details of the next road. See RouteRoad for details of sub-attributes.
Type: [RouteRoad](API_RouteRoad.md) object
Required: No

 ** RoundaboutEnterStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-RoundaboutEnterStepDetails"></a>
Details that are specific to a Roundabout Enter step.
Type: [RouteRoundaboutEnterStepDetails](API_RouteRoundaboutEnterStepDetails.md) object
Required: No

 ** RoundaboutExitStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-RoundaboutExitStepDetails"></a>
Details that are specific to a Roundabout Exit step.
Type: [RouteRoundaboutExitStepDetails](API_RouteRoundaboutExitStepDetails.md) object
Required: No

 ** RoundaboutPassStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-RoundaboutPassStepDetails"></a>
Details that are specific to a Roundabout Pass step.
Type: [RouteRoundaboutPassStepDetails](API_RouteRoundaboutPassStepDetails.md) object
Required: No

 ** Signpost **   <a name="location-Type-RoutePedestrianTravelStep-Signpost"></a>
Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.
Type: [RouteSignpost](API_RouteSignpost.md) object
Required: No

 ** TurnStepDetails **   <a name="location-Type-RoutePedestrianTravelStep-TurnStepDetails"></a>
Details that are specific to a turn step.
Type: [RouteTurnStepDetails](API_RouteTurnStepDetails.md) object
Required: No

## See Also
<a name="API_RoutePedestrianTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePedestrianTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePedestrianTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePedestrianTravelStep)
