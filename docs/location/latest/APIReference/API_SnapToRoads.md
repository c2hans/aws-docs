---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html
---

# SnapToRoads
<a name="API_SnapToRoads"></a>

 `SnapToRoads` matches GPS trace to roads most likely traveled on.

For more information, see [Snap to Roads](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-roads.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_SnapToRoads_RequestSyntax"></a>

```
POST /v2/snap-to-roads?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "SnappedGeometryFormat": "{{string}}",
   "SnapRadius": {{number}},
   "TracePoints": [
      {
         "Heading": {{number}},
         "Position": [ {{number}} ],
         "Speed": {{number}},
         "Timestamp": "{{string}}"
      }
   ],
   "TravelMode": "{{string}}",
   "TravelModeOptions": {
      "Truck": {
         "GrossWeight": {{number}},
         "HazardousCargos": [ "{{string}}" ],
         "Height": {{number}},
         "Length": {{number}},
         "Trailer": {
            "TrailerCount": {{number}}
         },
         "TunnelRestrictionCode": "{{string}}",
         "Width": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_SnapToRoads_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_SnapToRoads_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SnappedGeometryFormat](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-SnappedGeometryFormat"></a>
Chooses what the returned SnappedGeometry format should be.
Default value: `FlexiblePolyline`
Type: String
Valid Values: `FlexiblePolyline | Simple`
Required: No

 ** [SnapRadius](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-SnapRadius"></a>
The radius around the provided tracepoint that is considered for snapping.
 **Unit**: `meters`
Default value: `300`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** [TracePoints](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-TracePoints"></a>
List of trace points to be snapped onto the road network.
Type: Array of [RoadSnapTracePoint](API_RoadSnapTracePoint.md) objects
Array Members: Minimum number of 2 items. Maximum number of 5000 items.
Required: Yes

 ** [TravelMode](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-TravelMode"></a>
Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.
Default value: `Car`
Type: String
Valid Values: `Car | Pedestrian | Scooter | Truck`
Required: No

 ** [TravelModeOptions](#API_SnapToRoads_RequestSyntax) **   <a name="location-SnapToRoads-request-TravelModeOptions"></a>
Travel mode related options for the provided travel mode.
Type: [RoadSnapTravelModeOptions](API_RoadSnapTravelModeOptions.md) object
Required: No

## Response Syntax
<a name="API_SnapToRoads_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "Notices": [
      {
         "Code": "string",
         "Title": "string",
         "TracePointIndexes": [ number ]
      }
   ],
   "SnappedGeometry": {
      "LineString": [
         [ number ]
      ],
      "Polyline": "string"
   },
   "SnappedGeometryFormat": "string",
   "SnappedTracePoints": [
      {
         "Confidence": number,
         "OriginalPosition": [ number ],
         "SnappedPosition": [ number ]
      }
   ]
}
```

## Response Elements
<a name="API_SnapToRoads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_SnapToRoads_ResponseSyntax) **   <a name="location-SnapToRoads-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.

The following data is returned in JSON format by the service.

 ** [Notices](#API_SnapToRoads_ResponseSyntax) **   <a name="location-SnapToRoads-response-Notices"></a>
Notices are additional information returned that indicate issues that occurred during route calculation.
Type: Array of [RoadSnapNotice](API_RoadSnapNotice.md) objects

 ** [SnappedGeometry](#API_SnapToRoads_ResponseSyntax) **   <a name="location-SnapToRoads-response-SnappedGeometry"></a>
The interpolated geometry for the snapped route onto the road network.
Type: [RoadSnapSnappedGeometry](API_RoadSnapSnappedGeometry.md) object

 ** [SnappedGeometryFormat](#API_SnapToRoads_ResponseSyntax) **   <a name="location-SnapToRoads-response-SnappedGeometryFormat"></a>
Specifies the format of the geometry returned for each leg of the route.
Type: String
Valid Values: `FlexiblePolyline | Simple`

 ** [SnappedTracePoints](#API_SnapToRoads_ResponseSyntax) **   <a name="location-SnapToRoads-response-SnappedTracePoints"></a>
The trace points snapped onto the road network.
Type: Array of [RoadSnapSnappedTracePoint](API_RoadSnapSnappedTracePoint.md) objects

## Errors
<a name="API_SnapToRoads_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_SnapToRoads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-routes-2020-11-19/SnapToRoads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/SnapToRoads)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
