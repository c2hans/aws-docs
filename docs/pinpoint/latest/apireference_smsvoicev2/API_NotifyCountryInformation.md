---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_NotifyCountryInformation.html
---

# NotifyCountryInformation
<a name="API_NotifyCountryInformation"></a>

The information for a country that supports notify messaging.

## Contents
<a name="API_NotifyCountryInformation_Contents"></a>

 ** CountryName **   <a name="pinpoint-Type-NotifyCountryInformation-CountryName"></a>
The name of the country.
Type: String
Required: Yes

 ** CustomerOwnedIdentityRequired **   <a name="pinpoint-Type-NotifyCountryInformation-CustomerOwnedIdentityRequired"></a>
Whether a customer-owned identity is required to send notify messages to this country.
Type: Boolean
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-NotifyCountryInformation-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** SupportedChannels **   <a name="pinpoint-Type-NotifyCountryInformation-SupportedChannels"></a>
An array of supported channels for the country. Supported values include `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** SupportedTiers **   <a name="pinpoint-Type-NotifyCountryInformation-SupportedTiers"></a>
An array of supported tiers for the country.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BASIC | ADVANCED`
Required: Yes

 ** SupportedUseCases **   <a name="pinpoint-Type-NotifyCountryInformation-SupportedUseCases"></a>
An array of supported use cases for the country.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `CODE_VERIFICATION`
Required: Yes

## See Also
<a name="API_NotifyCountryInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/NotifyCountryInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/NotifyCountryInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/NotifyCountryInformation)
