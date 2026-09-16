---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrix.html
---

# CalculateRouteMatrix
<a name="API_CalculateRouteMatrix"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the [V2 `CalculateRouteMatrix`](/location/latest/APIReference/API_CalculateRouteMatrix.html) unless you require Grab data.
This version of `CalculateRouteMatrix` is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `CalculateRouteMatrix` operation gives better results for matrix routing calculations.
If you are using an AWS SDK or the AWS CLI, note that the Routes API version 2 is found under `geo-routes` or `geo_routes`, not under `location`.
Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Routes V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html) or the [Developer Guide](/location/latest/developerguide/routes.html).

 [ Calculates a route matrix](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html) given the following required parameters: `DeparturePositions` and `DestinationPositions`. `CalculateRouteMatrix` calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, `CalculateRouteMatrix` will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of `DeparturePositions` times the number of `DestinationPositions`.

**Note**
Your account is charged for each route calculated, not the number of requests.

Requires that you first [create a route calculator resource](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html).

By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.

Additional options include:
+  [ Specifying a departure time](https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html) using either `DepartureTime` or `DepartNow`. This calculates routes based on predictive traffic data at the given time.
**Note**
You can't specify both `DepartureTime` and `DepartNow` in a single request. Specifying both parameters returns a validation error.
+  [Specifying a travel mode](https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html) using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in `CarModeOptions` if traveling by `Car`, or `TruckModeOptions` if traveling by `Truck`.

## Request Syntax
<a name="API_CalculateRouteMatrix_RequestSyntax"></a>

