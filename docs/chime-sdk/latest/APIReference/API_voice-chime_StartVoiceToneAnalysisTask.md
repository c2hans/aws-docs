---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartVoiceToneAnalysisTask.html
---

# StartVoiceToneAnalysisTask
<a name="API_voice-chime_StartVoiceToneAnalysisTask"></a>

Starts a voice tone analysis task. For more information about voice tone analysis, see [Using Amazon Chime SDK voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html) in the *Amazon Chime SDK Developer Guide*.

**Important**
Before starting any voice tone analysis tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the [AWS service terms](https://aws.amazon.com/service-terms/) for the Amazon Chime SDK.

## Request Syntax
<a name="API_voice-chime_StartVoiceToneAnalysisTask_RequestSyntax"></a>

```
POST /voice-connectors/{{VoiceConnectorId}}/voice-tone-analysis-tasks HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "LanguageCode": "{{string}}",
   "TransactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_StartVoiceToneAnalysisTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VoiceConnectorId](#API_voice-chime_StartVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_StartVoiceToneAnalysisTask-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_StartVoiceToneAnalysisTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_voice-chime_StartVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_StartVoiceToneAnalysisTask-request-ClientRequestToken"></a>
The unique identifier for the client request. Use a different token for different voice tone analysis tasks.
Type: String
Pattern: `^[-_a-zA-Z0-9]*${2,64}$`
Required: No

 ** [LanguageCode](#API_voice-chime_StartVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_StartVoiceToneAnalysisTask-request-LanguageCode"></a>
The language code.
Type: String
Valid Values: `en-US`
Required: Yes

 ** [TransactionId](#API_voice-chime_StartVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_StartVoiceToneAnalysisTask-request-TransactionId"></a>
The transaction ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_voice-chime_StartVoiceToneAnalysisTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "VoiceToneAnalysisTask": {
      "CallDetails": {
         "IsCaller": boolean,
         "TransactionId": "string",
         "VoiceConnectorId": "string"
      },
      "CreatedTimestamp": "string",
      "StartedTimestamp": "string",
      "StatusMessage": "string",
      "UpdatedTimestamp": "string",
      "VoiceToneAnalysisTaskId": "string",
      "VoiceToneAnalysisTaskStatus": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_StartVoiceToneAnalysisTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [VoiceToneAnalysisTask](#API_voice-chime_StartVoiceToneAnalysisTask_ResponseSyntax) **   <a name="chimesdk-voice-chime_StartVoiceToneAnalysisTask-response-VoiceToneAnalysisTask"></a>
The details of the voice tone analysis task.
Type: [VoiceToneAnalysisTask](API_voice-chime_VoiceToneAnalysisTask.md) object

## Errors
<a name="API_voice-chime_StartVoiceToneAnalysisTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** GoneException **
Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.
HTTP Status Code: 410

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

 ** UnprocessableEntityException **
A well-formed request couldn't be followed due to semantic errors.
HTTP Status Code: 422

## See Also
<a name="API_voice-chime_StartVoiceToneAnalysisTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/StartVoiceToneAnalysisTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
