---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.html
---

# SendTextMessage
<a name="API_SendTextMessage"></a>

Creates a new text message and sends it to a recipient's phone number. SendTextMessage only sends an SMS message to one recipient each time it is invoked.

SMS throughput limits are measured in Message Parts per Second (MPS). Your MPS limit depends on the destination country of your messages, as well as the type of phone number (origination number) that you use to send the message. For more information about MPS, see [Message Parts per Second (MPS) limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html) in the * AWS End User Messaging SMS User Guide*.

## Request Syntax
<a name="API_SendTextMessage_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationCountryParameters": {
      "{{string}}" : "{{string}}"
   },
   "DestinationPhoneNumber": "{{string}}",
   "DryRun": {{boolean}},
   "Keyword": "{{string}}",
   "MaxPrice": "{{string}}",
   "MessageBody": "{{string}}",
   "MessageFeedbackEnabled": {{boolean}},
   "MessageType": "{{string}}",
   "OriginationIdentity": "{{string}}",
   "ProtectConfigurationId": "{{string}}",
   "TimeToLive": {{number}}
}
```

## Request Parameters
<a name="API_SendTextMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationCountryParameters](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-DestinationCountryParameters"></a>
This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see [Special requirements for sending SMS messages to recipients in India](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html).
+  `IN_ENTITY_ID` The entity ID or Principal Entity (PE) ID that you received after completing the sender ID registration process.
+  `IN_TEMPLATE_ID` The template ID that you received after completing the sender ID registration process.
**Important**
Make sure that the Template ID that you specify matches your message template exactly. If your message doesn't match the template that you provided during the registration process, the mobile carriers might reject your message.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `IN_TEMPLATE_ID | IN_ENTITY_ID`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Value Pattern: `\S+`
Required: No

 ** [DestinationPhoneNumber](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [DryRun](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-DryRun"></a>
When set to true, the message is checked and validated, but isn't sent to the end recipient. You are not charged for using `DryRun`.
The Message Parts per Second (MPS) limit when using `DryRun` is five. If your origination identity has a lower MPS limit then the lower MPS limit is used. For more information about MPS limits, see [Message Parts per Second (MPS) limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html) in the * AWS End User Messaging SMS User Guide*..
Type: Boolean
Required: No

 ** [Keyword](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-Keyword"></a>
When you register a short code in the US, you must specify a program name. If you don’t have a US short code, omit this attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`
Required: No

 ** [MaxPrice](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-MaxPrice"></a>
The maximum amount that you want to spend, in US dollars, per each text message. If the calculated amount to send the text message is greater than `MaxPrice`, the message is not sent and an error is returned.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 8.
Pattern: `[0-9]{0,2}\.[0-9]{1,5}`
Required: No

 ** [MessageBody](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-MessageBody"></a>
The body of the text message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** [MessageFeedbackEnabled](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-MessageFeedbackEnabled"></a>
Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using [PutMessageFeedback](API_PutMessageFeedback.md).
Type: Boolean
Required: No

 ** [MessageType](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-MessageType"></a>
The type of message. Valid values are for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: No

 ** [OriginationIdentity](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-OriginationIdentity"></a>
The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, RcsAgentId, RcsAgentArn, SenderId, SenderIdArn, PoolId, or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: No

 ** [ProtectConfigurationId](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [TimeToLive](#API_SendTextMessage_RequestSyntax) **   <a name="pinpoint-SendTextMessage-request-TimeToLive"></a>
How long the text message is valid for, in seconds. By default this is 72 hours. If the messages isn't handed off before the TTL expires we stop attempting to hand off the message and return `TTL_EXPIRED` event.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 259200.
Required: No

## Response Syntax
<a name="API_SendTextMessage_ResponseSyntax"></a>

```
{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendTextMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendTextMessage_ResponseSyntax) **   <a name="pinpoint-SendTextMessage-response-MessageId"></a>
The unique identifier for the message.
Type: String

## Errors
<a name="API_SendTextMessage_Errors"></a>

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
<a name="API_SendTextMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
