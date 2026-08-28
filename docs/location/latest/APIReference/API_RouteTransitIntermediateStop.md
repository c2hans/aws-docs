---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitIntermediateStop.html
---

# RouteTransitIntermediateStop
<a name="API_RouteTransitIntermediateStop"></a>

An intermediate stop between departure and destination of the transit route.

## Contents
<a name="API_RouteTransitIntermediateStop_Contents"></a>

 ** Departure **   <a name="location-Type-RouteTransitIntermediateStop-Departure"></a>
Departure details for the intermediate stop.
Type: [RouteTransitDeparture](API_RouteTransitDeparture.md) object
Required: Yes

 ** Duration **   <a name="location-Type-RouteTransitIntermediateStop-Duration"></a>
Duration of the stop.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Attributes **   <a name="location-Type-RouteTransitIntermediateStop-Attributes"></a>
Attributes of the intermediate stop.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `NoEntry | NoExit`
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteTransitIntermediateStop-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this stop.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Transport **   <a name="location-Type-RouteTransitIntermediateStop-Transport"></a>
Transport mode details at the intermediate stop.
Type: [RouteTransitTransportModeDetails](API_RouteTransitTransportModeDetails.md) object
Required: No

## See Also
<a name="API_RouteTransitIntermediateStop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitIntermediateStop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitIntermediateStop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitIntermediateStop)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
