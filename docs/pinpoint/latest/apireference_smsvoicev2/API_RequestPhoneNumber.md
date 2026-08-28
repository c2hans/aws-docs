---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestPhoneNumber.html
---

# RequestPhoneNumber
<a name="API_RequestPhoneNumber"></a>

Request an origination phone number for use in your account. For more information on phone number request see [Request a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html) in the * AWS End User Messaging SMS User Guide*.

## Request Syntax
<a name="API_RequestPhoneNumber_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "InternationalSendingEnabled": {{boolean}},
   "IsoCountryCode": "{{string}}",
   "MessageType": "{{string}}",
   "NumberCapabilities": [ "{{string}}" ],
   "NumberType": "{{string}}",
   "OptOutListName": "{{string}}",
   "PoolId": "{{string}}",
   "RegistrationId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RequestPhoneNumber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DeletionProtectionEnabled](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the phone number can't be deleted.
Type: Boolean
Required: No

 ** [InternationalSendingEnabled](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-InternationalSendingEnabled"></a>
By default this is set to false. When set to true the international sending of phone number is Enabled.
Type: Boolean
Required: No

 ** [IsoCountryCode](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** [MessageType](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-MessageType"></a>
The type of message. Valid values are `TRANSACTIONAL` for messages that are critical or time-sensitive and `PROMOTIONAL` for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: Yes

 ** [NumberCapabilities](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-NumberCapabilities"></a>
Indicates if the phone number will be used for text messages, voice messages, or both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** [NumberType](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-NumberType"></a>
The type of phone number to request.
When you request a `SIMULATOR` phone number, you must set **MessageType** as `TRANSACTIONAL`.
Type: String
Valid Values: `LONG_CODE | TOLL_FREE | TEN_DLC | SIMULATOR`
Required: Yes

 ** [OptOutListName](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-OptOutListName"></a>
The name of the OptOutList to associate with the phone number. You can use the OptOutListName or OptOutListArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [PoolId](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-PoolId"></a>
The pool to associated with the phone number. You can use the PoolId or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: No

 ** [RegistrationId](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-RegistrationId"></a>
Use this field to attach your phone number for an external registration process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Tags](#API_RequestPhoneNumber_RequestSyntax) **   <a name="pinpoint-RequestPhoneNumber-request-Tags"></a>
An array of tags (key and value pairs) to associate with the requested phone number.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_RequestPhoneNumber_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DeletionProtectionEnabled": boolean,
   "InternationalSendingEnabled": boolean,
   "IsoCountryCode": "string",
   "MessageType": "string",
   "MonthlyLeasingPrice": "string",
   "NumberCapabilities": [ "string" ],
   "NumberType": "string",
   "OptOutListName": "string",
   "PhoneNumber": "string",
   "PhoneNumberArn": "string",
   "PhoneNumberId": "string",
   "PoolId": "string",
   "RegistrationId": "string",
   "SelfManagedOptOutsEnabled": boolean,
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean
}
```

## Response Elements
<a name="API_RequestPhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-CreatedTimestamp"></a>
The time when the phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the phone number can't be deleted.
Type: Boolean

 ** [InternationalSendingEnabled](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-InternationalSendingEnabled"></a>
By default this is set to false. When set to true the international sending of phone number is Enabled.
Type: Boolean

 ** [IsoCountryCode](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [MessageType](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-MessageType"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [MonthlyLeasingPrice](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-MonthlyLeasingPrice"></a>
The monthly price, in US dollars, to lease the phone number.
Type: String

 ** [NumberCapabilities](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-NumberCapabilities"></a>
Indicates if the phone number will be used for text messages, voice messages or both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`

 ** [NumberType](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-NumberType"></a>
The type of number that was released.
Type: String
Valid Values: `LONG_CODE | TOLL_FREE | TEN_DLC | SIMULATOR`

 ** [OptOutListName](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-OptOutListName"></a>
The name of the OptOutList that is associated with the requested phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PhoneNumber](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-PhoneNumber"></a>
The new phone number that was requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [PhoneNumberArn](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the requested phone number.
Type: String

 ** [PhoneNumberId](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-PhoneNumberId"></a>
The unique identifier of the new phone number.
Type: String

 ** [PoolId](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-PoolId"></a>
The unique identifier of the pool associated with the phone number
Type: String

 ** [RegistrationId](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [Status](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-Status"></a>
The current status of the request.
Type: String
Valid Values: `PENDING | ACTIVE | ASSOCIATING | DISASSOCIATING | DELETED`

 ** [Tags](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-Tags"></a>
An array of key and value pair tags that are associated with the phone number.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [TwoWayChannelArn](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-TwoWayChannelArn"></a>
The ARN used to identify the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_RequestPhoneNumber_ResponseSyntax) **   <a name="pinpoint-RequestPhoneNumber-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

## Errors
<a name="API_RequestPhoneNumber_Errors"></a>

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
<a name="API_RequestPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RequestPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
