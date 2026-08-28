---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleAfterTravelStep.html
---

# RouteVehicleAfterTravelStep
<a name="API_RouteVehicleAfterTravelStep"></a>

Steps of a leg that must be performed after the travel portion of the leg.

## Contents
<a name="API_RouteVehicleAfterTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteVehicleAfterTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteVehicleAfterTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Park`
Required: Yes

 ** ChargeStepDetails **   <a name="location-Type-RouteVehicleAfterTravelStep-ChargeStepDetails"></a>
Details that are specific to a Charge step.
 **Unit**: `KwH `
Type: [RouteChargeStepDetails](API_RouteChargeStepDetails.md) object
Required: No

 ** Instruction **   <a name="location-Type-RouteVehicleAfterTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Only available when the TravelStepType is Default.
Type: String
Required: No

## See Also
<a name="API_RouteVehicleAfterTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleAfterTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleAfterTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleAfterTravelStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
