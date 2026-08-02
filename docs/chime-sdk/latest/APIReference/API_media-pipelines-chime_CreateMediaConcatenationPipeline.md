---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html
---

# CreateMediaConcatenationPipeline
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline"></a>

Creates a media concatenation pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestSyntax"></a>

```
POST /sdk-media-concatenation-pipelines HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Sinks": [
      {
         "S3BucketSinkConfiguration": {
            "Destination": "{{string}}"
         },
         "Type": "{{string}}"
      }
   ],
   "Sources": [
      {
         "MediaCapturePipelineSourceConfiguration": {
            "ChimeSdkMeetingConfiguration": {
               "ArtifactsConfiguration": {
                  "Audio": {
                     "State": "{{string}}"
                  },
                  "CompositedVideo": {
                     "State": "{{string}}"
                  },
                  "Content": {
                     "State": "{{string}}"
                  },
                  "DataChannel": {
                     "State": "{{string}}"
                  },
                  "MeetingEvents": {
                     "State": "{{string}}"
                  },
                  "TranscriptionMessages": {
                     "State": "{{string}}"
                  },
                  "Video": {
                     "State": "{{string}}"
                  }
               }
            },
            "MediaPipelineArn": "{{string}}"
         },
         "Type": "{{string}}"
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
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaConcatenationPipeline-request-ClientRequestToken"></a>
The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media concatenation pipeline request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Sinks](#API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaConcatenationPipeline-request-Sinks"></a>
An object that specifies the data sinks for the media concatenation pipeline.
Type: Array of [ConcatenationSink](API_media-pipelines-chime_ConcatenationSink.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Sources](#API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaConcatenationPipeline-request-Sources"></a>
An object that specifies the sources for the media concatenation pipeline.
Type: Array of [ConcatenationSource](API_media-pipelines-chime_ConcatenationSource.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Tags](#API_media-pipelines-chime_CreateMediaConcatenationPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaConcatenationPipeline-request-Tags"></a>
The tags associated with the media concatenation pipeline.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "MediaConcatenationPipeline": {
      "CreatedTimestamp": "string",
      "MediaPipelineArn": "string",
      "MediaPipelineId": "string",
      "Sinks": [
         {
            "S3BucketSinkConfiguration": {
               "Destination": "string"
            },
            "Type": "string"
         }
      ],
      "Sources": [
         {
            "MediaCapturePipelineSourceConfiguration": {
               "ChimeSdkMeetingConfiguration": {
                  "ArtifactsConfiguration": {
                     "Audio": {
                        "State": "string"
                     },
                     "CompositedVideo": {
                        "State": "string"
                     },
                     "Content": {
                        "State": "string"
                     },
                     "DataChannel": {
                        "State": "string"
                     },
                     "MeetingEvents": {
                        "State": "string"
                     },
                     "TranscriptionMessages": {
                        "State": "string"
                     },
                     "Video": {
                        "State": "string"
                     }
                  }
               },
               "MediaPipelineArn": "string"
            },
            "Type": "string"
         }
      ],
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [MediaConcatenationPipeline](#API_media-pipelines-chime_CreateMediaConcatenationPipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaConcatenationPipeline-response-MediaConcatenationPipeline"></a>
A media concatenation pipeline object, the ID, source type, `MediaPipelineARN`, and sink of a media concatenation pipeline object.
Type: [MediaConcatenationPipeline](API_media-pipelines-chime_MediaConcatenationPipeline.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_Errors"></a>

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
<a name="API_media-pipelines-chime_CreateMediaConcatenationPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaConcatenationPipeline)
