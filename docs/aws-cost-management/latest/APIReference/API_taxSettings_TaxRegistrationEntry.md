---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationEntry.html
---

# TaxRegistrationEntry
<a name="API_taxSettings_TaxRegistrationEntry"></a>

The TRN information you provide when you add a new TRN, or update.

## Contents
<a name="API_taxSettings_TaxRegistrationEntry_Contents"></a>

 ** registrationId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-registrationId"></a>
Your tax registration unique identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** registrationType **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-registrationType"></a>
 Your tax registration type. This can be either `VAT` or `GST`.
Type: String
Valid Values: `VAT | GST | CPF | CNPJ | SST | TIN | NRIC | PAN | NIP`
Required: Yes

 ** additionalTaxInformation **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-additionalTaxInformation"></a>
 Additional tax information associated with your TRN. You only need to specify this parameter if AWS collects any additional information for your country within [AdditionalInfoRequest](API_taxSettings_AdditionalInfoRequest.md).
Type: [AdditionalInfoRequest](API_taxSettings_AdditionalInfoRequest.md) object
Required: No

 ** certifiedEmailId **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-certifiedEmailId"></a>
The email address to receive VAT invoices.
Type: String
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}`
Required: No

 ** legalAddress **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-legalAddress"></a>
The legal address associated with your TRN.
If you're setting a TRN in Brazil for the CNPJ tax type, you don't need to specify the legal address.
For TRNs in other countries and for CPF tax types Brazil, you must specify the legal address.
Type: [Address](API_taxSettings_Address.md) object
Required: No

 ** legalName **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-legalName"></a>
The legal name associated with your TRN.
If you're setting a TRN in Brazil, you don't need to specify the legal name. For TRNs in other countries, you must specify the legal name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** sector **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-sector"></a>
The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document.
Type: String
Valid Values: `Business | Individual | Government`
Required: No

 ** verificationDetails **   <a name="awscostmanagement-Type-taxSettings_TaxRegistrationEntry-verificationDetails"></a>
Additional details needed to verify your TRN information in Brazil. You only need to specify this parameter when you set a TRN in Brazil that is the CPF tax type.
Don't specify this parameter to set a TRN in Brazil of the CNPJ tax type or to set a TRN for another country.
Type: [VerificationDetails](API_taxSettings_VerificationDetails.md) object
Required: No

## See Also
<a name="API_taxSettings_TaxRegistrationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxRegistrationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxRegistrationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxRegistrationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
