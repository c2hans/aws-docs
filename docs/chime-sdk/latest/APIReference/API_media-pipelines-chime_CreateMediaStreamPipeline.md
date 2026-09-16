---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaStreamPipeline.html
---

# CreateMediaStreamPipeline
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline"></a>

Creates a streaming media pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_RequestSyntax"></a>

```
POST /sdk-media-stream-pipelines HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Sinks": [
      {
         "MediaStreamType": "{{string}}",
         "ReservedStreamCapacity": {{number}},
         "SinkArn": "{{string}}",
         "SinkType": "{{string}}"
      }
   ],
   "Sources": [
      {
         "SourceArn": "{{string}}",
         "SourceType": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaStreamPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaStreamPipeline-request-ClientRequestToken"></a>
The token assigned to the client making the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Sinks](#API_media-pipelines-chime_CreateMediaStreamPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaStreamPipeline-request-Sinks"></a>
The data sink for the media pipeline.
Type: Array of [MediaStreamSink](API_media-pipelines-chime_MediaStreamSink.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [Sources](#API_media-pipelines-chime_CreateMediaStreamPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaStreamPipeline-request-Sources"></a>
The data sources for the media pipeline.
Type: Array of [MediaStreamSource](API_media-pipelines-chime_MediaStreamSource.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [Tags](#API_media-pipelines-chime_CreateMediaStreamPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaStreamPipeline-request-Tags"></a>
The tags assigned to the media pipeline.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "MediaStreamPipeline": {
      "CreatedTimestamp": "string",
      "MediaPipelineArn": "string",
      "MediaPipelineId": "string",
      "Sinks": [
         {
            "MediaStreamType": "string",
            "ReservedStreamCapacity": number,
            "SinkArn": "string",
            "SinkType": "string"
         }
      ],
      "Sources": [
         {
            "SourceArn": "string",
            "SourceType": "string"
         }
      ],
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [MediaStreamPipeline](#API_media-pipelines-chime_CreateMediaStreamPipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaStreamPipeline-response-MediaStreamPipeline"></a>
The requested media pipeline.
Type: [MediaStreamPipeline](API_media-pipelines-chime_MediaStreamPipeline.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 404

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 401

## See Also
<a name="API_media-pipelines-chime_CreateMediaStreamPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaStreamPipeline)
