---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Address.html
---

# Address
<a name="API_Address"></a>

 Information about an address.

## Contents
<a name="API_Address_Contents"></a>

 ** AddressLine1 **   <a name="outposts-Type-Address-AddressLine1"></a>
The first line of the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^\S[\S ]*$`
Required: Yes

 ** City **   <a name="outposts-Type-Address-City"></a>
The city for the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`
Required: Yes

 ** ContactName **   <a name="outposts-Type-Address-ContactName"></a>
The name of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^\S[\S ]*$`
Required: Yes

 ** ContactPhoneNumber **   <a name="outposts-Type-Address-ContactPhoneNumber"></a>
The phone number of the contact, including the country code (for example, `+12065550100`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+[1-9][0-9]{1,18}`
Required: Yes

 ** CountryCode **   <a name="outposts-Type-Address-CountryCode"></a>
The ISO-3166 two-letter country code for the address.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: Yes

 ** PostalCode **   <a name="outposts-Type-Address-PostalCode"></a>
The postal code for the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-zA-Z0-9 -]+$`
Required: Yes

 ** StateOrRegion **   <a name="outposts-Type-Address-StateOrRegion"></a>
The state for the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`
Required: Yes

 ** AddressLine2 **   <a name="outposts-Type-Address-AddressLine2"></a>
The second line of the address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 60.
Pattern: `^\S[\S ]*$`
Required: No

 ** AddressLine3 **   <a name="outposts-Type-Address-AddressLine3"></a>
The third line of the address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 60.
Pattern: `^\S[\S ]*$`
Required: No

 ** DistrictOrCounty **   <a name="outposts-Type-Address-DistrictOrCounty"></a>
The district or county for the address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `^\S[\S ]*`
Required: No

 ** Municipality **   <a name="outposts-Type-Address-Municipality"></a>
The municipality for the address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 180.
Pattern: `^\S[\S ]*$`
Required: No

## See Also
<a name="API_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Address)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
