---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppCallSettings.html
---

# WhatsAppCallSettings
<a name="API_WhatsAppCallSettings"></a>

The calling configuration for a WhatsApp business phone number.

## Contents
<a name="API_WhatsAppCallSettings_Contents"></a>

 ** callEnabled **   <a name="Social-Type-WhatsAppCallSettings-callEnabled"></a>
Specifies whether calling is enabled for the phone number.
Type: Boolean
Required: Yes

 ** callbackPermissionStatus **   <a name="Social-Type-WhatsAppCallSettings-callbackPermissionStatus"></a>
The callback permission status for the phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** callHours **   <a name="Social-Type-WhatsAppCallSettings-callHours"></a>
The hours during which the business accepts calls on the phone number.
Type: [WhatsAppCallHours](API_WhatsAppCallHours.md) object
Required: No

 ** callIconVisibility **   <a name="Social-Type-WhatsAppCallSettings-callIconVisibility"></a>
The visibility setting for the call icon shown to end users in WhatsApp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_WhatsAppCallSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppCallSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppCallSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppCallSettings)
