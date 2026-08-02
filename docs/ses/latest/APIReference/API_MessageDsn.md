---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_MessageDsn.html
---

# MessageDsn
<a name="API_MessageDsn"></a>

Message-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html).

## Contents
<a name="API_MessageDsn_Contents"></a>

 ** ReportingMta **
The reporting MTA that attempted to deliver the message, formatted as specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-type; mta-name`). The default value is `dns; inbound-smtp.[region].amazonaws.com`.
Type: String
Required: Yes

 ** ArrivalDate **
When the message was received by the reporting mail transfer agent (MTA), in [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.
Type: Timestamp
Required: No

 ** ExtensionFields.member.N **
Additional X-headers to include in the DSN.
Type: Array of [ExtensionField](API_ExtensionField.md) objects
Required: No

## See Also
<a name="API_MessageDsn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/MessageDsn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/MessageDsn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/MessageDsn)
