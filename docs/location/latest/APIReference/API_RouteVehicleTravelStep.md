---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleTravelStep.html
---

# RouteVehicleTravelStep
<a name="API_RouteVehicleTravelStep"></a>

Steps of a leg that correspond to the travel portion of the leg.

## Contents
<a name="API_RouteVehicleTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteVehicleTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteVehicleTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Arrive | Continue | ContinueHighway | Depart | EnterHighway | Exit | Keep | Ramp | RoundaboutEnter | RoundaboutExit | RoundaboutPass | Turn | UTurn`
Required: Yes

 ** ContinueHighwayStepDetails **   <a name="location-Type-RouteVehicleTravelStep-ContinueHighwayStepDetails"></a>
Details that are specific to a Continue Highway step.
Type: [RouteContinueHighwayStepDetails](API_RouteContinueHighwayStepDetails.md) object
Required: No

 ** ContinueStepDetails **   <a name="location-Type-RouteVehicleTravelStep-ContinueStepDetails"></a>
Details that are specific to a Continue step.
Type: [RouteContinueStepDetails](API_RouteContinueStepDetails.md) object
Required: No

 ** CurrentRoad **   <a name="location-Type-RouteVehicleTravelStep-CurrentRoad"></a>
Details of the current road.
Type: [RouteRoad](API_RouteRoad.md) object
Required: No

 ** Distance **   <a name="location-Type-RouteVehicleTravelStep-Distance"></a>
Distance of the step.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** EnterHighwayStepDetails **   <a name="location-Type-RouteVehicleTravelStep-EnterHighwayStepDetails"></a>
Details that are specific to a Enter Highway step.
Type: [RouteEnterHighwayStepDetails](API_RouteEnterHighwayStepDetails.md) object
Required: No

 ** ExitNumber **   <a name="location-Type-RouteVehicleTravelStep-ExitNumber"></a>
Exit number of the road exit, if applicable.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: No

 ** ExitStepDetails **   <a name="location-Type-RouteVehicleTravelStep-ExitStepDetails"></a>
Details that are specific to a Roundabout Exit step.
Type: [RouteExitStepDetails](API_RouteExitStepDetails.md) object
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteVehicleTravelStep-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Instruction **   <a name="location-Type-RouteVehicleTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Only available when the TravelStepType is Default.
Type: String
Required: No

 ** KeepStepDetails **   <a name="location-Type-RouteVehicleTravelStep-KeepStepDetails"></a>
Details that are specific to a Keep step.
Type: [RouteKeepStepDetails](API_RouteKeepStepDetails.md) object
Required: No

 ** NextRoad **   <a name="location-Type-RouteVehicleTravelStep-NextRoad"></a>
Details of the next road. See RouteRoad for details of sub-attributes.
Type: [RouteRoad](API_RouteRoad.md) object
Required: No

 ** RampStepDetails **   <a name="location-Type-RouteVehicleTravelStep-RampStepDetails"></a>
Details that are specific to a Ramp step.
Type: [RouteRampStepDetails](API_RouteRampStepDetails.md) object
Required: No

 ** RoundaboutEnterStepDetails **   <a name="location-Type-RouteVehicleTravelStep-RoundaboutEnterStepDetails"></a>
Details that are specific to a Roundabout Enter step.
Type: [RouteRoundaboutEnterStepDetails](API_RouteRoundaboutEnterStepDetails.md) object
Required: No

 ** RoundaboutExitStepDetails **   <a name="location-Type-RouteVehicleTravelStep-RoundaboutExitStepDetails"></a>
Details that are specific to a Roundabout Exit step.
Type: [RouteRoundaboutExitStepDetails](API_RouteRoundaboutExitStepDetails.md) object
Required: No

 ** RoundaboutPassStepDetails **   <a name="location-Type-RouteVehicleTravelStep-RoundaboutPassStepDetails"></a>
Details that are specific to a Roundabout Pass step.
Type: [RouteRoundaboutPassStepDetails](API_RouteRoundaboutPassStepDetails.md) object
Required: No

 ** Signpost **   <a name="location-Type-RouteVehicleTravelStep-Signpost"></a>
Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.
Type: [RouteSignpost](API_RouteSignpost.md) object
Required: No

 ** TurnStepDetails **   <a name="location-Type-RouteVehicleTravelStep-TurnStepDetails"></a>
Details that are specific to a Turn step.
Type: [RouteTurnStepDetails](API_RouteTurnStepDetails.md) object
Required: No

 ** UTurnStepDetails **   <a name="location-Type-RouteVehicleTravelStep-UTurnStepDetails"></a>
Details that are specific to a Turn step.
Type: [RouteUTurnStepDetails](API_RouteUTurnStepDetails.md) object
Required: No

## See Also
<a name="API_RouteVehicleTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleTravelStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
