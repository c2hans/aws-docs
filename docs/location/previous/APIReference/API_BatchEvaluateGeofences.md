---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchEvaluateGeofences.html
---

# BatchEvaluateGeofences
<a name="API_BatchEvaluateGeofences"></a>

Evaluates device positions against the geofence geometries from a given geofence collection.

This operation always returns an empty response because geofences are asynchronously evaluated. The evaluation determines if the device has entered or exited a geofenced area, and then publishes one of the following events to Amazon EventBridge:
+  `ENTER` if Amazon Location determines that the tracked device has entered a geofenced area.
+  `EXIT` if Amazon Location determines that the tracked device has exited a geofenced area.

**Note**
The last geofence that a device was observed within is tracked for 30 days after the most recent device position update.

**Note**
Geofence evaluation uses the given device position. It does not account for the optional `Accuracy` of a `DevicePositionUpdate`.

**Note**
The `DeviceID` is used as a string to represent the device. You do not need to have a `Tracker` associated with the `DeviceID`.

## Request Syntax
<a name="API_BatchEvaluateGeofences_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/positions HTTP/1.1
Content-type: application/json

{
   "DevicePositionUpdates": [
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
<a name="API_BatchEvaluateGeofences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_BatchEvaluateGeofences_RequestSyntax) **   <a name="location-BatchEvaluateGeofences-request-uri-CollectionName"></a>
The geofence collection used in evaluating the position of devices against its geofences.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_BatchEvaluateGeofences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DevicePositionUpdates](#API_BatchEvaluateGeofences_RequestSyntax) **   <a name="location-BatchEvaluateGeofences-request-DevicePositionUpdates"></a>
Contains device details for each device to be evaluated against the given geofence collection.
Type: Array of [DevicePositionUpdate](API_DevicePositionUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchEvaluateGeofences_ResponseSyntax"></a>

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
<a name="API_BatchEvaluateGeofences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchEvaluateGeofences_ResponseSyntax) **   <a name="location-BatchEvaluateGeofences-response-Errors"></a>
Contains error details for each device that failed to evaluate its position against the given geofence collection.
Type: Array of [BatchEvaluateGeofencesError](API_BatchEvaluateGeofencesError.md) objects

## Errors
<a name="API_BatchEvaluateGeofences_Errors"></a>

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
<a name="API_BatchEvaluateGeofences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/BatchEvaluateGeofences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchEvaluateGeofences)
