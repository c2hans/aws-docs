---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationWithJurisdiction.html
---

# TaxRegistrationWithJurisdiction
<a name="API_taxSettings_TaxRegistrationWithJurisdiction"></a>

Your TRN information with jurisdiction details. This doesn't contain the full legal address associated with the TRN information.

## Contents
<a name="API_taxSettings_TaxRegistrationWithJurisdiction_Contents"></a>

 ** jurisdiction **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-jurisdiction"></a>
 The jurisdiction associated with your TRN information.
Type: [Jurisdiction](API_taxSettings_Jurisdiction.md) object
Required: Yes

 ** legalName **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-legalName"></a>
The legal name associated with your TRN information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-registrationId"></a>
Your tax registration unique identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationType **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-registrationType"></a>
 The type of your tax registration. This can be either `VAT` or `GST`.
Type: String
Valid Values: `VAT | GST | CPF | CNPJ | SST | TIN | NRIC | PAN | NIP`
Required: Yes

 ** status **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-status"></a>
The status of your TRN. This can be either `Verified`, `Pending`, `Deleted`, or `Rejected`.
Type: String
Valid Values: `Verified | Pending | Deleted | Rejected`
Required: Yes

 ** additionalTaxInformation **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-additionalTaxInformation"></a>
Additional tax information associated with your TRN.
Type: [AdditionalInfoResponse](API_taxSettings_AdditionalInfoResponse.md) object
Required: No

 ** certifiedEmailId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-certifiedEmailId"></a>
The email address to receive VAT invoices.
Type: String
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}`
Required: No

 ** sector **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-sector"></a>
The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document.
Type: String
Valid Values: `Business | Individual | Government`
Required: No

 ** taxDocumentMetadatas **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationWithJurisdiction-taxDocumentMetadatas"></a>
The metadata for your tax document.
Type: Array of [TaxDocumentMetadata](API_taxSettings_TaxDocumentMetadata.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_taxSettings_TaxRegistrationWithJurisdiction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxRegistrationWithJurisdiction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxRegistrationWithJurisdiction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxRegistrationWithJurisdiction)
