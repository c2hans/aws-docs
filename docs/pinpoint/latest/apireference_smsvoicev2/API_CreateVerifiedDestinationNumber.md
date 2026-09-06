---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateVerifiedDestinationNumber.html
---

# CreateVerifiedDestinationNumber
<a name="API_CreateVerifiedDestinationNumber"></a>

You can only send messages to verified destination numbers when your account is in the sandbox. You can add up to 10 verified destination numbers.

## Request Syntax
<a name="API_CreateVerifiedDestinationNumber_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DestinationPhoneNumber": "{{string}}",
   "RcsAgentId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateVerifiedDestinationNumber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateVerifiedDestinationNumber_RequestSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DestinationPhoneNumber](#API_CreateVerifiedDestinationNumber_RequestSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-request-DestinationPhoneNumber"></a>
The verified destination phone number, in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [RcsAgentId](#API_CreateVerifiedDestinationNumber_RequestSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-request-RcsAgentId"></a>
The unique identifier of the RCS agent to associate with the verified destination number. You can use either the RcsAgentId or RcsAgentArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Tags](#API_CreateVerifiedDestinationNumber_RequestSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-request-Tags"></a>
An array of tags (key and value pairs) to associate with the destination number.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateVerifiedDestinationNumber_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DestinationPhoneNumber": "string",
   "RcsAgentId": "string",
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "VerifiedDestinationNumberArn": "string",
   "VerifiedDestinationNumberId": "string"
}
```

## Response Elements
<a name="API_CreateVerifiedDestinationNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-CreatedTimestamp"></a>
The time when the verified phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DestinationPhoneNumber](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-DestinationPhoneNumber"></a>
The verified destination phone number, in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [RcsAgentId](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-RcsAgentId"></a>
The unique identifier of the RCS agent associated with the verified destination number.
Type: String

 ** [Status](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-Status"></a>
The status of the verified destination phone number.
+  `PENDING`: The phone number hasn't been verified yet.
+  `VERIFIED`: The phone number is verified and can receive messages.
Type: String
Valid Values: `PENDING | VERIFIED | UNSUPPORTED`

 ** [Tags](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-Tags"></a>
An array of tags (key and value pairs) to associate with the destination number.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [VerifiedDestinationNumberArn](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-VerifiedDestinationNumberArn"></a>
The Amazon Resource Name (ARN) for the verified destination phone number.
Type: String

 ** [VerifiedDestinationNumberId](#API_CreateVerifiedDestinationNumber_ResponseSyntax) **   <a name="pinpoint-CreateVerifiedDestinationNumber-response-VerifiedDestinationNumberId"></a>
The unique identifier for the verified destination phone number.
Type: String

## Errors
<a name="API_CreateVerifiedDestinationNumber_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
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
<a name="API_CreateVerifiedDestinationNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateVerifiedDestinationNumber)
