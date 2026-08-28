---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteContinueHighwayStepDetails.html
---

# RouteContinueHighwayStepDetails
<a name="API_RouteContinueHighwayStepDetails"></a>

Details related to the continue highway step.

## Contents
<a name="API_RouteContinueHighwayStepDetails_Contents"></a>

 ** Intersection **   <a name="location-Type-RouteContinueHighwayStepDetails-Intersection"></a>
Name of the intersection, if applicable to the step.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: Yes

 ** SteeringDirection **   <a name="location-Type-RouteContinueHighwayStepDetails-SteeringDirection"></a>
Steering direction for the step.
Type: String
Valid Values: `Left | Right | Straight`
Required: No

 ** TurnAngle **   <a name="location-Type-RouteContinueHighwayStepDetails-TurnAngle"></a>
Angle of the turn.
Type: Double
Valid Range: Minimum value of -180. Maximum value of 180.
Required: No

 ** TurnIntensity **   <a name="location-Type-RouteContinueHighwayStepDetails-TurnIntensity"></a>
Intensity of the turn.
Type: String
Valid Values: `Sharp | Slight | Typical`
Required: No

## See Also
<a name="API_RouteContinueHighwayStepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteContinueHighwayStepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteContinueHighwayStepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteContinueHighwayStepDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
