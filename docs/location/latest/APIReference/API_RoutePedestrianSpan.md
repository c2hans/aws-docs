---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianSpan.html
---

# RoutePedestrianSpan
<a name="API_RoutePedestrianSpan"></a>

Span computed for the requested SpanAdditionalFeatures.

## Contents
<a name="API_RoutePedestrianSpan_Contents"></a>

 ** BestCaseDuration **   <a name="location-Type-RoutePedestrianSpan-BestCaseDuration"></a>
Duration of the computed span without traffic congestion.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Country **   <a name="location-Type-RoutePedestrianSpan-Country"></a>
3 letter Country code corresponding to the Span.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Distance **   <a name="location-Type-RoutePedestrianSpan-Distance"></a>
Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Duration **   <a name="location-Type-RoutePedestrianSpan-Duration"></a>
Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** DynamicSpeed **   <a name="location-Type-RoutePedestrianSpan-DynamicSpeed"></a>
Dynamic speed details corresponding to the span.
 **Unit**: `kilometers per hour`
Type: [RouteSpanDynamicSpeedDetails](API_RouteSpanDynamicSpeedDetails.md) object
Required: No

 ** FunctionalClassification **   <a name="location-Type-RoutePedestrianSpan-FunctionalClassification"></a>
A numerical value indicating the functional classification of the road segment corresponding to the span.
Classification values are part of the hierarchical network that helps determine a logical and efficient route, and have the following definitions:

1. Roads that allow for high volume, maximum speed traffic movement between and through major metropolitan areas.

1. Roads that are used to channel traffic to functional class 1 roads for travel between and through cities in the shortest amount of time.

1. Roads that intersect functional class 2 roads and provide a high volume of traffic movement at a lower level of mobility than functional class 2 roads.

1. Roads that provide for a high volume of traffic movement at moderate speeds between neighborhoods.

1. Roads with volume and traffic movement below the level of any other functional class.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** GeometryOffset **   <a name="location-Type-RoutePedestrianSpan-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this span.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Incidents **   <a name="location-Type-RoutePedestrianSpan-Incidents"></a>
Incidents corresponding to the span. These index into the Incidents in the parent Leg.
Type: Array of integers
Required: No

 ** Names **   <a name="location-Type-RoutePedestrianSpan-Names"></a>
Provides an array of names of the pedestrian span in available languages.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: No

 ** PedestrianAccess **   <a name="location-Type-RoutePedestrianSpan-PedestrianAccess"></a>
Access attributes for a pedestrian corresponding to the span.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Valid Values: `Allowed | Indoors | NoThroughTraffic | Park | Stairs | TollRoad`
Required: No

 ** Region **   <a name="location-Type-RoutePedestrianSpan-Region"></a>
2-3 letter Region code corresponding to the Span. This is either a province or a state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3.
Required: No

 ** RoadAttributes **   <a name="location-Type-RoutePedestrianSpan-RoadAttributes"></a>
Attributes for the road segment corresponding to the span.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Valid Values: `Bridge | BuiltUpArea | ControlledAccessHighway | DirtRoad | DividedRoad | Motorway | PrivateRoad | Ramp | RightHandTraffic | Roundabout | Tunnel | UnderConstruction`
Required: No

 ** RouteNumbers **   <a name="location-Type-RoutePedestrianSpan-RouteNumbers"></a>
Designated route name or number corresponding to the span.
Type: Array of [RouteNumber](API_RouteNumber.md) objects
Required: No

 ** SpeedLimit **   <a name="location-Type-RoutePedestrianSpan-SpeedLimit"></a>
Speed limit details corresponding to the span.
 **Unit**: `kilometers per hour`
Type: [RouteSpanSpeedLimitDetails](API_RouteSpanSpeedLimitDetails.md) object
Required: No

 ** TypicalDuration **   <a name="location-Type-RoutePedestrianSpan-TypicalDuration"></a>
Duration of the computed span under typical traffic congestion.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_RoutePedestrianSpan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePedestrianSpan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePedestrianSpan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePedestrianSpan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
