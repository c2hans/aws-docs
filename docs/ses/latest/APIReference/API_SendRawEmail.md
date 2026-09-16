---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html
---

# SendRawEmail
<a name="API_SendRawEmail"></a>

Composes an email message and immediately queues it for sending.

This operation is more flexible than the `SendEmail` operation. When you use the `SendRawEmail` operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you need to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments.

The `SendRawEmail` operation has the following requirements:
+ You can only send email from [verified email addresses or domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html). If you try to send email from an address that isn't verified, the operation results in an "Email address not verified" error.
+ If your account is still in the [Amazon SES sandbox](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html), you can only send email to other verified addresses in your account, or to addresses that are associated with the [Amazon SES mailbox simulator](https://docs.aws.amazon.com/ses/latest/dg/send-an-email-from-console.html).
+ The maximum message size, including attachments, is 10 MB.
+ Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.
+ If you send a single message to more than one recipient address, and one of the recipient addresses isn't in a valid format (that is, it's not in the format *UserName@[SubDomain.]Domain.TopLevelDomain*), Amazon SES rejects the entire message, even if the other addresses are valid.
+ Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.
+ Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn't preserved. For this reason, we highly recommend that you encode all content that isn't 7-bit ASCII. For more information, see [MIME Encoding](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html#send-email-mime-encoding) in the *Amazon SES Developer Guide*.

Additionally, keep the following considerations in mind when using the `SendRawEmail` operation:
+ Although you can customize the message headers when using the `SendRawEmail` operation, Amazon SES automatically applies its own `Message-ID` and `Date` headers; if you passed these headers when creating the message, they are overwritten by the values that Amazon SES provides.
+ If you are using sending authorization to send on behalf of another user, `SendRawEmail` enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters `SourceArn`, `FromArn`, and/or `ReturnPathArn`, or you can include the following X-headers in the header of your raw email:
  +  `X-SES-SOURCE-ARN`
  +  `X-SES-FROM-ARN`
  +  `X-SES-RETURN-PATH-ARN`
**Important**
Don't include these X-headers in the DKIM signature. Amazon SES removes these before it sends the email.

  If you only specify the `SourceIdentityArn` parameter, Amazon SES sets the From and Return-Path addresses to the same identity that you specified.

  For more information about sending authorization, see the [Using Sending Authorization with Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) in the *Amazon SES Developer Guide.*
+ For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your *sending quota*). For more information about sending quotas in Amazon SES, see [Managing Your Amazon SES Sending Limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html) in the *Amazon SES Developer Guide.*

## Request Parameters
<a name="API_SendRawEmail_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set to use when you send an email using `SendRawEmail`.
Type: String
Required: No

 **Destinations.member.N**
A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.
Type: Array of strings
Required: No

 ** FromArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular "From" address in the header of the raw email.
Instead of using this parameter, you can use the X-header `X-SES-FROM-ARN` in the raw message of the email. If you use both the `FromArn` parameter and the corresponding X-header, Amazon SES uses the value of the `FromArn` parameter.
For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html).
Type: String
Required: No

 ** RawMessage **
The raw email message itself. The message has to meet the following criteria:
+ The message has to contain a header and a body, separated by a blank line.
+ All of the required header fields must be present in the message.
+ Each part of a multipart MIME message must be formatted properly.
+ Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see [Unsupported Attachment Types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the *Amazon SES Developer Guide*.
+ The entire message must be base64-encoded.
+ If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see [Sending Raw Email](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) in the *Amazon SES Developer Guide*.
+ Per [RFC 5321](https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6), the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.
Type: [RawMessage](API_RawMessage.md) object
Required: Yes

 ** ReturnPathArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `ReturnPath` parameter.
For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com`) attaches a policy to it that authorizes you to use `feedback@example.com`, then you would specify the `ReturnPathArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com`, and the `ReturnPath` to be `feedback@example.com`.
Instead of using this parameter, you can use the X-header `X-SES-RETURN-PATH-ARN` in the raw message of the email. If you use both the `ReturnPathArn` parameter and the corresponding X-header, Amazon SES uses the value of the `ReturnPathArn` parameter.
For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html).
Type: String
Required: No

 ** Source **
The identity's email address. If you do not provide a value for this parameter, you must specify a "From" address in the raw text of the message. (You can also specify both.)
Amazon SES does not support the SMTPUTF8 extension, as described in[RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html). For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492).
If you specify the `Source` parameter and have feedback forwarding enabled, then bounces and complaints are sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.
Type: String
Required: No

 ** SourceArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the `Source` parameter.
For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com`) attaches a policy to it that authorizes you to send from `user@example.com`, then you would specify the `SourceArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com`, and the `Source` to be `user@example.com`.
Instead of using this parameter, you can use the X-header `X-SES-SOURCE-ARN` in the raw message of the email. If you use both the `SourceArn` parameter and the corresponding X-header, Amazon SES uses the value of the `SourceArn` parameter.
For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html).
Type: String
Required: No

 **Tags.member.N**
A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendRawEmail`. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
Type: Array of [MessageTag](API_MessageTag.md) objects
Required: No

## Response Elements
<a name="API_SendRawEmail_ResponseElements"></a>

The following element is returned by the service.

 ** MessageId **
The unique message identifier returned from the `SendRawEmail` action.
Type: String

## Errors
<a name="API_SendRawEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountSendingPaused **
Indicates that email sending is disabled for your entire Amazon SES account.
You can enable or disable email sending for your Amazon SES account using [UpdateAccountSendingEnabled](API_UpdateAccountSendingEnabled.md).
HTTP Status Code: 400

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

 ** ConfigurationSetSendingPaused **
Indicates that email sending is disabled for the configuration set.
You can enable or disable email sending for a configuration set using [UpdateConfigurationSetSendingEnabled](API_UpdateConfigurationSetSendingEnabled.md).
 ** ConfigurationSetName **
The name of the configuration set for which email sending is disabled.
HTTP Status Code: 400

 ** MailFromDomainNotVerified **
 Indicates that the message could not be sent because Amazon SES could not read the MX record required to use the specified MAIL FROM domain. For information about editing the custom MAIL FROM domain settings for an identity, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-edit.html).
HTTP Status Code: 400

 ** MessageRejected **
Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.
HTTP Status Code: 400

## See Also
<a name="API_SendRawEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SendRawEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SendRawEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SendRawEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SendRawEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SendRawEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SendRawEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SendRawEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SendRawEmail)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SendRawEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SendRawEmail)
