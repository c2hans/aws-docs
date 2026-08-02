---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_RecipientDsnFields.html
---

# RecipientDsnFields
<a name="API_RecipientDsnFields"></a>

Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html).

## Contents
<a name="API_RecipientDsnFields_Contents"></a>

 ** Action **
The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by [RFC 3464](https://tools.ietf.org/html/rfc3464).
Type: String
Valid Values: `failed | delayed | delivered | relayed | expanded`
Required: Yes

 ** Status **
The status code that indicates what went wrong. This is required by [RFC 3464](https://tools.ietf.org/html/rfc3464).
Type: String
Required: Yes

 ** DiagnosticCode **
An extended explanation of what went wrong; this is usually an SMTP response. See [RFC 3463](https://tools.ietf.org/html/rfc3463) for the correct formatting of this parameter.
Type: String
Required: No

 ** ExtensionFields.member.N **
Additional X-headers to include in the DSN.
Type: Array of [ExtensionField](API_ExtensionField.md) objects
Required: No

 ** FinalRecipient **
The email address that the message was ultimately delivered to. This corresponds to the `Final-Recipient` in the DSN. If not specified, `FinalRecipient` is set to the `Recipient` specified in the `BouncedRecipientInfo` structure. Either `FinalRecipient` or the recipient in `BouncedRecipientInfo` must be a recipient of the original bounced message.
Do not prepend the `FinalRecipient` email address with `rfc 822;`, as described in [RFC 3798](https://tools.ietf.org/html/rfc3798).
Type: String
Required: No

 ** LastAttemptDate **
The time the final delivery attempt was made, in [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.
Type: Timestamp
Required: No

 ** RemoteMta **
The MTA to which the remote MTA attempted to deliver the message, formatted as specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-type; mta-name`). This parameter typically applies only to propagating synchronous bounces.
Type: String
Required: No

## See Also
<a name="API_RecipientDsnFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/RecipientDsnFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/RecipientDsnFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/RecipientDsnFields)
