---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html
---

# UpdateVoiceProfile
<a name="API_voice-chime_UpdateVoiceProfile"></a>

Updates the specified voice profile’s voice print and refreshes its expiration timestamp.

**Important**
As a condition of using this feature, you acknowledge that the collection, use, storage, and retention of your caller’s biometric identifiers and biometric information (“biometric data”) in the form of a digital voiceprint requires the caller’s informed consent via a written release. Such consent is required under various state laws, including biometrics laws in Illinois, Texas, Washington and other state privacy laws.
You must provide a written release to each caller through a process that clearly reflects each caller’s informed consent before using Amazon Chime SDK Voice Insights service, as required under the terms of your agreement with AWS governing your use of the service.

## Request Syntax
<a name="API_voice-chime_UpdateVoiceProfile_RequestSyntax"></a>

```
PUT /voice-profiles/{{VoiceProfileId}} HTTP/1.1
Content-type: application/json

{
   "SpeakerSearchTaskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateVoiceProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VoiceProfileId](#API_voice-chime_UpdateVoiceProfile_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceProfile-request-uri-VoiceProfileId"></a>
The profile ID.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateVoiceProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SpeakerSearchTaskId](#API_voice-chime_UpdateVoiceProfile_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceProfile-request-SpeakerSearchTaskId"></a>
The ID of the speaker search task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_voice-chime_UpdateVoiceProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VoiceProfile": {
      "CreatedTimestamp": "string",
      "ExpirationTimestamp": "string",
      "UpdatedTimestamp": "string",
      "VoiceProfileArn": "string",
      "VoiceProfileDomainId": "string",
      "VoiceProfileId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdateVoiceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VoiceProfile](#API_voice-chime_UpdateVoiceProfile_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceProfile-response-VoiceProfile"></a>
The updated voice profile settings.
Type: [VoiceProfile](API_voice-chime_VoiceProfile.md) object

## Errors
<a name="API_voice-chime_UpdateVoiceProfile_Errors"></a>

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

## See Also
<a name="API_voice-chime_UpdateVoiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateVoiceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
