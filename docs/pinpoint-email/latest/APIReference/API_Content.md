---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Content.html
---

# Content
<a name="API_Content"></a>

An object that represents the content of the email, and optionally a character set specification.

## Contents
<a name="API_Content_Contents"></a>

 ** Data **   <a name="pinpoint-Type-Content-Data"></a>
The content of the message itself.
Type: String
Required: Yes

 ** Charset **   <a name="pinpoint-Type-Content-Charset"></a>
The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8`, `ISO-8859-1`, or `Shift_JIS`.
Type: String
Required: No

## See Also
<a name="API_Content_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/Content)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/Content)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/Content)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
