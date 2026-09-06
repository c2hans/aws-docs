---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_WhatsAppMessageTemplateSourceConfiguration.html
---

# WhatsAppMessageTemplateSourceConfiguration
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration"></a>

Configuration information about the external data source.

## Contents
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration_Contents"></a>

 ** businessAccountId **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration-businessAccountId"></a>
The ID of the End User Messaging WhatsApp Business Account to associate with this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*(^waba-[0-9a-zA-Z]+$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** templateId **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration-templateId"></a>
The WhatsApp template ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** components **   <a name="connect-Type-amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration-components"></a>
The list of component mapping from WhatsApp template parameters to Message Template attributes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

## See Also
<a name="API_amazon-q-connect_WhatsAppMessageTemplateSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/WhatsAppMessageTemplateSourceConfiguration)
