---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleTravelOnlySummary.html
---

# RouteVehicleTravelOnlySummary
<a name="API_RouteVehicleTravelOnlySummary"></a>

Summarized details of the route.

## Contents
<a name="API_RouteVehicleTravelOnlySummary_Contents"></a>

 ** Duration **   <a name="location-Type-RouteVehicleTravelOnlySummary-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** BestCaseDuration **   <a name="location-Type-RouteVehicleTravelOnlySummary-BestCaseDuration"></a>
Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TypicalDuration **   <a name="location-Type-RouteVehicleTravelOnlySummary-TypicalDuration"></a>
Duration of the leg under typical traffic congestion.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_RouteVehicleTravelOnlySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleTravelOnlySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleTravelOnlySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleTravelOnlySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
