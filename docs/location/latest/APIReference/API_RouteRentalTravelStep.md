---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRentalTravelStep.html
---

# RouteRentalTravelStep
<a name="API_RouteRentalTravelStep"></a>

A step that must be performed during the travel portion of the leg.

## Contents
<a name="API_RouteRentalTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteRentalTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteRentalTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Arrive | Continue | Depart | Exit | Keep | Ramp | RoundaboutEnter | RoundaboutExit | RoundaboutPass | Turn | UTurn`
Required: Yes

 ** ContinueStepDetails **   <a name="location-Type-RouteRentalTravelStep-ContinueStepDetails"></a>
Details related to the continue step.
Type: [RouteContinueStepDetails](API_RouteContinueStepDetails.md) object
Required: No

 ** Distance **   <a name="location-Type-RouteRentalTravelStep-Distance"></a>
Distance of the step.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** ExitStepDetails **   <a name="location-Type-RouteRentalTravelStep-ExitStepDetails"></a>
Details related to the exit step.
Type: [RouteExitStepDetails](API_RouteExitStepDetails.md) object
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteRentalTravelStep-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Instruction **   <a name="location-Type-RouteRentalTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Type: String
Required: No

 ** KeepStepDetails **   <a name="location-Type-RouteRentalTravelStep-KeepStepDetails"></a>
Details that are specific to a Keep step.
Type: [RouteKeepStepDetails](API_RouteKeepStepDetails.md) object
Required: No

 ** RampStepDetails **   <a name="location-Type-RouteRentalTravelStep-RampStepDetails"></a>
Details that are specific to a ramp step.
Type: [RouteRampStepDetails](API_RouteRampStepDetails.md) object
Required: No

 ** RoundaboutEnterStepDetails **   <a name="location-Type-RouteRentalTravelStep-RoundaboutEnterStepDetails"></a>
Details about the roundabout leg.
Type: [RouteRoundaboutEnterStepDetails](API_RouteRoundaboutEnterStepDetails.md) object
Required: No

 ** RoundaboutExitStepDetails **   <a name="location-Type-RouteRentalTravelStep-RoundaboutExitStepDetails"></a>
Details about the roundabout step.
Type: [RouteRoundaboutExitStepDetails](API_RouteRoundaboutExitStepDetails.md) object
Required: No

 ** RoundaboutPassStepDetails **   <a name="location-Type-RouteRentalTravelStep-RoundaboutPassStepDetails"></a>
Details about the step.
Type: [RouteRoundaboutPassStepDetails](API_RouteRoundaboutPassStepDetails.md) object
Required: No

 ** TurnStepDetails **   <a name="location-Type-RouteRentalTravelStep-TurnStepDetails"></a>
Details related to the turn step.
Type: [RouteTurnStepDetails](API_RouteTurnStepDetails.md) object
Required: No

 ** UTurnStepDetails **   <a name="location-Type-RouteRentalTravelStep-UTurnStepDetails"></a>
Details related to the U-turn step.
Type: [RouteUTurnStepDetails](API_RouteUTurnStepDetails.md) object
Required: No

## See Also
<a name="API_RouteRentalTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRentalTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRentalTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRentalTravelStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
