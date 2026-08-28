---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppPhoneNumberDetail.html
---

# WhatsAppPhoneNumberDetail
<a name="API_WhatsAppPhoneNumberDetail"></a>

The details of your WhatsApp phone number.

## Contents
<a name="API_WhatsAppPhoneNumberDetail_Contents"></a>

 ** arn **   <a name="Social-Type-WhatsAppPhoneNumberDetail-arn"></a>
The ARN of the WhatsApp phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*:phone-number-id/[0-9a-zA-Z]+`
Required: Yes

 ** displayPhoneNumber **   <a name="Social-Type-WhatsAppPhoneNumberDetail-displayPhoneNumber"></a>
The phone number that appears in the recipients display.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** displayPhoneNumberName **   <a name="Social-Type-WhatsAppPhoneNumberDetail-displayPhoneNumberName"></a>
The display name for this phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** metaPhoneNumberId **   <a name="Social-Type-WhatsAppPhoneNumberDetail-metaPhoneNumberId"></a>
The phone number ID from Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** phoneNumber **   <a name="Social-Type-WhatsAppPhoneNumberDetail-phoneNumber"></a>
The phone number for sending WhatsApp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: Yes

 ** phoneNumberId **   <a name="Social-Type-WhatsAppPhoneNumberDetail-phoneNumberId"></a>
The phone number ID. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

 ** qualityRating **   <a name="Social-Type-WhatsAppPhoneNumberDetail-qualityRating"></a>
The quality rating of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: Yes

 ** dataLocalizationRegion **   <a name="Social-Type-WhatsAppPhoneNumberDetail-dataLocalizationRegion"></a>
The geographic region where the WhatsApp phone number's data is stored and processed.
Type: String
Pattern: `[A-Z]{2}`
Required: No

## See Also
<a name="API_WhatsAppPhoneNumberDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppPhoneNumberDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppPhoneNumberDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppPhoneNumberDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
