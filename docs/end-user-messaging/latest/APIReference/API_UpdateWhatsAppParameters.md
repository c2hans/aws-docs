---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateWhatsAppParameters.html
---

# UpdateWhatsAppParameters
<a name="API_UpdateWhatsAppParameters"></a>

The updated delivery parameters for the WhatsApp channel. Absent members preserve the current value, and the empty sentinel on a member clears it.

## Contents
<a name="API_UpdateWhatsAppParameters_Contents"></a>

 ** languageCode **   <a name="endusermessaging-Type-UpdateWhatsAppParameters-languageCode"></a>
The updated BCP 47 language code. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 35.
Pattern: `(\S{2,35})?`
Required: No

 ** whatsAppTemplateName **   <a name="endusermessaging-Type-UpdateWhatsAppParameters-whatsAppTemplateName"></a>
The updated name of the Meta-approved WhatsApp authentication template. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `\S*`
Required: No

## See Also
<a name="API_UpdateWhatsAppParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateWhatsAppParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateWhatsAppParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateWhatsAppParameters)
