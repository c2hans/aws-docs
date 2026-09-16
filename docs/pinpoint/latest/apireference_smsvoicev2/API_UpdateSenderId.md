---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateSenderId.html
---

# UpdateSenderId
<a name="API_UpdateSenderId"></a>

Updates the configuration of an existing sender ID.

## Request Syntax
<a name="API_UpdateSenderId_RequestSyntax"></a>

```
{
   "DeletionProtectionEnabled": {{boolean}},
   "IsoCountryCode": "{{string}}",
   "SenderId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSenderId_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeletionProtectionEnabled](#API_UpdateSenderId_RequestSyntax) **   <a name="pinpoint-UpdateSenderId-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
Type: Boolean
Required: No

 ** [IsoCountryCode](#API_UpdateSenderId_RequestSyntax) **   <a name="pinpoint-UpdateSenderId-request-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** [SenderId](#API_UpdateSenderId_RequestSyntax) **   <a name="pinpoint-UpdateSenderId-request-SenderId"></a>
The sender ID to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateSenderId_ResponseSyntax"></a>

```
{
   "DeletionProtectionEnabled": boolean,
   "IsoCountryCode": "string",
   "MessageTypes": [ "string" ],
   "MonthlyLeasingPrice": "string",
   "Registered": boolean,
   "RegistrationId": "string",
   "SenderId": "string",
   "SenderIdArn": "string"
}
```

## Response Elements
<a name="API_UpdateSenderId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionProtectionEnabled](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
Type: Boolean

 ** [IsoCountryCode](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [MessageTypes](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-MessageTypes"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [MonthlyLeasingPrice](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-MonthlyLeasingPrice"></a>
The monthly price, in US dollars, to lease the sender ID.
Type: String

 ** [Registered](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-Registered"></a>
True if the sender ID is registered..
Type: Boolean

 ** [RegistrationId](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [SenderId](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-SenderId"></a>
The sender ID that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`

 ** [SenderIdArn](#API_UpdateSenderId_ResponseSyntax) **   <a name="pinpoint-UpdateSenderId-response-SenderIdArn"></a>
The Amazon Resource Name (ARN) associated with the SenderId.
Type: String

## Errors
<a name="API_UpdateSenderId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
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
<a name="API_UpdateSenderId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/UpdateSenderId)
