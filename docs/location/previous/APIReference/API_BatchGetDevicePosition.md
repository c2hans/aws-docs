---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchGetDevicePosition.html
---

# BatchGetDevicePosition
<a name="API_BatchGetDevicePosition"></a>

Lists the latest device positions for requested devices.

## Request Syntax
<a name="API_BatchGetDevicePosition_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/get-positions HTTP/1.1
Content-type: application/json

{
   "DeviceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetDevicePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_BatchGetDevicePosition_RequestSyntax) **   <a name="location-BatchGetDevicePosition-request-uri-TrackerName"></a>
The tracker resource retrieving the device position.
Length Constraints: Minimum length of 1.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_BatchGetDevicePosition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceIds](#API_BatchGetDevicePosition_RequestSyntax) **   <a name="location-BatchGetDevicePosition-request-DeviceIds"></a>
Devices whose position you want to retrieve.
+ For example, for two devices: `device-ids=DeviceId1&device-ids=DeviceId2`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetDevicePosition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DevicePositions": [
      {
         "Accuracy": {
            "Horizontal": number
         },
         "DeviceId": "string",
         "Position": [ number ],
         "PositionProperties": {
            "string" : "string"
         },
         "ReceivedTime": "string",
         "SampleTime": "string"
      }
   ],
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
<a name="API_BatchGetDevicePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DevicePositions](#API_BatchGetDevicePosition_ResponseSyntax) **   <a name="location-BatchGetDevicePosition-response-DevicePositions"></a>
Contains device position details such as the device ID, position, and timestamps for when the position was received and sampled.
Type: Array of [DevicePosition](API_DevicePosition.md) objects

 ** [Errors](#API_BatchGetDevicePosition_ResponseSyntax) **   <a name="location-BatchGetDevicePosition-response-Errors"></a>
Contains error details for each device that failed to send its position to the tracker resource.
Type: Array of [BatchGetDevicePositionError](API_BatchGetDevicePositionError.md) objects

## Errors
<a name="API_BatchGetDevicePosition_Errors"></a>

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
<a name="API_BatchGetDevicePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/BatchGetDevicePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchGetDevicePosition)
