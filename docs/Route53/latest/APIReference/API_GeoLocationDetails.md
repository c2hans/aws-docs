---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocationDetails.html
---

# GeoLocationDetails
<a name="API_GeoLocationDetails"></a>

A complex type that contains the codes and full continent, country, and subdivision names for the specified `geolocation` code.

## Contents
<a name="API_GeoLocationDetails_Contents"></a>

 ** ContinentCode **   <a name="Route53-Type-GeoLocationDetails-ContinentCode"></a>
The two-letter code for the continent.
Type: String
Length Constraints: Fixed length of 2.
Required: No

 ** ContinentName **   <a name="Route53-Type-GeoLocationDetails-ContinentName"></a>
The full name of the continent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** CountryCode **   <a name="Route53-Type-GeoLocationDetails-CountryCode"></a>
The two-letter code for the country.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2.
Required: No

 ** CountryName **   <a name="Route53-Type-GeoLocationDetails-CountryName"></a>
The name of the country.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubdivisionCode **   <a name="Route53-Type-GeoLocationDetails-SubdivisionCode"></a>
The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see [Appendix B: Two–Letter State and Possession Abbreviations](https://pe.usps.com/text/pub28/28apb.htm) on the United States Postal Service website. For a list of all supported subdivision codes, use the [ListGeoLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: No

 ** SubdivisionName **   <a name="Route53-Type-GeoLocationDetails-SubdivisionName"></a>
The full name of the subdivision. Route 53 currently supports only states in the United States.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_GeoLocationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GeoLocationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GeoLocationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GeoLocationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
