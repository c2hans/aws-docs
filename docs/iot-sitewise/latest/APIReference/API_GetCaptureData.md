---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetCaptureData.html
---

# GetCaptureData
<a name="API_GetCaptureData"></a>

Retrieves video data for a specific time range.

## Request Syntax
<a name="API_GetCaptureData_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/get-capture-data HTTP/1.1
Content-type: application/json

{
   "endTime": {
      "offsetInNanos": {{number}},
      "timeInSeconds": {{number}}
   },
   "formatSettings": {
      "framesPerSecond": {{number}},
      "heightInPixels": {{number}},
      "widthInPixels": {{number}}
   },
   "nextToken": "{{string}}",
   "propertyAlias": "{{string}}",
   "startTime": {
      "offsetInNanos": {{number}},
      "timeInSeconds": {{number}}
   },
   "timeSeriesId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCaptureData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-uri-workspaceName"></a>
The name of the workspace that contains the capture source.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_GetCaptureData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endTime](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-endTime"></a>
The end time for the video data range. Must be greater than startTime.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** [formatSettings](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-formatSettings"></a>
The optional format settings for the output.
Type: [FormatSettings](API_FormatSettings.md) object
Required: No

 ** [nextToken](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-nextToken"></a>
The token from a previous response used to continue retrieving data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [propertyAlias](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-propertyAlias"></a>
The property alias that identifies the capture source. Mutually exclusive with timeSeriesId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [startTime](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-startTime"></a>
The start time for the video data range.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** [timeSeriesId](#API_GetCaptureData_RequestSyntax) **   <a name="iotsitewise-GetCaptureData-request-timeSeriesId"></a>
The time series ID that identifies the capture source. Mutually exclusive with propertyAlias.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: No

## Response Syntax
<a name="API_GetCaptureData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "data": blob,
   "dataType": "string",
   "endTime": {
      "offsetInNanos": number,
      "timeInSeconds": number
   },
   "nextToken": "string",
   "startTime": {
      "offsetInNanos": number,
      "timeInSeconds": number
   }
}
```

## Response Elements
<a name="API_GetCaptureData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [data](#API_GetCaptureData_ResponseSyntax) **   <a name="iotsitewise-GetCaptureData-response-data"></a>
The binary video data.
Type: Base64-encoded binary data object

 ** [dataType](#API_GetCaptureData_ResponseSyntax) **   <a name="iotsitewise-GetCaptureData-response-dataType"></a>
The type of the returned data.
Type: String
Valid Values: `VIDEO-MP4`

 ** [endTime](#API_GetCaptureData_ResponseSyntax) **   <a name="iotsitewise-GetCaptureData-response-endTime"></a>
The actual end time of the returned data.
Type: [TimeInNanos](API_TimeInNanos.md) object

 ** [nextToken](#API_GetCaptureData_ResponseSyntax) **   <a name="iotsitewise-GetCaptureData-response-nextToken"></a>
The token used to retrieve the next chunk. Absent if no more data is available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [startTime](#API_GetCaptureData_ResponseSyntax) **   <a name="iotsitewise-GetCaptureData-response-startTime"></a>
The actual start time of the returned data.
Type: [TimeInNanos](API_TimeInNanos.md) object

## Errors
<a name="API_GetCaptureData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_GetCaptureData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/GetCaptureData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GetCaptureData)
