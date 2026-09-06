---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendNotifyTextMessage.html
---

# SendNotifyTextMessage
<a name="API_SendNotifyTextMessage"></a>

Sends a templated text message through a notify configuration to a recipient's phone number.

## Request Syntax
<a name="API_SendNotifyTextMessage_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationPhoneNumber": "{{string}}",
   "DryRun": {{boolean}},
   "MessageFeedbackEnabled": {{boolean}},
   "NotifyConfigurationId": "{{string}}",
   "TemplateId": "{{string}}",
   "TemplateVariables": {
      "{{string}}" : "{{string}}"
   },
   "TimeToLive": {{number}}
}
```

## Request Parameters
<a name="API_SendNotifyTextMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationPhoneNumber](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [DryRun](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-DryRun"></a>
When set to true, the message is checked and validated, but isn't sent to the end recipient.
Type: Boolean
Required: No

 ** [MessageFeedbackEnabled](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-MessageFeedbackEnabled"></a>
Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using [PutMessageFeedback](API_PutMessageFeedback.md).
Type: Boolean
Required: No

 ** [NotifyConfigurationId](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-NotifyConfigurationId"></a>
The unique identifier of the notify configuration to use for sending the message. This can be either the NotifyConfigurationId or NotifyConfigurationArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [TemplateId](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-TemplateId"></a>
The unique identifier of the template to use for the message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`
Required: No

 ** [TemplateVariables](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-TemplateVariables"></a>
A map of template variable names and their values. All variable values are passed as strings regardless of the declared variable type. For example, pass `INTEGER` values as `"42"` and `BOOLEAN` values as `"true"` or `"false"`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[A-Za-z0-9_]+`
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [TimeToLive](#API_SendNotifyTextMessage_RequestSyntax) **   <a name="pinpoint-SendNotifyTextMessage-request-TimeToLive"></a>
How long the text message is valid for, in seconds. By default this is 72 hours.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 259200.
Required: No

## Response Syntax
<a name="API_SendNotifyTextMessage_ResponseSyntax"></a>

```
{
   "MessageId": "string",
   "ResolvedMessageBody": "string",
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_SendNotifyTextMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendNotifyTextMessage_ResponseSyntax) **   <a name="pinpoint-SendNotifyTextMessage-response-MessageId"></a>
The unique identifier for the message.
Type: String

 ** [ResolvedMessageBody](#API_SendNotifyTextMessage_ResponseSyntax) **   <a name="pinpoint-SendNotifyTextMessage-response-ResolvedMessageBody"></a>
The message body after template variable substitution has been applied.
Type: String

 ** [TemplateId](#API_SendNotifyTextMessage_ResponseSyntax) **   <a name="pinpoint-SendNotifyTextMessage-response-TemplateId"></a>
The unique identifier of the template used for the message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`

## Errors
<a name="API_SendNotifyTextMessage_Errors"></a>

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
<a name="API_SendNotifyTextMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendNotifyTextMessage)
