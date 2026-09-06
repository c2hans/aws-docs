---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_VerifyDestinationNumber.html
---

# VerifyDestinationNumber
<a name="API_VerifyDestinationNumber"></a>

Use the verification code that was received by the verified destination phone number to opt-in the verified destination phone number to receive more messages.

## Request Syntax
<a name="API_VerifyDestinationNumber_RequestSyntax"></a>

```
{
   "VerificationCode": "{{string}}",
   "VerifiedDestinationNumberId": "{{string}}"
}
```

## Request Parameters
<a name="API_VerifyDestinationNumber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VerificationCode](#API_VerifyDestinationNumber_RequestSyntax) **   <a name="pinpoint-VerifyDestinationNumber-request-VerificationCode"></a>
The verification code that was received by the verified destination phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [VerifiedDestinationNumberId](#API_VerifyDestinationNumber_RequestSyntax) **   <a name="pinpoint-VerifyDestinationNumber-request-VerifiedDestinationNumberId"></a>
The unique identifier for the verififed destination phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_VerifyDestinationNumber_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DestinationPhoneNumber": "string",
   "Status": "string",
   "VerifiedDestinationNumberArn": "string",
   "VerifiedDestinationNumberId": "string"
}
```

## Response Elements
<a name="API_VerifyDestinationNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_VerifyDestinationNumber_ResponseSyntax) **   <a name="pinpoint-VerifyDestinationNumber-response-CreatedTimestamp"></a>
The time when the destination phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DestinationPhoneNumber](#API_VerifyDestinationNumber_ResponseSyntax) **   <a name="pinpoint-VerifyDestinationNumber-response-DestinationPhoneNumber"></a>
The phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [Status](#API_VerifyDestinationNumber_ResponseSyntax) **   <a name="pinpoint-VerifyDestinationNumber-response-Status"></a>
The status for being able to send messages to the phone number.
Type: String
Valid Values: `PENDING | VERIFIED | UNSUPPORTED`

 ** [VerifiedDestinationNumberArn](#API_VerifyDestinationNumber_ResponseSyntax) **   <a name="pinpoint-VerifyDestinationNumber-response-VerifiedDestinationNumberArn"></a>
The Amazon Resource Name (ARN) for the verified destination phone number.
Type: String

 ** [VerifiedDestinationNumberId](#API_VerifyDestinationNumber_ResponseSyntax) **   <a name="pinpoint-VerifyDestinationNumber-response-VerifiedDestinationNumberId"></a>
The unique identifier for the verified destination phone number.
Type: String

## Errors
<a name="API_VerifyDestinationNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_VerifyDestinationNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/VerifyDestinationNumber)
