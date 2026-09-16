---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendEmail.html
---

# SendEmail
<a name="API_SendEmail"></a>

Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:
+  **Simple** – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you.
+  **Raw** – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.

## Request Syntax
<a name="API_SendEmail_RequestSyntax"></a>

```
POST /v1/email/outbound-emails HTTP/1.1
Content-type: application/json

{
   "ConfigurationSetName": "{{string}}",
   "Content": {
      "Raw": {
         "Data": {{blob}}
      },
      "Simple": {
         "Body": {
            "Html": {
               "Charset": "{{string}}",
               "Data": "{{string}}"
            },
            "Text": {
               "Charset": "{{string}}",
               "Data": "{{string}}"
            }
         },
         "Subject": {
            "Charset": "{{string}}",
            "Data": "{{string}}"
         }
      },
      "Template": {
         "TemplateArn": "{{string}}",
         "TemplateData": "{{string}}"
      }
   },
   "Destination": {
      "BccAddresses": [ "{{string}}" ],
      "CcAddresses": [ "{{string}}" ],
      "ToAddresses": [ "{{string}}" ]
   },
   "EmailTags": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "FeedbackForwardingEmailAddress": "{{string}}",
   "FromEmailAddress": "{{string}}",
   "ReplyToAddresses": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_SendEmail_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendEmail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-ConfigurationSetName"></a>
The name of the configuration set that you want to use when sending the email.
Type: String
Required: No

 ** [Content](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-Content"></a>
An object that contains the body of the message. You can send either a Simple message or a Raw message.
Type: [EmailContent](API_EmailContent.md) object
Required: Yes

 ** [Destination](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-Destination"></a>
An object that contains the recipients of the email message.
Type: [Destination](API_Destination.md) object
Required: Yes

 ** [EmailTags](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-EmailTags"></a>
A list of tags, in the form of name/value pairs, to apply to an email that you send using the `SendEmail` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
Type: Array of [MessageTag](API_MessageTag.md) objects
Required: No

 ** [FeedbackForwardingEmailAddress](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-FeedbackForwardingEmailAddress"></a>
The address that Amazon Pinpoint should send bounce and complaint notifications to.
Type: String
Required: No

 ** [FromEmailAddress](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-FromEmailAddress"></a>
The email address that you want to use as the "From" address for the email. The address that you specify has to be verified.
Type: String
Required: No

 ** [ReplyToAddresses](#API_SendEmail_RequestSyntax) **   <a name="pinpoint-SendEmail-request-ReplyToAddresses"></a>
The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_SendEmail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendEmail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendEmail_ResponseSyntax) **   <a name="pinpoint-SendEmail-response-MessageId"></a>
A unique identifier for the message that is generated when Amazon Pinpoint accepts the message.
It is possible for Amazon Pinpoint to accept a message without sending it. This can happen when the message you're trying to send has an attachment that doesn't pass a virus check, or when you send a templated email that contains invalid personalization content, for example.
Type: String

## Errors
<a name="API_SendEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountSuspendedException **
The message can't be sent because the account's ability to send email has been permanently restricted.
HTTP Status Code: 400

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** LimitExceededException **
There are too many instances of the specified resource type.
HTTP Status Code: 400

 ** MailFromDomainNotVerifiedException **
The message can't be sent because the sending domain isn't verified.
HTTP Status Code: 400

 ** MessageRejected **
The message can't be sent because it contains invalid content.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** SendingPausedException **
The message can't be sent because the account's ability to send email is currently paused.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_SendEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/SendEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/SendEmail)
