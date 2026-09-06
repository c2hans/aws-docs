---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestSenderId.html
---

# RequestSenderId
<a name="API_RequestSenderId"></a>

Request a new sender ID that doesn't require registration.

## Request Syntax
<a name="API_RequestSenderId_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "IsoCountryCode": "{{string}}",
   "MessageTypes": [ "{{string}}" ],
   "SenderId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RequestSenderId_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DeletionProtectionEnabled](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
Type: Boolean
Required: No

 ** [IsoCountryCode](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** [MessageTypes](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-MessageTypes"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: No

 ** [SenderId](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-SenderId"></a>
The sender ID string to request. The sender ID can be 1-11 alphanumeric characters including letters (A-Z, a-z), numbers (0-9), or hyphens (-). The sender ID must contain at least one letter and cannot start or end with a hyphen.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Tags](#API_RequestSenderId_RequestSyntax) **   <a name="pinpoint-RequestSenderId-request-Tags"></a>
An array of tags (key and value pairs) to associate with the sender ID.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_RequestSenderId_ResponseSyntax"></a>

```
{
   "DeletionProtectionEnabled": boolean,
   "IsoCountryCode": "string",
   "MessageTypes": [ "string" ],
   "MonthlyLeasingPrice": "string",
   "Registered": boolean,
   "SenderId": "string",
   "SenderIdArn": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_RequestSenderId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionProtectionEnabled](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
Type: Boolean

 ** [IsoCountryCode](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [MessageTypes](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-MessageTypes"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [MonthlyLeasingPrice](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-MonthlyLeasingPrice"></a>
The monthly price, in US dollars, to lease the sender ID.
Type: String

 ** [Registered](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-Registered"></a>
True if the sender ID is registered.
Type: Boolean

 ** [SenderId](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-SenderId"></a>
The sender ID that was requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`

 ** [SenderIdArn](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-SenderIdArn"></a>
The Amazon Resource Name (ARN) associated with the SenderId.
Type: String

 ** [Tags](#API_RequestSenderId_ResponseSyntax) **   <a name="pinpoint-RequestSenderId-response-Tags"></a>
An array of tags (key and value pairs) to associate with the sender ID.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_RequestSenderId_Errors"></a>

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
<a name="API_RequestSenderId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RequestSenderId)
