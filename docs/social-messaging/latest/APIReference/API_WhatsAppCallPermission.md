---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppCallPermission.html
---

# WhatsAppCallPermission
<a name="API_WhatsAppCallPermission"></a>

The current calling permission state for a business phone number and a specific WhatsApp end user.

## Contents
<a name="API_WhatsAppCallPermission_Contents"></a>

 ** status **   <a name="Social-Type-WhatsAppCallPermission-status"></a>
The permission status for the end user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** expirationTime **   <a name="Social-Type-WhatsAppCallPermission-expirationTime"></a>
The time when a temporary permission expires. This value is absent for permanent permissions and when there is no permission.
Type: Timestamp
Required: No

## See Also
<a name="API_WhatsAppCallPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppCallPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppCallPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppCallPermission)
