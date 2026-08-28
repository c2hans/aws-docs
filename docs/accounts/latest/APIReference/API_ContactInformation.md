---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_ContactInformation.html
---

# ContactInformation
<a name="API_ContactInformation"></a>

Contains the details of the primary contact information associated with an AWS account.

## Contents
<a name="API_ContactInformation_Contents"></a>

 ** AddressLine1 **   <a name="accounts-Type-ContactInformation-AddressLine1"></a>
The first line of the primary contact address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Required: Yes

 ** City **   <a name="accounts-Type-ContactInformation-City"></a>
The city of the primary contact address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** CountryCode **   <a name="accounts-Type-ContactInformation-CountryCode"></a>
The ISO-3166 two-letter country code for the primary contact address.
Type: String
Length Constraints: Fixed length of 2.
Required: Yes

 ** FullName **   <a name="accounts-Type-ContactInformation-FullName"></a>
The full name of the primary contact address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** PhoneNumber **   <a name="accounts-Type-ContactInformation-PhoneNumber"></a>
The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[+][\s0-9()-]+`
Required: Yes

 ** PostalCode **   <a name="accounts-Type-ContactInformation-PostalCode"></a>
The postal code of the primary contact address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: Yes

 ** AddressLine2 **   <a name="accounts-Type-ContactInformation-AddressLine2"></a>
The second line of the primary contact address, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Required: No

 ** AddressLine3 **   <a name="accounts-Type-ContactInformation-AddressLine3"></a>
The third line of the primary contact address, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Required: No

 ** CompanyName **   <a name="accounts-Type-ContactInformation-CompanyName"></a>
The name of the company associated with the primary contact information, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** DistrictOrCounty **   <a name="accounts-Type-ContactInformation-DistrictOrCounty"></a>
The district or county of the primary contact address, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** StateOrRegion **   <a name="accounts-Type-ContactInformation-StateOrRegion"></a>
The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, `NJ`) or the full state name (for example, `New Jersey`). This field is required in the following countries: `US`, `CA`, `GB`, `DE`, `JP`, `IN`, and `BR`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** WebsiteUrl **   <a name="accounts-Type-ContactInformation-WebsiteUrl"></a>
The URL of the website associated with the primary contact information, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ContactInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/ContactInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/ContactInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/ContactInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Account Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query accounts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
