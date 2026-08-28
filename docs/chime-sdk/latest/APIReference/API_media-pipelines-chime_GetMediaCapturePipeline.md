---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html
---

# GetMediaCapturePipeline
<a name="API_media-pipelines-chime_GetMediaCapturePipeline"></a>

Gets an existing media pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_RequestSyntax"></a>

```
GET /sdk-media-capture-pipelines/{{mediaPipelineId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [mediaPipelineId](#API_media-pipelines-chime_GetMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_GetMediaCapturePipeline-request-uri-MediaPipelineId"></a>
The ID of the pipeline that you want to get.
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MediaCapturePipeline": {
      "ChimeSdkMeetingConfiguration": {
         "ArtifactsConfiguration": {
            "Audio": {
               "MuxType": "string"
            },
            "CompositedVideo": {
               "GridViewConfiguration": {
                  "ActiveSpeakerOnlyConfiguration": {
                     "ActiveSpeakerPosition": "string"
                  },
                  "CanvasOrientation": "string",
                  "ContentShareLayout": "string",
                  "HorizontalLayoutConfiguration": {
                     "TileAspectRatio": "string",
                     "TileCount": number,
                     "TileOrder": "string",
                     "TilePosition": "string"
                  },
                  "PresenterOnlyConfiguration": {
                     "PresenterPosition": "string"
                  },
                  "VerticalLayoutConfiguration": {
                     "TileAspectRatio": "string",
                     "TileCount": number,
                     "TileOrder": "string",
                     "TilePosition": "string"
                  },
                  "VideoAttribute": {
                     "BorderColor": "string",
                     "BorderThickness": number,
                     "CornerRadius": number,
                     "HighlightColor": "string"
                  }
               },
               "Layout": "string",
               "Resolution": "string"
            },
            "Content": {
               "MuxType": "string",
               "State": "string"
            },
            "Video": {
               "MuxType": "string",
               "State": "string"
            }
         },
         "SourceConfiguration": {
            "SelectedVideoStreams": {
               "AttendeeIds": [ "string" ],
               "ExternalUserIds": [ "string" ]
            }
         }
      },
      "CreatedTimestamp": "string",
      "MediaPipelineArn": "string",
      "MediaPipelineId": "string",
      "SinkArn": "string",
      "SinkIamRoleArn": "string",
      "SinkType": "string",
      "SourceArn": "string",
      "SourceType": "string",
      "SseAwsKeyManagementParams": {
         "AwsKmsEncryptionContext": "string",
         "AwsKmsKeyId": "string"
      },
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MediaCapturePipeline](#API_media-pipelines-chime_GetMediaCapturePipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_GetMediaCapturePipeline-response-MediaCapturePipeline"></a>
The media pipeline object.
Type: [MediaCapturePipeline](API_media-pipelines-chime_MediaCapturePipeline.md) object

## Errors
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_Errors"></a>

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
<a name="API_media-pipelines-chime_GetMediaCapturePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/GetMediaCapturePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
