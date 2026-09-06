---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteExitStepDetails.html
---

# RouteExitStepDetails
<a name="API_RouteExitStepDetails"></a>

Details related to the exit step.

## Contents
<a name="API_RouteExitStepDetails_Contents"></a>

 ** Intersection **   <a name="location-Type-RouteExitStepDetails-Intersection"></a>
Name of the intersection, if applicable to the step.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: Yes

 ** RelativeExit **   <a name="location-Type-RouteExitStepDetails-RelativeExit"></a>
Exit to be taken.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 12.
Required: No

 ** SteeringDirection **   <a name="location-Type-RouteExitStepDetails-SteeringDirection"></a>
Steering direction for the step.
Type: String
Valid Values: `Left | Right | Straight`
Required: No

 ** TurnAngle **   <a name="location-Type-RouteExitStepDetails-TurnAngle"></a>
Angle of the turn.
Type: Double
Valid Range: Minimum value of -180. Maximum value of 180.
Required: No

 ** TurnIntensity **   <a name="location-Type-RouteExitStepDetails-TurnIntensity"></a>
Intensity of the turn.
Type: String
Valid Values: `Sharp | Slight | Typical`
Required: No

## See Also
<a name="API_RouteExitStepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteExitStepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteExitStepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteExitStepDetails)
