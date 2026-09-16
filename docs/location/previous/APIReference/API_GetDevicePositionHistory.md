---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetDevicePositionHistory.html
---

# GetDevicePositionHistory
<a name="API_GetDevicePositionHistory"></a>

Retrieves the device position history from a tracker resource within a specified range of time.

**Note**
Device positions are deleted after 30 days.

## Request Syntax
<a name="API_GetDevicePositionHistory_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/devices/{{DeviceId}}/list-positions HTTP/1.1
Content-type: application/json

{
   "EndTimeExclusive": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTimeInclusive": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDevicePositionHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-uri-DeviceId"></a>
The device whose position history you want to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** [TrackerName](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-uri-TrackerName"></a>
The tracker resource receiving the request for the device position history.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_GetDevicePositionHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTimeExclusive](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-EndTimeExclusive"></a>
Specify the end time for the position history in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`. By default, the value will be the time that the request is made.
Requirement:
+ The time specified for `EndTimeExclusive` must be after the time for `StartTimeInclusive`.
Type: Timestamp
Required: No

 ** [MaxResults](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-MaxResults"></a>
An optional limit for the number of device positions returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [StartTimeInclusive](#API_GetDevicePositionHistory_RequestSyntax) **   <a name="location-GetDevicePositionHistory-request-StartTimeInclusive"></a>
Specify the start time for the position history in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`. By default, the value will be 24 hours prior to the time that the request is made.
Requirement:
+ The time specified for `StartTimeInclusive` must be before `EndTimeExclusive`.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetDevicePositionHistory_ResponseSyntax"></a>

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
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDevicePositionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DevicePositions](#API_GetDevicePositionHistory_ResponseSyntax) **   <a name="location-GetDevicePositionHistory-response-DevicePositions"></a>
Contains the position history details for the requested device.
Type: Array of [DevicePosition](API_DevicePosition.md) objects

 ** [NextToken](#API_GetDevicePositionHistory_ResponseSyntax) **   <a name="location-GetDevicePositionHistory-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_GetDevicePositionHistory_Errors"></a>

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
<a name="API_GetDevicePositionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetDevicePositionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetDevicePositionHistory)
