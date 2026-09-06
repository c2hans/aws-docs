---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_Headquarters.html
---

# Headquarters
<a name="API_account_Headquarters"></a>

Contains the partner's headquarters location using International Organization for Standardization (ISO) 3166 country and subdivision codes.

## Contents
<a name="API_account_Headquarters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CountryCode **   <a name="AWSPartnerCentral-Type-account_Headquarters-CountryCode"></a>
The ISO 3166-1 alpha-2 country code of the partner's headquarters. For example, `US`, `BR`, or `DE`.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** SubdivisionCode **   <a name="AWSPartnerCentral-Type-account_Headquarters-SubdivisionCode"></a>
The subdivision portion of the ISO 3166-2 code for the partner's headquarters (for example, `SP` from `BR-SP`, `NSW` from `AU-NSW`, or `13` from `JP-13`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `[A-Z0-9]{1,3}`
Required: Yes

## See Also
<a name="API_account_Headquarters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/Headquarters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/Headquarters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/Headquarters)
