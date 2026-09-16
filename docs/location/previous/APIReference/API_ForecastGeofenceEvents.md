---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ForecastGeofenceEvents.html
---

# ForecastGeofenceEvents
<a name="API_ForecastGeofenceEvents"></a>

This action forecasts future geofence events that are likely to occur within a specified time horizon if a device continues moving at its current speed. Each forecasted event is associated with a geofence from a provided geofence collection. A forecast event can have one of the following states:

 `ENTER`: The device position is outside the referenced geofence, but the device may cross into the geofence during the forecasting time horizon if it maintains its current speed.

 `EXIT`: The device position is inside the referenced geofence, but the device may leave the geofence during the forecasted time horizon if the device maintains it's current speed.

 `IDLE`:The device is inside the geofence, and it will remain inside the geofence through the end of the time horizon if the device maintains it's current speed.

**Note**
Heading direction is not considered in the current version. The API takes a conservative approach and includes events that can occur for any heading.

## Request Syntax
<a name="API_ForecastGeofenceEvents_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/forecast-geofence-events HTTP/1.1
Content-type: application/json

{
   "DeviceState": {
      "Position": [ {{number}} ],
      "Speed": {{number}}
   },
   "DistanceUnit": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SpeedUnit": "{{string}}",
   "TimeHorizonMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_ForecastGeofenceEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-uri-CollectionName"></a>
The name of the geofence collection.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_ForecastGeofenceEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceState](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-DeviceState"></a>
Represents the device's state, including its current position and speed. When speed is omitted, this API performs a *containment check*. The *containment check* operation returns `IDLE` events for geofences where the device is currently inside of, but no other events.
Type: [ForecastGeofenceEventsDeviceState](API_ForecastGeofenceEventsDeviceState.md) object
Required: Yes

 ** [DistanceUnit](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-DistanceUnit"></a>
The distance unit used for the `NearestDistance` property returned in a forecasted event. The measurement system must match for `DistanceUnit` and `SpeedUnit`; if `Kilometers` is specified for `DistanceUnit`, then `SpeedUnit` must be `KilometersPerHour`.
Default Value: `Kilometers`
Type: String
Valid Values: `Kilometers | Miles`
Required: No

 ** [MaxResults](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-MaxResults"></a>
An optional limit for the number of resources returned in a single call.
Default value: `20`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: No

 ** [SpeedUnit](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-SpeedUnit"></a>
The speed unit for the device captured by the device state. The measurement system must match for `DistanceUnit` and `SpeedUnit`; if `Kilometers` is specified for `DistanceUnit`, then `SpeedUnit` must be `KilometersPerHour`.
Default Value: `KilometersPerHour`.
Type: String
Valid Values: `KilometersPerHour | MilesPerHour`
Required: No

 ** [TimeHorizonMinutes](#API_ForecastGeofenceEvents_RequestSyntax) **   <a name="location-ForecastGeofenceEvents-request-TimeHorizonMinutes"></a>
The forward-looking time window for forecasting, specified in minutes. The API only returns events that are predicted to occur within this time horizon. When no value is specified, this API performs a *containment check*. The *containment check* operation returns `IDLE` events for geofences where the device is currently inside of, but no other events.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_ForecastGeofenceEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DistanceUnit": "string",
   "ForecastedEvents": [
      {
         "EventId": "string",
         "EventType": "string",
         "ForecastedBreachTime": "string",
         "GeofenceId": "string",
         "GeofenceProperties": {
            "string" : "string"
         },
         "IsDeviceInGeofence": boolean,
         "NearestDistance": number
      }
   ],
   "NextToken": "string",
   "SpeedUnit": "string"
}
```

## Response Elements
<a name="API_ForecastGeofenceEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DistanceUnit](#API_ForecastGeofenceEvents_ResponseSyntax) **   <a name="location-ForecastGeofenceEvents-response-DistanceUnit"></a>
The distance unit for the forecasted events.
Type: String
Valid Values: `Kilometers | Miles`

 ** [ForecastedEvents](#API_ForecastGeofenceEvents_ResponseSyntax) **   <a name="location-ForecastGeofenceEvents-response-ForecastedEvents"></a>
The list of forecasted events.
Type: Array of [ForecastedEvent](API_ForecastedEvent.md) objects

 ** [NextToken](#API_ForecastGeofenceEvents_ResponseSyntax) **   <a name="location-ForecastGeofenceEvents-response-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.

 ** [SpeedUnit](#API_ForecastGeofenceEvents_ResponseSyntax) **   <a name="location-ForecastGeofenceEvents-response-SpeedUnit"></a>
The speed unit for the forecasted events.
Type: String
Valid Values: `KilometersPerHour | MilesPerHour`

## Errors
<a name="API_ForecastGeofenceEvents_Errors"></a>

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
<a name="API_ForecastGeofenceEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/ForecastGeofenceEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ForecastGeofenceEvents)
