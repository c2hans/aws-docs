---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SendNotificationActionDefinition.html
---

# SendNotificationActionDefinition
<a name="API_SendNotificationActionDefinition"></a>

Information about the send notification action.

## Contents
<a name="API_SendNotificationActionDefinition_Contents"></a>

 ** Content **   <a name="connect-Type-SendNotificationActionDefinition-Content"></a>
Notification content. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ContentType **   <a name="connect-Type-SendNotificationActionDefinition-ContentType"></a>
Content type format.
Type: String
Valid Values: `PLAIN_TEXT`
Required: Yes

 ** DeliveryMethod **   <a name="connect-Type-SendNotificationActionDefinition-DeliveryMethod"></a>
Notification delivery method.
Type: String
Valid Values: `EMAIL`
Required: Yes

 ** Recipient **   <a name="connect-Type-SendNotificationActionDefinition-Recipient"></a>
Notification recipient.
Type: [NotificationRecipientType](API_NotificationRecipientType.md) object
Required: Yes

 ** Exclusion **   <a name="connect-Type-SendNotificationActionDefinition-Exclusion"></a>
Recipients to exclude from notification.
Type: [NotificationRecipientType](API_NotificationRecipientType.md) object
Required: No

 ** Subject **   <a name="connect-Type-SendNotificationActionDefinition-Subject"></a>
The subject of the email if the delivery method is `EMAIL`. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_SendNotificationActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SendNotificationActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SendNotificationActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SendNotificationActionDefinition)
