---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html
---

# SendTemplatedEmail
<a name="API_SendTemplatedEmail"></a>

Composes an email message using an email template and immediately queues it for sending.

To send email using this operation, your call must meet the following requirements:
+ The call must refer to an existing email template. You can create email templates using the [CreateTemplate](API_CreateTemplate.md) operation.
+ The message must be sent from a verified email address or domain.
+ If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) in the *Amazon SES Developer Guide.*
+ The maximum message size is 10 MB.
+ Calls to the `SendTemplatedEmail` operation may only include one `Destination` parameter. A destination is a set of recipients that receives the same version of the email. The `Destination` parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.
+ The `Destination` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain*), the entire message is rejected, even if the message contains other recipients that are valid.

**Important**
If your call to the `SendTemplatedEmail` operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can't render the email because the template contains errors, it doesn't send the email. Additionally, because it already accepted the message, Amazon SES doesn't return a message stating that it was unable to send the email.
For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see [Sending Personalized Email Using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html) in the *Amazon Simple Email Service Developer Guide*.

## Request Parameters
<a name="API_SendTemplatedEmail_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set to use when you send an email using `SendTemplatedEmail`.
Type: String
Required: No

 ** Destination **
The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.
Type: [Destination](API_Destination.md) object
Required: Yes

 **ReplyToAddresses.member.N**
The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.
Type: Array of strings
Required: No

 ** ReturnPath **
The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipient's ISP; this message is forwarded to the email address specified by the `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.
Type: String
Required: No

 ** ReturnPathArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `ReturnPath` parameter.
For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com`) attaches a policy to it that authorizes you to use `feedback@example.com`, then you would specify the `ReturnPathArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com`, and the `ReturnPath` to be `feedback@example.com`.
For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).
Type: String
Required: No

 ** Source **
The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html).
If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the `SourceArn` parameter. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).
Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531). for this reason, The email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html). For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492).
Type: String
Required: Yes

 ** SourceArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the `Source` parameter.
For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com`) attaches a policy to it that authorizes you to send from `user@example.com`, then you would specify the `SourceArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com`, and the `Source` to be `user@example.com`.
For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).
Type: String
Required: No

 **Tags.member.N**
A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendTemplatedEmail`. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
Type: Array of [MessageTag](API_MessageTag.md) objects
Required: No

 ** Template **
The template to use when sending this email.
Type: String
Required: Yes

 ** TemplateArn **
The ARN of the template to use when sending this email.
Type: String
Required: No

 ** TemplateData **
A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
Type: String
Length Constraints: Maximum length of 262144.
Required: Yes

## Response Elements
<a name="API_SendTemplatedEmail_ResponseElements"></a>

The following element is returned by the service.

 ** MessageId **
The unique message identifier returned from the `SendTemplatedEmail` action.
Type: String

## Errors
<a name="API_SendTemplatedEmail_Errors"></a>

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

 ** TemplateDoesNotExist **
Indicates that the Template object you specified does not exist in your Amazon SES account.
HTTP Status Code: 400

## See Also
<a name="API_SendTemplatedEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SendTemplatedEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SendTemplatedEmail)
