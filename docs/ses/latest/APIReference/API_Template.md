---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html
---

# Template
<a name="API_Template"></a>

The content of the email, composed of a subject line and either an HTML part or a text-only part.

## Contents
<a name="API_Template_Contents"></a>

 ** TemplateName **
The name of the template. You use this name when you send email using the `SendTemplatedEmail` or `SendBulkTemplatedEmail` operations.
Type: String
Required: Yes

 ** HtmlPart **
The HTML body of the email.
Type: String
Required: No

 ** SubjectPart **
The subject line of the email.
Type: String
Required: No

 ** TextPart **
The email body that is visible to recipients whose email clients do not display HTML content.
Type: String
Required: No

## See Also
<a name="API_Template_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/Template)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/Template)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/Template)
