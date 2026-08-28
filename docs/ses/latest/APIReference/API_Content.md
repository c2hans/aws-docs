---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_Content.html
---

# Content
<a name="API_Content"></a>

Represents textual data, plus an optional character set specification.

By default, the text must be 7-bit ASCII, due to the constraints of the SMTP protocol. If the text must contain any other characters, then you must also specify a character set. Examples include UTF-8, ISO-8859-1, and Shift\_JIS.

## Contents
<a name="API_Content_Contents"></a>

 ** Data **
The textual data of the content.
Type: String
Required: Yes

 ** Charset **
The character set of the content.
Type: String
Required: No

## See Also
<a name="API_Content_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/Content)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/Content)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/Content)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
