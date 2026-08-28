---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html
---

# CreateMediaCapturePipeline
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline"></a>

Creates a media pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax"></a>

```
POST /sdk-media-capture-pipelines HTTP/1.1
Content-type: application/json

{
   "ChimeSdkMeetingConfiguration": {
      "ArtifactsConfiguration": {
         "Audio": {
            "MuxType": "{{string}}"
         },
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
         "Content": {
            "MuxType": "{{string}}",
            "State": "{{string}}"
         },
         "Video": {
            "MuxType": "{{string}}",
            "State": "{{string}}"
         }
      },
      "SourceConfiguration": {
         "SelectedVideoStreams": {
            "AttendeeIds": [ "{{string}}" ],
            "ExternalUserIds": [ "{{string}}" ]
         }
      }
   },
   "ClientRequestToken": "{{string}}",
   "SinkArn": "{{string}}",
   "SinkIamRoleArn": "{{string}}",
   "SinkType": "{{string}}",
   "SourceArn": "{{string}}",
   "SourceType": "{{string}}",
   "SseAwsKeyManagementParams": {
      "AwsKmsEncryptionContext": "{{string}}",
      "AwsKmsKeyId": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChimeSdkMeetingConfiguration](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-ChimeSdkMeetingConfiguration"></a>
The configuration for a specified media pipeline. `SourceType` must be `ChimeSdkMeeting`.
Type: [ChimeSdkMeetingConfiguration](API_media-pipelines-chime_ChimeSdkMeetingConfiguration.md) object
Required: No

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-ClientRequestToken"></a>
The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [SinkArn](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SinkArn"></a>
The ARN of the sink type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** [SinkIamRoleArn](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SinkIamRoleArn"></a>
The Amazon Resource Name (ARN) of the sink role to be used with `AwsKmsKeyId` in `SseAwsKeyManagementParams`. Can only interact with `S3Bucket` sink type. The role must belong to the caller’s account and be able to act on behalf of the caller during the API call. All minimum policy permissions requirements for the caller to perform sink-related actions are the same for `SinkIamRoleArn`.
Additionally, the role must have permission to `kms:GenerateDataKey` using KMS key supplied as `AwsKmsKeyId` in `SseAwsKeyManagementParams`. If media concatenation will be required later, the role must also have permission to `kms:Decrypt` for the same KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** [SinkType](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SinkType"></a>
Destination type to which the media artifacts are saved. You must use an S3 bucket.
Type: String
Valid Values: `S3Bucket`
Required: Yes

 ** [SourceArn](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SourceArn"></a>
ARN of the source from which the media artifacts are captured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** [SourceType](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SourceType"></a>
Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source.
Type: String
Valid Values: `ChimeSdkMeeting`
Required: Yes

 ** [SseAwsKeyManagementParams](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-SseAwsKeyManagementParams"></a>
An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.
Type: [SseAwsKeyManagementParams](API_media-pipelines-chime_SseAwsKeyManagementParams.md) object
Required: No

 ** [Tags](#API_media-pipelines-chime_CreateMediaCapturePipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-request-Tags"></a>
The tag key-value pairs.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [MediaCapturePipeline](#API_media-pipelines-chime_CreateMediaCapturePipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaCapturePipeline-response-MediaCapturePipeline"></a>
A media pipeline object, the ID, source type, source ARN, sink type, and sink ARN of a media pipeline object.
Type: [MediaCapturePipeline](API_media-pipelines-chime_MediaCapturePipeline.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_Errors"></a>

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
<a name="API_media-pipelines-chime_CreateMediaCapturePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaCapturePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
