---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccountIdMetaData.html
---

# LinkedWhatsAppBusinessAccountIdMetaData
<a name="API_LinkedWhatsAppBusinessAccountIdMetaData"></a>

Contains your WhatsApp registration status and details of any unregistered WhatsApp phone number.

## Contents
<a name="API_LinkedWhatsAppBusinessAccountIdMetaData_Contents"></a>

 ** accountName **   <a name="Social-Type-LinkedWhatsAppBusinessAccountIdMetaData-accountName"></a>
The name of your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** registrationStatus **   <a name="Social-Type-LinkedWhatsAppBusinessAccountIdMetaData-registrationStatus"></a>
The registration status of the linked WhatsApp Business Account.
Type: String
Valid Values: `COMPLETE | INCOMPLETE`
Required: No

 ** unregisteredWhatsAppPhoneNumbers **   <a name="Social-Type-LinkedWhatsAppBusinessAccountIdMetaData-unregisteredWhatsAppPhoneNumbers"></a>
The details for unregistered WhatsApp phone numbers.
Type: Array of [WhatsAppPhoneNumberDetail](API_WhatsAppPhoneNumberDetail.md) objects
Required: No

 ** wabaId **   <a name="Social-Type-LinkedWhatsAppBusinessAccountIdMetaData-wabaId"></a>
The Amazon Resource Name (ARN) of the WhatsApp Business Account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: No

## See Also
<a name="API_LinkedWhatsAppBusinessAccountIdMetaData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountIdMetaData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountIdMetaData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountIdMetaData)
