---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStream.html
---

# GetStream
<a name="API_GetStream"></a>

Gets information about the active (live) stream on a specified channel.

## Request Syntax
<a name="API_GetStream_RequestSyntax"></a>

```
POST /GetStream HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetStream_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_GetStream_RequestSyntax) **   <a name="ivs-GetStream-request-channelArn"></a>
Channel ARN for stream to be accessed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "stream": {
      "channelArn": "string",
      "health": "string",
      "playbackUrl": "string",
      "startTime": "string",
      "state": "string",
      "streamId": "string",
      "viewerCount": number
   }
}
```

## Response Elements
<a name="API_GetStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [stream](#API_GetStream_ResponseSyntax) **   <a name="ivs-GetStream-response-stream"></a>

Type: [Stream](API_Stream.md) object

## Errors
<a name="API_GetStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ChannelNotBroadcasting **
The stream is offline for the given channel ARN.
HTTP Status Code: 404

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/GetStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/GetStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/GetStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/GetStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/GetStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/GetStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/GetStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/GetStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/GetStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/GetStream)
