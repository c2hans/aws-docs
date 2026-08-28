---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitTravelStep.html
---

# RouteTransitTravelStep
<a name="API_RouteTransitTravelStep"></a>

A step that must be performed during the travel portion of the leg.

## Contents
<a name="API_RouteTransitTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteTransitTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteTransitTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Depart`
Required: Yes

 ** Distance **   <a name="location-Type-RouteTransitTravelStep-Distance"></a>
Distance of the step.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteTransitTravelStep-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Instruction **   <a name="location-Type-RouteTransitTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Type: String
Required: No

## See Also
<a name="API_RouteTransitTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitTravelStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
