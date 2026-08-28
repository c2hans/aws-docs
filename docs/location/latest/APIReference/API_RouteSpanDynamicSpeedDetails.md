---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSpanDynamicSpeedDetails.html
---

# RouteSpanDynamicSpeedDetails
<a name="API_RouteSpanDynamicSpeedDetails"></a>

Details about the dynamic speed.

 **Unit**: `kilometers per hour`

## Contents
<a name="API_RouteSpanDynamicSpeedDetails_Contents"></a>

 ** BestCaseSpeed **   <a name="location-Type-RouteSpanDynamicSpeedDetails-BestCaseSpeed"></a>
Estimated speed while traversing the span without traffic congestion.
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** TurnDuration **   <a name="location-Type-RouteSpanDynamicSpeedDetails-TurnDuration"></a>
Estimated time to turn from this span into the next.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TypicalSpeed **   <a name="location-Type-RouteSpanDynamicSpeedDetails-TypicalSpeed"></a>
Estimated speed while traversing the span under typical traffic congestion.
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

## See Also
<a name="API_RouteSpanDynamicSpeedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteSpanDynamicSpeedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteSpanDynamicSpeedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteSpanDynamicSpeedDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