```
POST /routes/v0/calculators/{{CalculatorName}}/calculate/route-matrix?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "CarModeOptions": {
      "AvoidFerries": {{boolean}},
      "AvoidTolls": {{boolean}}
   },
   "DepartNow": {{boolean}},
   "DeparturePositions": [
      [ {{number}} ]
   ],
   "DepartureTime": "{{string}}",
   "DestinationPositions": [
      [ {{number}} ]
   ],
   "DistanceUnit": "{{string}}",
   "TravelMode": "{{string}}",
   "TruckModeOptions": {
      "AvoidFerries": {{boolean}},
      "AvoidTolls": {{boolean}},
      "Dimensions": {
         "Height": {{number}},
         "Length": {{number}},
         "Unit": "{{string}}",
         "Width": {{number}}
      },
      "Weight": {
         "Total": {{number}},
         "Unit": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CalculateRouteMatrix_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatorName](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-uri-CalculatorName"></a>
The name of the route calculator resource that you want to use to calculate the route matrix.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Key](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_CalculateRouteMatrix_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CarModeOptions](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-CarModeOptions"></a>
Specifies route preferences when traveling by `Car`, such as avoiding routes that use ferries or tolls.
Requirements: `TravelMode` must be specified as `Car`.
Type: [CalculateRouteCarModeOptions](API_CalculateRouteCarModeOptions.md) object
Required: No

 ** [DepartNow](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DepartNow"></a>
Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can't set both `DepartureTime` and `DepartNow`. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.
Default Value: `false`
Valid Values: `false` \| `true`
Type: Boolean
Required: No

 ** [DeparturePositions](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DeparturePositions"></a>
The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in [WGS 84](https://earth-info.nga.mil/GandG/wgs84/index.html) format: `[longitude, latitude]`. For example, `[-123.115, 49.285]`.
Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See [ Position restrictions](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits) in the *Amazon Location Service Developer Guide*.
For route calculators that use Esri as the data provider, if you specify a departure that's not located on a road, Amazon Location [ moves the position to the nearest road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html). The snapped value is available in the result in `SnappedDeparturePositions`.
Valid Values: `[-180 to 180,-90 to 90]`
Type: Array of arrays of doubles
Array Members: Minimum number of 1 item. Maximum number of 350 items.
Array Members: Fixed number of 2 items.
Required: Yes

 ** [DepartureTime](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DepartureTime"></a>
Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can't set both `DepartureTime` and `DepartNow`. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.
Setting a departure time in the past returns a `400 ValidationException` error.
+ In [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`. For example, `2020–07-2T12:15:20.000Z+01:00`
Type: Timestamp
Required: No

 ** [DestinationPositions](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DestinationPositions"></a>
The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in [WGS 84](https://earth-info.nga.mil/GandG/wgs84/index.html) format: `[longitude, latitude]`. For example, `[-122.339, 47.615]`
Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See [ Position restrictions](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits) in the *Amazon Location Service Developer Guide*.
For route calculators that use Esri as the data provider, if you specify a destination that's not located on a road, Amazon Location [ moves the position to the nearest road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html). The snapped value is available in the result in `SnappedDestinationPositions`.
Valid Values: `[-180 to 180,-90 to 90]`
Type: Array of arrays of doubles
Array Members: Minimum number of 1 item. Maximum number of 350 items.
Array Members: Fixed number of 2 items.
Required: Yes

 ** [DistanceUnit](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DistanceUnit"></a>
Set the unit system to specify the distance.
Default Value: `Kilometers`
Type: String
Valid Values: `Kilometers | Miles`
Required: No

 ** [TravelMode](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-TravelMode"></a>
Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.
The `TravelMode` you specify also determines how you specify route preferences:
+ If traveling by `Car` use the `CarModeOptions` parameter.
+ If traveling by `Truck` use the `TruckModeOptions` parameter.
 `Bicycle` or `Motorcycle` are only valid when using `Grab` as a data provider, and only within Southeast Asia.
 `Truck` is not available for Grab.
For more information about using Grab as a data provider, see [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html) in the *Amazon Location Service Developer Guide*.
Default Value: `Car`
Type: String
Valid Values: `Car | Truck | Walking | Bicycle | Motorcycle`
Required: No

 ** [TruckModeOptions](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-TruckModeOptions"></a>
Specifies route preferences when traveling by `Truck`, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.
Requirements: `TravelMode` must be specified as `Truck`.
Type: [CalculateRouteTruckModeOptions](API_CalculateRouteTruckModeOptions.md) object
Required: No

## Response Syntax
<a name="API_CalculateRouteMatrix_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RouteMatrix": [
      [
         {
            "Distance": number,
            "DurationSeconds": number,
            "Error": {
               "Code": "string",
               "Message": "string"
            }
         }
      ]
   ],
   "SnappedDeparturePositions": [
      [ number ]
   ],
   "SnappedDestinationPositions": [
      [ number ]
   ],
   "Summary": {
      "DataSource": "string",
      "DistanceUnit": "string",
      "ErrorCount": number,
      "RouteCount": number
   }
}
```

## Response Elements
<a name="API_CalculateRouteMatrix_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RouteMatrix](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-RouteMatrix"></a>
The calculated route matrix containing the results for all pairs of `DeparturePositions` to `DestinationPositions`. Each row corresponds to one entry in `DeparturePositions`. Each entry in the row corresponds to the route from that entry in `DeparturePositions` to an entry in `DestinationPositions`.
Type: Array of arrays of [RouteMatrixEntry](API_RouteMatrixEntry.md) objects

 ** [SnappedDeparturePositions](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-SnappedDeparturePositions"></a>
For routes calculated using an Esri route calculator resource, departure positions are snapped to the closest road. For Esri route calculator resources, this returns the list of departure/origin positions used for calculation of the `RouteMatrix`.
Type: Array of arrays of doubles
Array Members: Minimum number of 1 item. Maximum number of 350 items.
Array Members: Fixed number of 2 items.

 ** [SnappedDestinationPositions](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-SnappedDestinationPositions"></a>
The list of destination positions for the route matrix used for calculation of the `RouteMatrix`.
Type: Array of arrays of doubles
Array Members: Minimum number of 1 item. Maximum number of 350 items.
Array Members: Fixed number of 2 items.

 ** [Summary](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-Summary"></a>
Contains information about the route matrix, `DataSource`, `DistanceUnit`, `RouteCount` and `ErrorCount`.
Type: [CalculateRouteMatrixSummary](API_CalculateRouteMatrixSummary.md) object

## Errors
<a name="API_CalculateRouteMatrix_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_CalculateRouteMatrix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CalculateRouteMatrix)
