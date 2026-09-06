---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_BusinessVerificationDetails.html
---

# BusinessVerificationDetails
<a name="API_account_BusinessVerificationDetails"></a>

Contains the business information required for verifying a company's legal status and registration details within AWS Partner Central.

## Contents
<a name="API_account_BusinessVerificationDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CountryCode **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationDetails-CountryCode"></a>
The ISO 3166-1 alpha-2 country code where the business is legally registered and operates.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** LegalName **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationDetails-LegalName"></a>
The official legal name of the business as registered with the appropriate government authorities.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** RegistrationId **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationDetails-RegistrationId"></a>
The unique business registration identifier assigned by the government or regulatory authority, such as a company registration number or tax identification number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** JurisdictionOfIncorporation **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationDetails-JurisdictionOfIncorporation"></a>
The specific legal jurisdiction or state where the business was incorporated or registered, providing additional location context beyond the country code.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z0-9]{2}`
Required: No

## See Also
<a name="API_account_BusinessVerificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/BusinessVerificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/BusinessVerificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/BusinessVerificationDetails)
