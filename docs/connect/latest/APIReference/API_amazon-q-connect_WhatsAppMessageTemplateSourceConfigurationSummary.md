---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary.html
---

# WhatsAppMessageTemplateSourceConfigurationSummary
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary"></a>

Configuration information about the external data source.

## Contents
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary_Contents"></a>

 ** businessAccountId **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-businessAccountId"></a>
The ID of the End User Messaging WhatsApp Business Account to associate with this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*(^waba-[0-9a-zA-Z]+$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** templateId **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-templateId"></a>
The ID of WhatsApp template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** components **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-components"></a>
The list of component mapping from WhatsApp template parameters to Message Template attributes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

 ** language **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-language"></a>
The language of the WhatsApp template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Required: No

 ** name **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-name"></a>
The name of the WhatsApp template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** status **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-status"></a>
The status of the message template.
Type: String
Valid Values: `VALID | INVALID | REJECTED`
Required: No

 ** statusReason **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary-statusReason"></a>
The status reason of the message template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
