---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

**Note**
Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html). For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492).

## Contents
<a name="API_Destination_Contents"></a>

 ** BccAddresses.member.N **
The recipients to place on the BCC: line of the message.
Type: Array of strings
Required: No

 ** CcAddresses.member.N **
The recipients to place on the CC: line of the message.
Type: Array of strings
Required: No

 ** ToAddresses.member.N **
The recipients to place on the To: line of the message.
Type: Array of strings
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/Destination)
