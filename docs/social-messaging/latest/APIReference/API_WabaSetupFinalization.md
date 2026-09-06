---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WabaSetupFinalization.html
---

# WabaSetupFinalization
<a name="API_WabaSetupFinalization"></a>

The registration details for a linked WhatsApp Business Account.

## Contents
<a name="API_WabaSetupFinalization_Contents"></a>

 ** eventDestinations **   <a name="Social-Type-WabaSetupFinalization-eventDestinations"></a>
The event destinations for the linked WhatsApp Business Account.
Type: Array of [WhatsAppBusinessAccountEventDestination](API_WhatsAppBusinessAccountEventDestination.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** id **   <a name="Social-Type-WabaSetupFinalization-id"></a>
The ID of the linked WhatsApp Business Account, formatted as `waba-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** tags **   <a name="Social-Type-WabaSetupFinalization-tags"></a>
An array of key and value pair tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_WabaSetupFinalization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WabaSetupFinalization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WabaSetupFinalization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WabaSetupFinalization)
