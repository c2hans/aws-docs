---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html
---

# CreateVoiceProfile
<a name="API_voice-chime_CreateVoiceProfile"></a>

Creates a voice profile, which consists of an enrolled user and their latest voice print.

**Important**
Before creating any voice profiles, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the [AWS service terms](https://aws.amazon.com/service-terms/) for the Amazon Chime SDK.

For more information about voice profiles and voice analytics, see [Using Amazon Chime SDK Voice Analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html) in the *Amazon Chime SDK Developer Guide*.

## Request Syntax
<a name="API_voice-chime_CreateVoiceProfile_RequestSyntax"></a>

```
POST /voice-profiles HTTP/1.1
Content-type: application/json

{
   "SpeakerSearchTaskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateVoiceProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateVoiceProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SpeakerSearchTaskId](#API_voice-chime_CreateVoiceProfile_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfile-request-SpeakerSearchTaskId"></a>
The ID of the speaker search task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_voice-chime_CreateVoiceProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_voice-chime_CreateVoiceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [VoiceProfile](#API_voice-chime_CreateVoiceProfile_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfile-response-VoiceProfile"></a>
The requested voice profile.
Type: [VoiceProfile](API_voice-chime_VoiceProfile.md) object

## Errors
<a name="API_voice-chime_CreateVoiceProfile_Errors"></a>

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

## See Also
<a name="API_voice-chime_CreateVoiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateVoiceProfile)
