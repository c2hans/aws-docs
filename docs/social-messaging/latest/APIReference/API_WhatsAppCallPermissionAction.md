---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppCallPermissionAction.html
---

# WhatsAppCallPermissionAction
<a name="API_WhatsAppCallPermissionAction"></a>

Describes a single calling action the business can take with an end user, including whether the action is currently allowed and any limits that apply to it. Returned as an item in the actions list from `GetWhatsAppCallPermission`.

## Contents
<a name="API_WhatsAppCallPermissionAction_Contents"></a>

 ** actionName **   <a name="Social-Type-WhatsAppCallPermissionAction-actionName"></a>
The name of the calling action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** canPerformAction **   <a name="Social-Type-WhatsAppCallPermissionAction-canPerformAction"></a>
Specifies whether the business can currently perform the action.
Type: Boolean
Required: Yes

 ** limits **   <a name="Social-Type-WhatsAppCallPermissionAction-limits"></a>
The time-bound limits that apply to the action.
Type: Array of [WhatsAppCallPermissionLimit](API_WhatsAppCallPermissionLimit.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_WhatsAppCallPermissionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppCallPermissionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppCallPermissionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppCallPermissionAction)
