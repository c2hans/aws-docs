---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeQueryComponents.html
---

# GeocodeQueryComponents
<a name="API_geoplaces_GeocodeQueryComponents"></a>

A structured free text query allows you to search for places by the name or text representation of specific properties of the place.

## Contents
<a name="API_geoplaces_GeocodeQueryComponents_Contents"></a>

 ** AddressNumber **   <a name="location-Type-geoplaces_GeocodeQueryComponents-AddressNumber"></a>
The house number or address results should have.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** Country **   <a name="location-Type-geoplaces_GeocodeQueryComponents-Country"></a>
The alpha-2 or alpha-3 character code for the country that the results will be present in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** District **   <a name="location-Type-geoplaces_GeocodeQueryComponents-District"></a>
The district or division of a city the results should be present in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** Locality **   <a name="location-Type-geoplaces_GeocodeQueryComponents-Locality"></a>
The city or locality results should be present in.
Example: `Vancouver`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_GeocodeQueryComponents-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** Region **   <a name="location-Type-geoplaces_GeocodeQueryComponents-Region"></a>
The region or state results should be to be present in.
Example: `North Rhine-Westphalia`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** Street **   <a name="location-Type-geoplaces_GeocodeQueryComponents-Street"></a>
The name of the street results should be present in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_GeocodeQueryComponents-SubRegion"></a>
The sub-region or county for which results should be present in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^;]+`
Required: No

## See Also
<a name="API_geoplaces_GeocodeQueryComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/GeocodeQueryComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/GeocodeQueryComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/GeocodeQueryComponents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
