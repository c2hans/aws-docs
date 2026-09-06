---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html
---

# CreateMediaInsightsPipeline
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline"></a>

Creates a media insights pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax"></a>

```
POST /media-insights-pipelines HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "KinesisVideoStreamRecordingSourceRuntimeConfiguration": {
      "FragmentSelector": {
         "FragmentSelectorType": "{{string}}",
         "TimestampRange": {
            "EndTimestamp": {{number}},
            "StartTimestamp": {{number}}
         }
      },
      "Streams": [
         {
            "StreamArn": "{{string}}"
         }
      ]
   },
   "KinesisVideoStreamSourceRuntimeConfiguration": {
      "MediaEncoding": "{{string}}",
      "MediaSampleRate": {{number}},
      "Streams": [
         {
            "FragmentNumber": "{{string}}",
            "StreamArn": "{{string}}",
            "StreamChannelDefinition": {
               "ChannelDefinitions": [
                  {
                     "ChannelId": {{number}},
                     "ParticipantRole": "{{string}}"
                  }
               ],
               "NumberOfChannels": {{number}}
            }
         }
      ]
   },
   "MediaInsightsPipelineConfigurationArn": "{{string}}",
   "MediaInsightsRuntimeMetadata": {
      "{{string}}" : "{{string}}"
   },
   "S3RecordingSinkRuntimeConfiguration": {
      "Destination": "{{string}}",
      "RecordingFileFormat": "{{string}}"
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
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-ClientRequestToken"></a>
The unique identifier for the media insights pipeline request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [KinesisVideoStreamRecordingSourceRuntimeConfiguration](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-KinesisVideoStreamRecordingSourceRuntimeConfiguration"></a>
The runtime configuration for the Kinesis video recording stream source.
Type: [KinesisVideoStreamRecordingSourceRuntimeConfiguration](API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration.md) object
Required: No

 ** [KinesisVideoStreamSourceRuntimeConfiguration](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-KinesisVideoStreamSourceRuntimeConfiguration"></a>
The runtime configuration for the Kinesis video stream source of the media insights pipeline.
Type: [KinesisVideoStreamSourceRuntimeConfiguration](API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration.md) object
Required: No

 ** [MediaInsightsPipelineConfigurationArn](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-MediaInsightsPipelineConfigurationArn"></a>
The ARN of the pipeline's configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** [MediaInsightsRuntimeMetadata](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-MediaInsightsRuntimeMetadata"></a>
The runtime metadata for the media insights pipeline. Consists of a key-value map of strings.
Type: String to string map
Key Length Constraints: Maximum length of 1024.
Key Pattern: `.*\S.*`
Value Length Constraints: Maximum length of 4096.
Value Pattern: `.*`
Required: No

 ** [S3RecordingSinkRuntimeConfiguration](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-S3RecordingSinkRuntimeConfiguration"></a>
The runtime configuration for the S3 recording sink. If specified, the settings in this structure override any settings in `S3RecordingSinkConfiguration`.
Type: [S3RecordingSinkRuntimeConfiguration](API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.md) object
Required: No

 ** [Tags](#API_media-pipelines-chime_CreateMediaInsightsPipeline_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-request-Tags"></a>
The tags assigned to the media insights pipeline.
Type: Array of [Tag](API_media-pipelines-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "MediaInsightsPipeline": {
      "CreatedTimestamp": "string",
      "ElementStatuses": [
         {
            "Status": "string",
            "Type": "string"
         }
      ],
      "KinesisVideoStreamRecordingSourceRuntimeConfiguration": {
         "FragmentSelector": {
            "FragmentSelectorType": "string",
            "TimestampRange": {
               "EndTimestamp": number,
               "StartTimestamp": number
            }
         },
         "Streams": [
            {
               "StreamArn": "string"
            }
         ]
      },
      "KinesisVideoStreamSourceRuntimeConfiguration": {
         "MediaEncoding": "string",
         "MediaSampleRate": number,
         "Streams": [
            {
               "FragmentNumber": "string",
               "StreamArn": "string",
               "StreamChannelDefinition": {
                  "ChannelDefinitions": [
                     {
                        "ChannelId": number,
                        "ParticipantRole": "string"
                     }
                  ],
                  "NumberOfChannels": number
               }
            }
         ]
      },
      "MediaInsightsPipelineConfigurationArn": "string",
      "MediaInsightsRuntimeMetadata": {
         "string" : "string"
      },
      "MediaPipelineArn": "string",
      "MediaPipelineId": "string",
      "S3RecordingSinkRuntimeConfiguration": {
         "Destination": "string",
         "RecordingFileFormat": "string"
      },
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [MediaInsightsPipeline](#API_media-pipelines-chime_CreateMediaInsightsPipeline_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_CreateMediaInsightsPipeline-response-MediaInsightsPipeline"></a>
The media insights pipeline object.
Type: [MediaInsightsPipeline](API_media-pipelines-chime_MediaInsightsPipeline.md) object

## Errors
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_Errors"></a>

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
<a name="API_media-pipelines-chime_CreateMediaInsightsPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)
