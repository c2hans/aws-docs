---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ListStreams.html
---

# ListStreams
<a name="API_ListStreams"></a>

Returns an array of `StreamInfo` objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a `StreamNameCondition`.

## Request Syntax
<a name="API_ListStreams_RequestSyntax"></a>

```
POST /listStreams HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StreamNameCondition": {
      "ComparisonOperator": "{{string}}",
      "ComparisonValue": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListStreams_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStreams_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListStreams_RequestSyntax) **   <a name="KinesisVideo-ListStreams-request-MaxResults"></a>
The maximum number of streams to return in the response. The default is 10,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListStreams_RequestSyntax) **   <a name="KinesisVideo-ListStreams-request-NextToken"></a>
If you specify this parameter, when the result of a `ListStreams` operation is truncated, the call returns the `NextToken` in the response. To get another batch of streams, provide this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`
Required: No

 ** [StreamNameCondition](#API_ListStreams_RequestSyntax) **   <a name="KinesisVideo-ListStreams-request-StreamNameCondition"></a>
Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition.
Type: [StreamNameCondition](API_StreamNameCondition.md) object
Required: No

## Response Syntax
<a name="API_ListStreams_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StreamInfoList": [
      {
         "CreationTime": number,
         "DataRetentionInHours": number,
         "DeviceName": "string",
         "KmsKeyId": "string",
         "MediaType": "string",
         "Status": "string",
         "StreamARN": "string",
         "StreamName": "string",
         "Version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListStreams_ResponseSyntax) **   <a name="KinesisVideo-ListStreams-response-NextToken"></a>
If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [StreamInfoList](#API_ListStreams_ResponseSyntax) **   <a name="KinesisVideo-ListStreams-response-StreamInfoList"></a>
An array of `StreamInfo` objects.
Type: Array of [StreamInfo](API_StreamInfo.md) objects

## Errors
<a name="API_ListStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientLimitExceededException **
Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.
HTTP Status Code: 400

 ** InvalidArgumentException **
The value for this input parameter is invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/ListStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListStreams)
