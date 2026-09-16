---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchUpdateDevicePosition.html
---

# BatchUpdateDevicePosition
<a name="API_BatchUpdateDevicePosition"></a>

Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch). Amazon Location uses the data when it reports the last known device position and position history. Amazon Location retains location data for 30 days.

**Note**
Position updates are handled based on the `PositionFiltering` property of the tracker. When `PositionFiltering` is set to `TimeBased`, updates are evaluated against linked geofence collections, and location data is stored at a maximum of one position per 30 second interval. If your update frequency is more often than every 30 seconds, only one update per 30 seconds is stored for each unique device ID.
When `PositionFiltering` is set to `DistanceBased` filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than 30 m (98.4 ft).
When `PositionFiltering` is set to `AccuracyBased` filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than the measured accuracy. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is neither stored or evaluated if the device has moved less than 15 m. If `PositionFiltering` is set to `AccuracyBased` filtering, Amazon Location uses the default value `{ "Horizontal": 0}` when accuracy is not provided on a `DevicePositionUpdate`.

## Request Syntax
<a name="API_BatchUpdateDevicePosition_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/positions HTTP/1.1
Content-type: application/json

{
   "Updates": [
      {
         "Accuracy": {
            "Horizontal": {{number}}
         },
         "DeviceId": "{{string}}",
         "Position": [ {{number}} ],
         "PositionProperties": {
            "{{string}}" : "{{string}}"
         },
         "SampleTime": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateDevicePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_BatchUpdateDevicePosition_RequestSyntax) **   <a name="location-BatchUpdateDevicePosition-request-uri-TrackerName"></a>
The name of the tracker resource to update.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_BatchUpdateDevicePosition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Updates](#API_BatchUpdateDevicePosition_RequestSyntax) **   <a name="location-BatchUpdateDevicePosition-request-Updates"></a>
Contains the position update details for each device, up to 10 devices.
Type: Array of [DevicePositionUpdate](API_DevicePositionUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateDevicePosition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "DeviceId": "string",
         "Error": {
            "Code": "string",
            "Message": "string"
         },
         "SampleTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateDevicePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchUpdateDevicePosition_ResponseSyntax) **   <a name="location-BatchUpdateDevicePosition-response-Errors"></a>
Contains error details for each device that failed to update its position.
Type: Array of [BatchUpdateDevicePositionError](API_BatchUpdateDevicePositionError.md) objects

## Errors
<a name="API_BatchUpdateDevicePosition_Errors"></a>

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
<a name="API_BatchUpdateDevicePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/BatchUpdateDevicePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchUpdateDevicePosition)
