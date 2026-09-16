---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.html
---

# BatchDeleteDevicePositionHistory
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory"></a>

Deletes the position history of one or more devices from a tracker resource.

## Request Syntax
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/delete-positions HTTP/1.1
Content-type: application/json

{
   "DeviceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_WaypointTracking_BatchDeleteDevicePositionHistory_RequestSyntax) **   <a name="location-WaypointTracking_BatchDeleteDevicePositionHistory-request-uri-TrackerName"></a>
The name of the tracker resource to delete the device position history from.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceIds](#API_WaypointTracking_BatchDeleteDevicePositionHistory_RequestSyntax) **   <a name="location-WaypointTracking_BatchDeleteDevicePositionHistory-request-DeviceIds"></a>
Devices whose position history you want to delete.
+ For example, for two devices: `“DeviceIds” : [DeviceId1,DeviceId2]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## Response Syntax
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_ResponseSyntax"></a>

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
         }
      }
   ]
}
```

## Response Elements
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_WaypointTracking_BatchDeleteDevicePositionHistory_ResponseSyntax) **   <a name="location-WaypointTracking_BatchDeleteDevicePositionHistory-response-Errors"></a>
Contains error details for each device history that failed to delete.
Type: Array of [BatchDeleteDevicePositionHistoryError](API_WaypointTracking_BatchDeleteDevicePositionHistoryError.md) objects

## Errors
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_WaypointTracking_BatchDeleteDevicePositionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/BatchDeleteDevicePositionHistory)
