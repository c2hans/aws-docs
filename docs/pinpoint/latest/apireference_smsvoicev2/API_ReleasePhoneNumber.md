---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ReleasePhoneNumber.html
---

# ReleasePhoneNumber
<a name="API_ReleasePhoneNumber"></a>

Releases an existing origination phone number in your account. Once released, a phone number is no longer available for sending messages.

If the origination phone number has deletion protection enabled or is associated with a pool, an error is returned.

## Request Syntax
<a name="API_ReleasePhoneNumber_RequestSyntax"></a>

```
{
   "PhoneNumberId": "{{string}}"
}
```

## Request Parameters
<a name="API_ReleasePhoneNumber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PhoneNumberId](#API_ReleasePhoneNumber_RequestSyntax) **   <a name="pinpoint-ReleasePhoneNumber-request-PhoneNumberId"></a>
The PhoneNumberId or PhoneNumberArn of the phone number to release. You can use [DescribePhoneNumbers](API_DescribePhoneNumbers.md) to get the values for PhoneNumberId and PhoneNumberArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_ReleasePhoneNumber_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "IsoCountryCode": "string",
   "MessageType": "string",
   "MonthlyLeasingPrice": "string",
   "NumberCapabilities": [ "string" ],
   "NumberType": "string",
   "OptOutListName": "string",
   "PhoneNumber": "string",
   "PhoneNumberArn": "string",
   "PhoneNumberId": "string",
   "RegistrationId": "string",
   "SelfManagedOptOutsEnabled": boolean,
   "Status": "string",
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean
}
```

## Response Elements
<a name="API_ReleasePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-CreatedTimestamp"></a>
The time when the phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [IsoCountryCode](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [MessageType](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-MessageType"></a>
The message type that was associated with the phone number.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [MonthlyLeasingPrice](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-MonthlyLeasingPrice"></a>
The monthly price of the phone number, in US dollars.
Type: String

 ** [NumberCapabilities](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-NumberCapabilities"></a>
Specifies if the number could be used for text messages, voice, or both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`

 ** [NumberType](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-NumberType"></a>
The type of number that was released.
Type: String
Valid Values: `SHORT_CODE | LONG_CODE | TOLL_FREE | TEN_DLC | SIMULATOR`

 ** [OptOutListName](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-OptOutListName"></a>
The name of the OptOutList that was associated with the phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PhoneNumber](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-PhoneNumber"></a>
The phone number that was released.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [PhoneNumberArn](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-PhoneNumberArn"></a>
The PhoneNumberArn of the phone number that was released.
Type: String

 ** [PhoneNumberId](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-PhoneNumberId"></a>
The PhoneNumberId of the phone number that was released.
Type: String

 ** [RegistrationId](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [Status](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-Status"></a>
The current status of the request.
Type: String
Valid Values: `PENDING | ACTIVE | ASSOCIATING | DISASSOCIATING | DELETED`

 ** [TwoWayChannelArn](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the TwoWayChannel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_ReleasePhoneNumber_ResponseSyntax) **   <a name="pinpoint-ReleasePhoneNumber-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

## Errors
<a name="API_ReleasePhoneNumber_Errors"></a>

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
<a name="API_ReleasePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ReleasePhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
