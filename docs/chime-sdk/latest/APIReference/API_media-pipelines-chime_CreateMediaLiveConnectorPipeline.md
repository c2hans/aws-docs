---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaLiveConnectorPipeline.html
---

# CreateMediaLiveConnectorPipeline
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline"></a>

Creates a media live connector pipeline in an Amazon Chime SDK meeting.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestSyntax"></a>

```
POST /sdk-media-live-connector-pipelines HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Sinks": [
      {
         "RTMPConfiguration": {
            "AudioChannels": "{{string}}",
            "AudioSampleRate": "{{string}}",
            "Url": "{{string}}"
         },
         "SinkType": "{{string}}"
      }
   ],
   "Sources": [
      {
         "ChimeSdkMeetingLiveConnectorConfiguration": {
            "Arn": "{{string}}",
            "CompositedVideo": {
               "GridViewConfiguration": {
                  "ActiveSpeakerOnlyConfiguration": {
                     "ActiveSpeakerPosition": "{{string}}"
                  },
                  "CanvasOrientation": "{{string}}",
                  "ContentShareLayout": "{{string}}",
                  "HorizontalLayoutConfiguration": {
                     "TileAspectRatio": "{{string}}",
                     "TileCount": {{number}},
                     "TileOrder": "{{string}}",
                     "TilePosition": "{{string}}"
                  },
                  "PresenterOnlyConfiguration": {
                     "PresenterPosition": "{{string}}"
                  },
                  "VerticalLayoutConfiguration": {
                     "TileAspectRatio": "{{string}}",
                     "TileCount": {{number}},
                     "TileOrder": "{{string}}",
                     "TilePosition": "{{string}}"
                  },
                  "VideoAttribute": {
                     "BorderColor": "{{string}}",
                     "BorderThickness": {{number}},
                     "CornerRadius": {{number}},
                     "HighlightColor": "{{string}}"
                  }
               },
               "Layout": "{{string}}",
               "Resolution": "{{string}}"
            },
            "MuxType": "{{string}}",
            "SourceConfiguration": {
               "SelectedVideoStreams": {
                  "AttendeeIds": [ "{{string}}" ],
                  "ExternalUserIds": [ "{{string}}" ]
               }
            }
         },
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
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaLiveConnectorPipeline-request-ClientRequestToken"></a>
The token assigned to the client making the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Sinks](#API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaLiveConnectorPipeline-request-Sinks"></a>
The media live connector pipeline's data sinks.
Type: Array of [LiveConnectorSinkConfiguration](API_media-pipelines-chime_LiveConnectorSinkConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Sources](#API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaLiveConnectorPipeline-request-Sources"></a>
The media live connector pipeline's data sources.
Type: Array of [LiveConnectorSourceConfiguration](API_media-pipelines-chime_LiveConnectorSourceConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Tags](#API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaLiveConnectorPipeline-request-Tags"></a>
The tags associated with the media live connector pipeline.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "MediaLiveConnectorPipeline": {
      "CreatedTimestamp": "string",
      "MediaPipelineArn": "string",
      "MediaPipelineId": "string",
      "Sinks": [
         {
            "RTMPConfiguration": {
               "AudioChannels": "string",
               "AudioSampleRate": "string",
               "Url": "string"
            },
            "SinkType": "string"
         }
      ],
      "Sources": [
         {
            "ChimeSdkMeetingLiveConnectorConfiguration": {
               "Arn": "string",
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
               "MuxType": "string",
               "SourceConfiguration": {
                  "SelectedVideoStreams": {
                     "AttendeeIds": [ "string" ],
                     "ExternalUserIds": [ "string" ]
                  }
               }
            },
            "SourceType": "string"
         }
      ],
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [MediaLiveConnectorPipeline](#API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaLiveConnectorPipeline-response-MediaLiveConnectorPipeline"></a>
The new media live connector pipeline.
Type: [MediaLiveConnectorPipeline](API_media-pipelines-chime_MediaLiveConnectorPipeline.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_Errors"></a>

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
<a name="API_media-pipelines-chime_CreateMediaLiveConnectorPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaLiveConnectorPipeline)
