---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_Address.html
---

# Address

The postal address of a legal entity.

## Contents
<a name="API_channel_Address_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** addressLine **   <a name="AWSPartnerCentral-Type-channel_Address-addressLine"></a>
The first line of the street address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `\p{Z}*[^\p{C}\p{Z}][^\p{C}]*`
Required: Yes

 ** city **   <a name="AWSPartnerCentral-Type-channel_Address-city"></a>
The city or locality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\p{Z}*[^\p{C}\p{Z}][^\p{C}]*`
Required: Yes

 ** countryCode **   <a name="AWSPartnerCentral-Type-channel_Address-countryCode"></a>
The two-letter ISO 3166-1 country code.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** postalCode **   <a name="AWSPartnerCentral-Type-channel_Address-postalCode"></a>
The postal code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `\p{Z}*[^\p{C}\p{Z}][^\p{C}]*`
Required: Yes

 ** stateOrRegion **   <a name="AWSPartnerCentral-Type-channel_Address-stateOrRegion"></a>
The state, province, or prefecture.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\p{Z}*[^\p{C}\p{Z}][^\p{C}]*`
Required: Yes

 ** addressLine2 **   <a name="AWSPartnerCentral-Type-channel_Address-addressLine2"></a>
The second line of the street address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `\p{Z}*[^\p{C}\p{Z}][^\p{C}]*`
Required: No

## See Also
<a name="API_channel_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/Address)
