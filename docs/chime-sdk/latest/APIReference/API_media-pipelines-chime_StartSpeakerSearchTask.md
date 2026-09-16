---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html
---

# StartSpeakerSearchTask
<a name="API_media-pipelines-chime_StartSpeakerSearchTask"></a>

Starts a speaker search task.

**Important**
Before starting any speaker search tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the [AWS service terms](https://aws.amazon.com/service-terms/) for the Amazon Chime SDK.

## Request Syntax
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_RequestSyntax"></a>

```
POST /media-insights-pipelines/{{identifier}}/speaker-search-tasks?operation=start HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "KinesisVideoStreamSourceTaskConfiguration": {
      "ChannelId": {{number}},
      "FragmentNumber": "{{string}}",
      "StreamArn": "{{string}}"
   },
   "VoiceProfileDomainArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_media-pipelines-chime_StartSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_StartSpeakerSearchTask-request-uri-Identifier"></a>
The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_media-pipelines-chime_StartSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_StartSpeakerSearchTask-request-ClientRequestToken"></a>
The unique identifier for the client request. Use a different token for different speaker search tasks.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [KinesisVideoStreamSourceTaskConfiguration](#API_media-pipelines-chime_StartSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_StartSpeakerSearchTask-request-KinesisVideoStreamSourceTaskConfiguration"></a>
The task configuration for the Kinesis video stream source of the media insights pipeline.
Type: [KinesisVideoStreamSourceTaskConfiguration](API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration.md) object
Required: No

 ** [VoiceProfileDomainArn](#API_media-pipelines-chime_StartSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_StartSpeakerSearchTask-request-VoiceProfileDomainArn"></a>
The ARN of the voice profile domain that will store the voice profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

## Response Syntax
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "SpeakerSearchTask": {
      "CreatedTimestamp": "string",
      "SpeakerSearchTaskId": "string",
      "SpeakerSearchTaskStatus": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [SpeakerSearchTask](#API_media-pipelines-chime_StartSpeakerSearchTask_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_StartSpeakerSearchTask-response-SpeakerSearchTask"></a>
The details of the speaker search task.
Type: [SpeakerSearchTask](API_media-pipelines-chime_SpeakerSearchTask.md) object

## Errors
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_Errors"></a>

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
<a name="API_media-pipelines-chime_StartSpeakerSearchTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/StartSpeakerSearchTask)
