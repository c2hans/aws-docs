---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_WhatsAppParameters.html
---

# WhatsAppParameters
<a name="API_WhatsAppParameters"></a>

The delivery parameters for the WhatsApp channel.

## Contents
<a name="API_WhatsAppParameters_Contents"></a>

 ** languageCode **   <a name="endusermessaging-Type-WhatsAppParameters-languageCode"></a>
The BCP 47 language code used to render the template. This value is required for the WhatsApp channel.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Pattern: `\S+`
Required: No

 ** whatsAppTemplateName **   <a name="endusermessaging-Type-WhatsAppParameters-whatsAppTemplateName"></a>
The name of the Meta-approved WhatsApp authentication template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\S+`
Required: No

## See Also
<a name="API_WhatsAppParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/WhatsAppParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/WhatsAppParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/WhatsAppParameters)
