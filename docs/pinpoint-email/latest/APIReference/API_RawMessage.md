---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_RawMessage.html
---

# RawMessage
<a name="API_RawMessage"></a>

The raw email message.

## Contents
<a name="API_RawMessage_Contents"></a>

 ** Data **   <a name="pinpoint-Type-RawMessage-Data"></a>
The raw email message. The message has to meet the following criteria:
+ The message has to contain a header and a body, separated by one blank line.
+ All of the required header fields must be present in the message.
+ Each part of a multipart MIME message must be formatted properly.
+ Attachments must be in a file format that Amazon Pinpoint supports.
+ The entire message must be Base64 encoded.
+ If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
+ The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321).
Type: Base64-encoded binary data object
Required: Yes

## See Also
<a name="API_RawMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/RawMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/RawMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/RawMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
