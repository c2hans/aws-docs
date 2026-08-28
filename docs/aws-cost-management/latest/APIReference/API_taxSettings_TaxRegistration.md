---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistration.html
---

# TaxRegistration
<a name="API_taxSettings_TaxRegistration"></a>

Your TRN information.

## Contents
<a name="API_taxSettings_TaxRegistration_Contents"></a>

 ** legalAddress **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-legalAddress"></a>
 The legal address associated with your TRN registration.
Type: [Address](API_taxSettings_Address.md) object
Required: Yes

 ** legalName **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-legalName"></a>
 The legal name associated with your TRN registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-registrationId"></a>
 Your tax registration unique identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationType **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-registrationType"></a>
Type of your tax registration.
Type: String
Valid Values: `VAT | GST | CPF | CNPJ | SST | TIN | NRIC | PAN | NIP`
Required: Yes

 ** status **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-status"></a>
 The status of your TRN. This can be either `Verified`, `Pending`, `Deleted`, or `Rejected`.
Type: String
Valid Values: `Verified | Pending | Deleted | Rejected`
Required: Yes

 ** additionalTaxInformation **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-additionalTaxInformation"></a>
 Additional tax information associated with your TRN.
Type: [AdditionalInfoResponse](API_taxSettings_AdditionalInfoResponse.md) object
Required: No

 ** certifiedEmailId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-certifiedEmailId"></a>
The email address to receive VAT invoices.
Type: String
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}`
Required: No

 ** sector **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-sector"></a>
The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government. Note that certain values may not applicable for the request country. Please refer to country specific information in API document.
Type: String
Valid Values: `Business | Individual | Government`
Required: No

 ** taxDocumentMetadatas **   <a name="awscostmanagement-Type-taxSettings_TaxRegistration-taxDocumentMetadatas"></a>
The metadata for your tax document.
Type: Array of [TaxDocumentMetadata](API_taxSettings_TaxDocumentMetadata.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_taxSettings_TaxRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
