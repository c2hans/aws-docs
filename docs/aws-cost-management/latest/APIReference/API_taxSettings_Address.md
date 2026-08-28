---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Address.html
---

# Address
<a name="API_taxSettings_Address"></a>

 The details of the address associated with the TRN information.

## Contents
<a name="API_taxSettings_Address_Contents"></a>

 ** countryCode **   <a name="awscostmanagement-Type-taxSettings_Address-countryCode"></a>
The country code for the country that the address is in.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[a-zA-Z]+`
Required: Yes

 ** postalCode **   <a name="awscostmanagement-Type-taxSettings_Address-postalCode"></a>
 The postal code associated with the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** addressLine1 **   <a name="awscostmanagement-Type-taxSettings_Address-addressLine1"></a>
The first line of the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** addressLine2 **   <a name="awscostmanagement-Type-taxSettings_Address-addressLine2"></a>
The second line of the address, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** addressLine3 **   <a name="awscostmanagement-Type-taxSettings_Address-addressLine3"></a>
 The third line of the address, if applicable. Currently, the Tax Settings API accepts the `addressLine3` parameter only for Saudi Arabia. When you specify a TRN in Saudi Arabia, you must enter the `addressLine3` and specify the building number for the address. For example, you might enter `1234`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** city **   <a name="awscostmanagement-Type-taxSettings_Address-city"></a>
The city that the address is in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** districtOrCounty **   <a name="awscostmanagement-Type-taxSettings_Address-districtOrCounty"></a>
The district or county the address is located.
For addresses in Brazil, this parameter uses the name of the neighborhood. When you set a TRN in Brazil, use `districtOrCounty` for the neighborhood name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** stateOrRegion **   <a name="awscostmanagement-Type-taxSettings_Address-stateOrRegion"></a>
The state, region, or province that the address is located. This field is only required for Canada, India, United Arab Emirates, Romania, and Brazil (CPF). It is optional for all other countries.
If this is required for tax settings, use the same name as shown on the **Tax Settings** page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

## See Also
<a name="API_taxSettings_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/Address)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
