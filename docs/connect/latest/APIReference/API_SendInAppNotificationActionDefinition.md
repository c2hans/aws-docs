---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SendInAppNotificationActionDefinition.html
---

# SendInAppNotificationActionDefinition
<a name="API_SendInAppNotificationActionDefinition"></a>

Information about the send in-app notification action.

## Contents
<a name="API_SendInAppNotificationActionDefinition_Contents"></a>

 ** Content **   <a name="connect-Type-SendInAppNotificationActionDefinition-Content"></a>
Notification content. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
Type: String to string map
Valid Keys: `en_US | de_DE | es_ES | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | zh_CN | zh_TW`
Value Length Constraints: Minimum length of 0. Maximum length of 3000.
Required: Yes

 ** Recipient **   <a name="connect-Type-SendInAppNotificationActionDefinition-Recipient"></a>
Notification recipient.
Type: [NotificationRecipientType](API_NotificationRecipientType.md) object
Required: Yes

 ** Exclusion **   <a name="connect-Type-SendInAppNotificationActionDefinition-Exclusion"></a>
Recipients to exclude from notification.
Type: [NotificationRecipientType](API_NotificationRecipientType.md) object
Required: No

 ** Priority **   <a name="connect-Type-SendInAppNotificationActionDefinition-Priority"></a>
Notification priority.
Type: String
Valid Values: `HIGH | LOW`
Required: No

## See Also
<a name="API_SendInAppNotificationActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SendInAppNotificationActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SendInAppNotificationActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SendInAppNotificationActionDefinition)
