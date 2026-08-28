---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html
---

# Template
<a name="API_Template"></a>

An object that defines the email template to use for an email message, and the values to use for any message variables in that template. An *email template* is a type of message template that contains content that you want to reuse in email messages that you send. You can specifiy the email template by providing the name or ARN of an *email template* previously saved in your Amazon SES account or by providing the full template content.

## Contents
<a name="API_Template_Contents"></a>

 ** Attachments **   <a name="SES-Type-Template-Attachments"></a>
 The List of attachments to include in your email. All recipients will receive the same attachments.
Type: Array of [Attachment](API_Attachment.md) objects
Required: No

 ** Headers **   <a name="SES-Type-Template-Headers"></a>
The list of message headers that will be added to the email message.
Type: Array of [MessageHeader](API_MessageHeader.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** TemplateArn **   <a name="SES-Type-Template-TemplateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TemplateContent **   <a name="SES-Type-Template-TemplateContent"></a>
The content of the template.
Amazon SES supports only simple substitions when you send email using the `SendEmail` or `SendBulkEmail` operations and you provide the full template content in the request.
Type: [EmailTemplateContent](API_EmailTemplateContent.md) object
Required: No

 ** TemplateData **   <a name="SES-Type-Template-TemplateData"></a>
An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** TemplateName **   <a name="SES-Type-Template-TemplateName"></a>
The name of the template. You will refer to this name when you send email using the `SendEmail` or `SendBulkEmail` operations.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Template_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Template)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Template)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Template)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
