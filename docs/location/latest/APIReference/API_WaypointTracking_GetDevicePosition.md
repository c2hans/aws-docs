---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html
---

# GetDevicePosition
<a name="API_WaypointTracking_GetDevicePosition"></a>

Retrieves a device's most recent position according to its sample time.

**Note**
Device positions are deleted after 30 days.

## Request Syntax
<a name="API_WaypointTracking_GetDevicePosition_RequestSyntax"></a>

```
GET /tracking/v0/trackers/{{TrackerName}}/devices/{{DeviceId}}/positions/latest HTTP/1.1
```

## URI Request Parameters
<a name="API_WaypointTracking_GetDevicePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_WaypointTracking_GetDevicePosition_RequestSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-request-uri-DeviceId"></a>
The device whose position you want to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** [TrackerName](#API_WaypointTracking_GetDevicePosition_RequestSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-request-uri-TrackerName"></a>
The tracker resource receiving the position update.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_GetDevicePosition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_WaypointTracking_GetDevicePosition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_WaypointTracking_GetDevicePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accuracy](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-Accuracy"></a>
The accuracy of the device position.
Type: [PositionalAccuracy](API_WaypointTracking_PositionalAccuracy.md) object

 ** [DeviceId](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-DeviceId"></a>
The device whose position you retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`

 ** [Position](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-Position"></a>
The last known device position.
Type: Array of doubles
Array Members: Fixed number of 2 items.

 ** [PositionProperties](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-PositionProperties"></a>
The properties associated with the position.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 150.

 ** [ReceivedTime](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-ReceivedTime"></a>
The timestamp for when the tracker resource received the device position. Uses [ ISO 8601 ](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [SampleTime](#API_WaypointTracking_GetDevicePosition_ResponseSyntax) **   <a name="location-WaypointTracking_GetDevicePosition-response-SampleTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601 ](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

## Errors
<a name="API_WaypointTracking_GetDevicePosition_Errors"></a>

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
<a name="API_WaypointTracking_GetDevicePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/GetDevicePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/GetDevicePosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
