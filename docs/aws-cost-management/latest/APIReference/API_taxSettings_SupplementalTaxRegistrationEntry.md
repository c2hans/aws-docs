---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SupplementalTaxRegistrationEntry.html
---

# SupplementalTaxRegistrationEntry
<a name="API_taxSettings_SupplementalTaxRegistrationEntry"></a>

 The supplemental TRN information to provide when adding or updating a supplemental TRN.

## Contents
<a name="API_taxSettings_SupplementalTaxRegistrationEntry_Contents"></a>

 ** address **   <a name="awscostmanagement-Type-taxSettings_SupplementalTaxRegistrationEntry-address"></a>
 The details of the address associated with the TRN information.
Type: [Address](API_taxSettings_Address.md) object
Required: Yes

 ** legalName **   <a name="awscostmanagement-Type-taxSettings_SupplementalTaxRegistrationEntry-legalName"></a>
 The legal name associated with your TRN registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationId **   <a name="awscostmanagement-Type-taxSettings_SupplementalTaxRegistrationEntry-registrationId"></a>
 The supplemental TRN unique identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationType **   <a name="awscostmanagement-Type-taxSettings_SupplementalTaxRegistrationEntry-registrationType"></a>
 Type of supplemental TRN. Currently, this can only be VAT.
Type: String
Valid Values: `VAT`
Required: Yes

## See Also
<a name="API_taxSettings_SupplementalTaxRegistrationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/SupplementalTaxRegistrationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/SupplementalTaxRegistrationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/SupplementalTaxRegistrationEntry)
