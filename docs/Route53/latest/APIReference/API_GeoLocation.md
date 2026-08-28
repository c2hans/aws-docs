---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html
---

# GeoLocation
<a name="API_GeoLocation"></a>

A complex type that contains information about a geographic location.

## Contents
<a name="API_GeoLocation_Contents"></a>

 ** ContinentCode **   <a name="Route53-Type-GeoLocation-ContinentCode"></a>
The two-letter code for the continent.
Amazon Route 53 supports the following continent codes:
+  **AF**: Africa
+  **AN**: Antarctica
+  **AS**: Asia
+  **EU**: Europe
+  **OC**: Oceania
+  **NA**: North America
+  **SA**: South America
Constraint: Specifying `ContinentCode` with either `CountryCode` or `SubdivisionCode` returns an `InvalidInput` error.
Type: String
Length Constraints: Fixed length of 2.
Required: No

 ** CountryCode **   <a name="Route53-Type-GeoLocation-CountryCode"></a>
For geolocation resource record sets, the two-letter code for a country.
Amazon Route 53 uses the two-letter country codes that are specified in [ISO standard 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
Route 53 also supports the country code **UA** for Ukraine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2.
Required: No

 ** SubdivisionCode **   <a name="Route53-Type-GeoLocation-SubdivisionCode"></a>
For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn't support any other values for `SubdivisionCode`. For a list of state abbreviations, see [Appendix B: Two–Letter State and Possession Abbreviations](https://pe.usps.com/text/pub28/28apb.htm) on the United States Postal Service website.
If you specify `subdivisioncode`, you must also specify `US` for `CountryCode`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: No

## See Also
<a name="API_GeoLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GeoLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GeoLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GeoLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
