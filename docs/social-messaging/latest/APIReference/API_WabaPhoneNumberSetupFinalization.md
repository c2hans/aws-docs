---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WabaPhoneNumberSetupFinalization.html
---

# WabaPhoneNumberSetupFinalization
<a name="API_WabaPhoneNumberSetupFinalization"></a>

The registration details for a linked phone number.

## Contents
<a name="API_WabaPhoneNumberSetupFinalization_Contents"></a>

 ** id **   <a name="Social-Type-WabaPhoneNumberSetupFinalization-id"></a>
The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use the [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) API action to find a phone number's id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** twoFactorPin **   <a name="Social-Type-WabaPhoneNumberSetupFinalization-twoFactorPin"></a>
The PIN to use for two-step verification. To reset your PIN follow the directions in [Updating PIN](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin) in the *WhatsApp Business Platform Cloud API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Required: Yes

 ** dataLocalizationRegion **   <a name="Social-Type-WabaPhoneNumberSetupFinalization-dataLocalizationRegion"></a>
The two letter ISO region for the location of where Meta will store data.

**Asia–Pacific (APAC)**
+ Australia **AU**
+ Indonesia **ID**
+ India **IN**
+ Japan **JP**
+ Singapore **SG**
+ South Korea **KR**

**Europe**
+ Germany **DE**
+ Switzerland **CH**
+ United Kingdom **GB**

**Latin America (LATAM)**
+ Brazil **BR**

**Middle East and Africa (MEA)**
+ Bahrain **BH**
+ South Africa **ZA**
+ United Arab Emirates **AE**

**North America (NORAM)**
+ Canada **CA**
Type: String
Pattern: `[A-Z]{2}`
Required: No

 ** tags **   <a name="Social-Type-WabaPhoneNumberSetupFinalization-tags"></a>
An array of key and value pair tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_WabaPhoneNumberSetupFinalization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WabaPhoneNumberSetupFinalization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WabaPhoneNumberSetupFinalization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WabaPhoneNumberSetupFinalization)
