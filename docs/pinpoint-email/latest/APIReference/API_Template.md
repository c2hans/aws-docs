---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Template.html
---

# Template
<a name="API_Template"></a>

An object that defines the email template to use for an email message, and the values to use for any message variables in that template. An *email template* is a type of message template that contains content that you want to define, save, and reuse in email messages that you send for any of your Amazon Pinpoint projects.

## Contents
<a name="API_Template_Contents"></a>

 ** TemplateArn **   <a name="pinpoint-Type-Template-TemplateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Required: No

 ** TemplateData **   <a name="pinpoint-Type-Template-TemplateData"></a>
An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

## See Also
<a name="API_Template_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/Template)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/Template)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/Template)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
