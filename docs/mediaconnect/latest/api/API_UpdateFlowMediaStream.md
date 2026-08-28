---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowMediaStream.html
---

# UpdateFlowMediaStream
<a name="API_UpdateFlowMediaStream"></a>

 Updates an existing media stream.

## Request Syntax
<a name="API_UpdateFlowMediaStream_RequestSyntax"></a>

```
PUT /v1/flows/{{flowArn}}/mediaStreams/{{mediaStreamName}} HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "fmtp": {
         "channelOrder": "{{string}}",
         "colorimetry": "{{string}}",
         "exactFramerate": "{{string}}",
         "par": "{{string}}",
         "range": "{{string}}",
         "scanMode": "{{string}}",
         "tcs": "{{string}}"
      },
      "lang": "{{string}}"
   },
   "clockRate": {{number}},
   "description": "{{string}}",
   "mediaStreamType": "{{string}}",
   "videoFormat": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFlowMediaStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that is associated with the media stream that you updated.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

 ** [mediaStreamName](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-uri-mediaStreamName"></a>
 The media stream that you updated.
Required: Yes

## Request Body
<a name="API_UpdateFlowMediaStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-attributes"></a>
 The attributes that you want to assign to the media stream.
Type: [MediaStreamAttributesRequest](API_MediaStreamAttributesRequest.md) object
Required: No

 ** [clockRate](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-clockRate"></a>
The sample rate for the stream. This value in measured in kHz.
Type: Integer
Required: No

 ** [description](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-description"></a>
A description that can help you quickly identify what your media stream is used for.
Type: String
Required: No

 ** [mediaStreamType](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-mediaStreamType"></a>
The type of media stream.
Type: String
Valid Values: `video | audio | ancillary-data`
Required: No

 ** [videoFormat](#API_UpdateFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-request-videoFormat"></a>
The resolution of the video.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateFlowMediaStream_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "flowArn": "string",
   "mediaStream": {
      "attributes": {
         "fmtp": {
            "channelOrder": "string",
            "colorimetry": "string",
            "exactFramerate": "string",
            "par": "string",
            "range": "string",
            "scanMode": "string",
            "tcs": "string"
         },
         "lang": "string"
      },
      "clockRate": number,
      "description": "string",
      "fmt": number,
      "mediaStreamId": number,
      "mediaStreamName": "string",
      "mediaStreamType": "string",
      "videoFormat": "string"
   }
}
```

## Response Elements
<a name="API_UpdateFlowMediaStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_UpdateFlowMediaStream_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-response-flowArn"></a>
The ARN of the flow that is associated with the media stream that you updated.
Type: String

 ** [mediaStream](#API_UpdateFlowMediaStream_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowMediaStream-response-mediaStream"></a>
The media stream that you updated.
Type: [MediaStream](API_MediaStream.md) object

## Errors
<a name="API_UpdateFlowMediaStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_UpdateFlowMediaStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateFlowMediaStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateFlowMediaStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
