---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTimeBreakdown.html
---

# WaypointOptimizationTimeBreakdown
<a name="API_WaypointOptimizationTimeBreakdown"></a>

Time breakdown for the sequence.

## Contents
<a name="API_WaypointOptimizationTimeBreakdown_Contents"></a>

 ** RestDuration **   <a name="location-Type-WaypointOptimizationTimeBreakdown-RestDuration"></a>
Resting phase of the cycle.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** ServiceDuration **   <a name="location-Type-WaypointOptimizationTimeBreakdown-ServiceDuration"></a>
Service time spent at the destination. At an appointment, the service time should be the appointment duration.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** TravelDuration **   <a name="location-Type-WaypointOptimizationTimeBreakdown-TravelDuration"></a>
Traveling phase of the cycle.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** WaitDuration **   <a name="location-Type-WaypointOptimizationTimeBreakdown-WaitDuration"></a>
Waiting phase of the cycle.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_WaypointOptimizationTimeBreakdown_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationTimeBreakdown)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationTimeBreakdown)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationTimeBreakdown)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
