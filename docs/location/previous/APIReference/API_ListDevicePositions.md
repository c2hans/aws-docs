---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListDevicePositions.html
---

# ListDevicePositions
<a name="API_ListDevicePositions"></a>

A batch request to retrieve all device positions.

## Request Syntax
<a name="API_ListDevicePositions_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/list-positions HTTP/1.1
Content-type: application/json

{
   "FilterGeometry": {
      "Polygon": [
         [
            [ {{number}} ]
         ]
      ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDevicePositions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_ListDevicePositions_RequestSyntax) **   <a name="location-ListDevicePositions-request-uri-TrackerName"></a>
The tracker resource containing the requested devices.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_ListDevicePositions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FilterGeometry](#API_ListDevicePositions_RequestSyntax) **   <a name="location-ListDevicePositions-request-FilterGeometry"></a>
The geometry used to filter device positions.
Type: [TrackingFilterGeometry](API_TrackingFilterGeometry.md) object
Required: No

 ** [MaxResults](#API_ListDevicePositions_RequestSyntax) **   <a name="location-ListDevicePositions-request-MaxResults"></a>
An optional limit for the number of entries returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListDevicePositions_RequestSyntax) **   <a name="location-ListDevicePositions-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListDevicePositions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
      {
         "Accuracy": {
            "Horizontal": number
         },
         "DeviceId": "string",
         "Position": [ number ],
         "PositionProperties": {
            "string" : "string"
         },
         "SampleTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDevicePositions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_ListDevicePositions_ResponseSyntax) **   <a name="location-ListDevicePositions-response-Entries"></a>
Contains details about each device's last known position.
Type: Array of [ListDevicePositionsResponseEntry](API_ListDevicePositionsResponseEntry.md) objects

 ** [NextToken](#API_ListDevicePositions_ResponseSyntax) **   <a name="location-ListDevicePositions-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListDevicePositions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

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
<a name="API_ListDevicePositions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/ListDevicePositions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListDevicePositions)
