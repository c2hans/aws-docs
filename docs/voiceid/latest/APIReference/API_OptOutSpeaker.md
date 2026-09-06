---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_OptOutSpeaker.html
---

# OptOutSpeaker
<a name="API_connect-voice-id_OptOutSpeaker"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Opts out a speaker from Voice ID. A speaker can be opted out regardless of whether or not they already exist in Voice ID. If they don't yet exist, a new speaker is created in an opted out state. If they already exist, their existing status is overridden and they are opted out. Enrollment and evaluation authentication requests are rejected for opted out speakers, and opted out speakers have no voice embeddings stored in Voice ID.

## Request Syntax
<a name="API_connect-voice-id_OptOutSpeaker_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "SpeakerId": "{{string}}"
}
```

## Request Parameters
<a name="API_connect-voice-id_OptOutSpeaker_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_connect-voice-id_OptOutSpeaker_RequestSyntax) **   <a name="connect-connect-voice-id_OptOutSpeaker-request-DomainId"></a>
The identifier of the domain that contains the speaker.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: Yes

 ** [SpeakerId](#API_connect-voice-id_OptOutSpeaker_RequestSyntax) **   <a name="connect-connect-voice-id_OptOutSpeaker-request-SpeakerId"></a>
The identifier of the speaker you want opted-out.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(id#[a-zA-Z0-9]{22}|[a-zA-Z0-9][a-zA-Z0-9_-]*)`
Required: Yes

## Response Syntax
<a name="API_connect-voice-id_OptOutSpeaker_ResponseSyntax"></a>

```
{
   "Speaker": {
      "CreatedAt": number,
      "CustomerSpeakerId": "string",
      "DomainId": "string",
      "GeneratedSpeakerId": "string",
      "LastAccessedAt": number,
      "Status": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_connect-voice-id_OptOutSpeaker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Speaker](#API_connect-voice-id_OptOutSpeaker_ResponseSyntax) **   <a name="connect-connect-voice-id_OptOutSpeaker-response-Speaker"></a>
Details about the opted-out speaker.
Type: [Speaker](API_connect-voice-id_Speaker.md) object

## Errors
<a name="API_connect-voice-id_OptOutSpeaker_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** ConflictException **
The request failed due to a conflict. Check the `ConflictType` and error message for more details.
 ** ConflictType **
The type of conflict which caused a ConflictException. Possible types and the corresponding error messages are as follows:
+  `DOMAIN_NOT_ACTIVE`: The domain is not active.
+  `CANNOT_CHANGE_SPEAKER_AFTER_ENROLLMENT`: You cannot change the speaker ID after an enrollment has been requested.
+  `ENROLLMENT_ALREADY_EXISTS`: There is already an enrollment for this session.
+  `SPEAKER_NOT_SET`: You must set the speaker ID before requesting an enrollment.
+  `SPEAKER_OPTED_OUT`: You cannot request an enrollment for an opted out speaker.
+  `CONCURRENT_CHANGES`: The request could not be processed as the resource was modified by another request during execution.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found. Check the `ResourceType` and error message for more details.
 ** ResourceType **
The type of resource which cannot not be found. Possible types are `BATCH_JOB`, `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeded the service quota. Refer to [Voice ID Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas) and try your request again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_OptOutSpeaker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/OptOutSpeaker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/OptOutSpeaker)
