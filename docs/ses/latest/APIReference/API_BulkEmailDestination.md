---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_BulkEmailDestination.html
---

# BulkEmailDestination
<a name="API_BulkEmailDestination"></a>

An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.

## Contents
<a name="API_BulkEmailDestination_Contents"></a>

 ** Destination **
Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html). For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492).
Type: [Destination](API_Destination.md) object
Required: Yes

 ** ReplacementTags.member.N **
A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendBulkTemplatedEmail`. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
Type: Array of [MessageTag](API_MessageTag.md) objects
Required: No

 ** ReplacementTemplateData **
A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

## See Also
<a name="API_BulkEmailDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/BulkEmailDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/BulkEmailDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/BulkEmailDestination)
