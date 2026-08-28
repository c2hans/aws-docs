---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration.html
---

# UpdateMediaInsightsPipelineConfiguration
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration"></a>

Updates the media insights pipeline's configuration settings.

## Request Syntax
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestSyntax"></a>

```
PUT /media-insights-pipeline-configurations/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "Elements": [
      {
         "AmazonTranscribeCallAnalyticsProcessorConfiguration": {
            "CallAnalyticsStreamCategories": [ "{{string}}" ],
            "ContentIdentificationType": "{{string}}",
            "ContentRedactionType": "{{string}}",
            "EnablePartialResultsStabilization": {{boolean}},
            "FilterPartialResults": {{boolean}},
            "LanguageCode": "{{string}}",
            "LanguageModelName": "{{string}}",
            "PartialResultsStability": "{{string}}",
            "PiiEntityTypes": "{{string}}",
            "PostCallAnalyticsSettings": {
               "ContentRedactionOutput": "{{string}}",
               "DataAccessRoleArn": "{{string}}",
               "OutputEncryptionKMSKeyId": "{{string}}",
               "OutputLocation": "{{string}}"
            },
            "VocabularyFilterMethod": "{{string}}",
            "VocabularyFilterName": "{{string}}",
            "VocabularyName": "{{string}}"
         },
         "AmazonTranscribeProcessorConfiguration": {
            "ContentIdentificationType": "{{string}}",
            "ContentRedactionType": "{{string}}",
            "EnablePartialResultsStabilization": {{boolean}},
            "FilterPartialResults": {{boolean}},
            "IdentifyLanguage": {{boolean}},
            "IdentifyMultipleLanguages": {{boolean}},
            "LanguageCode": "{{string}}",
            "LanguageModelName": "{{string}}",
            "LanguageOptions": "{{string}}",
            "PartialResultsStability": "{{string}}",
            "PiiEntityTypes": "{{string}}",
            "PreferredLanguage": "{{string}}",
            "ShowSpeakerLabel": {{boolean}},
            "VocabularyFilterMethod": "{{string}}",
            "VocabularyFilterName": "{{string}}",
            "VocabularyFilterNames": "{{string}}",
            "VocabularyName": "{{string}}",
            "VocabularyNames": "{{string}}"
         },
         "KinesisDataStreamSinkConfiguration": {
            "InsightsTarget": "{{string}}"
         },
         "LambdaFunctionSinkConfiguration": {
            "InsightsTarget": "{{string}}"
         },
         "S3RecordingSinkConfiguration": {
            "Destination": "{{string}}",
            "RecordingFileFormat": "{{string}}"
         },
         "SnsTopicSinkConfiguration": {
            "InsightsTarget": "{{string}}"
         },
         "SqsQueueSinkConfiguration": {
            "InsightsTarget": "{{string}}"
         },
         "Type": "{{string}}",
         "VoiceAnalyticsProcessorConfiguration": {
            "SpeakerSearchStatus": "{{string}}",
            "VoiceToneAnalysisStatus": "{{string}}"
         },
         "VoiceEnhancementSinkConfiguration": {
            "Disabled": {{boolean}}
         }
      }
   ],
   "RealTimeAlertConfiguration": {
      "Disabled": {{boolean}},
      "Rules": [
         {
            "IssueDetectionConfiguration": {
               "RuleName": "{{string}}"
            },
            "KeywordMatchConfiguration": {
               "Keywords": [ "{{string}}" ],
               "Negate": {{boolean}},
               "RuleName": "{{string}}"
            },
            "SentimentConfiguration": {
               "RuleName": "{{string}}",
               "SentimentType": "{{string}}",
               "TimePeriod": {{number}}
            },
            "Type": "{{string}}"
         }
      ]
   },
   "ResourceAccessRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration-request-uri-Identifier"></a>
The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration.
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Elements](#API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration-request-Elements"></a>
The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream..
Type: Array of [MediaInsightsPipelineConfigurationElement](API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement.md) objects
Required: Yes

 ** [RealTimeAlertConfiguration](#API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration-request-RealTimeAlertConfiguration"></a>
The configuration settings for real-time alerts for the media insights pipeline.
Type: [RealTimeAlertConfiguration](API_media-pipelines-chime_RealTimeAlertConfiguration.md) object
Required: No

 ** [ResourceAccessRoleArn](#API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration-request-ResourceAccessRoleArn"></a>
The ARN of the role used by the service to access AWS resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

## Response Syntax
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MediaInsightsPipelineConfiguration": {
      "CreatedTimestamp": "string",
      "Elements": [
         {
            "AmazonTranscribeCallAnalyticsProcessorConfiguration": {
               "CallAnalyticsStreamCategories": [ "string" ],
               "ContentIdentificationType": "string",
               "ContentRedactionType": "string",
               "EnablePartialResultsStabilization": boolean,
               "FilterPartialResults": boolean,
               "LanguageCode": "string",
               "LanguageModelName": "string",
               "PartialResultsStability": "string",
               "PiiEntityTypes": "string",
               "PostCallAnalyticsSettings": {
                  "ContentRedactionOutput": "string",
                  "DataAccessRoleArn": "string",
                  "OutputEncryptionKMSKeyId": "string",
                  "OutputLocation": "string"
               },
               "VocabularyFilterMethod": "string",
               "VocabularyFilterName": "string",
               "VocabularyName": "string"
            },
            "AmazonTranscribeProcessorConfiguration": {
               "ContentIdentificationType": "string",
               "ContentRedactionType": "string",
               "EnablePartialResultsStabilization": boolean,
               "FilterPartialResults": boolean,
               "IdentifyLanguage": boolean,
               "IdentifyMultipleLanguages": boolean,
               "LanguageCode": "string",
               "LanguageModelName": "string",
               "LanguageOptions": "string",
               "PartialResultsStability": "string",
               "PiiEntityTypes": "string",
               "PreferredLanguage": "string",
               "ShowSpeakerLabel": boolean,
               "VocabularyFilterMethod": "string",
               "VocabularyFilterName": "string",
               "VocabularyFilterNames": "string",
               "VocabularyName": "string",
               "VocabularyNames": "string"
            },
            "KinesisDataStreamSinkConfiguration": {
               "InsightsTarget": "string"
            },
            "LambdaFunctionSinkConfiguration": {
               "InsightsTarget": "string"
            },
            "S3RecordingSinkConfiguration": {
               "Destination": "string",
               "RecordingFileFormat": "string"
            },
            "SnsTopicSinkConfiguration": {
               "InsightsTarget": "string"
            },
            "SqsQueueSinkConfiguration": {
               "InsightsTarget": "string"
            },
            "Type": "string",
            "VoiceAnalyticsProcessorConfiguration": {
               "SpeakerSearchStatus": "string",
               "VoiceToneAnalysisStatus": "string"
            },
            "VoiceEnhancementSinkConfiguration": {
               "Disabled": boolean
            }
         }
      ],
      "MediaInsightsPipelineConfigurationArn": "string",
      "MediaInsightsPipelineConfigurationId": "string",
      "MediaInsightsPipelineConfigurationName": "string",
      "RealTimeAlertConfiguration": {
         "Disabled": boolean,
         "Rules": [
            {
               "IssueDetectionConfiguration": {
                  "RuleName": "string"
               },
               "KeywordMatchConfiguration": {
                  "Keywords": [ "string" ],
                  "Negate": boolean,
                  "RuleName": "string"
               },
               "SentimentConfiguration": {
                  "RuleName": "string",
                  "SentimentType": "string",
                  "TimePeriod": number
               },
               "Type": "string"
            }
         ]
      },
      "ResourceAccessRoleArn": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MediaInsightsPipelineConfiguration](#API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration-response-MediaInsightsPipelineConfiguration"></a>
The updated configuration settings.
Type: [MediaInsightsPipelineConfiguration](API_media-pipelines-chime_MediaInsightsPipelineConfiguration.md) object

## Errors
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 409

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
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
