---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html
---

# SendBounce
<a name="API_SendBounce"></a>

Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this operation on an email up to 24 hours after you receive it.

**Note**
You cannot use this operation to send generic bounces for mail that was not received by Amazon SES.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_SendBounce_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **BouncedRecipientInfoList.member.N**
A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one `BouncedRecipientInfo` in the list.
Type: Array of [BouncedRecipientInfo](API_BouncedRecipientInfo.md) objects
Required: Yes

 ** BounceSender **
The address to use in the "From" header of the bounce message. This must be an identity that you have verified with Amazon SES.
Type: String
Required: Yes

 ** BounceSenderArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the "From" header of the bounce. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).
Type: String
Required: No

 ** Explanation **
Human-readable text for the bounce message to explain the failure. If not specified, the text is auto-generated based on the bounced recipient information.
Type: String
Required: No

 ** MessageDsn **
Message-related DSN fields. If not specified, Amazon SES chooses the values.
Type: [MessageDsn](API_MessageDsn.md) object
Required: No

 ** OriginalMessageId **
The message ID of the message to be bounced.
Type: String
Required: Yes

## Response Elements
<a name="API_SendBounce_ResponseElements"></a>

The following element is returned by the service.

 ** MessageId **
The message ID of the bounce message.
Type: String

## Errors
<a name="API_SendBounce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** MessageRejected **
Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.
HTTP Status Code: 400

## See Also
<a name="API_SendBounce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SendBounce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SendBounce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SendBounce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SendBounce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SendBounce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SendBounce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SendBounce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SendBounce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SendBounce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SendBounce)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
