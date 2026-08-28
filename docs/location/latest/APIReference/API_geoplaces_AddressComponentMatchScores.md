---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AddressComponentMatchScores.html
---

# AddressComponentMatchScores
<a name="API_geoplaces_AddressComponentMatchScores"></a>

Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.

## Contents
<a name="API_geoplaces_AddressComponentMatchScores_Contents"></a>

 ** AddressNumber **   <a name="location-Type-geoplaces_AddressComponentMatchScores-AddressNumber"></a>
The house number or address results should have.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Block **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Block"></a>
Name of the block.
Example: `Sunny Mansion 203 block: 2 Chome`
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Building **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Building"></a>
The name of the building at the address.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Country **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Country"></a>
The alpha-2 or alpha-3 character code for the country that the results will be present in.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** District **   <a name="location-Type-geoplaces_AddressComponentMatchScores-District"></a>
The district or division of a city the results should be present in.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Intersection **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Intersection"></a>
Name of the streets in the intersection.
Example: `["Friedrichstraße","Unter den Linden"]`
Type: Array of doubles
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Locality"></a>
The city or locality results should be present in.
Example: `Vancouver`.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_AddressComponentMatchScores-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Region **   <a name="location-Type-geoplaces_AddressComponentMatchScores-Region"></a>
The region or state results should be to be present in.
Example: `North Rhine-Westphalia`.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** SecondaryAddressComponents **   <a name="location-Type-geoplaces_AddressComponentMatchScores-SecondaryAddressComponents"></a>
Match scores for the secondary address components in the result.
Coverage for this functionality is available in the following countries: AUS, AUT, BRA, CAN, ESP, FRA, GBR, IDN, IND, NZL, TUR, TWN, USA.
Type: Array of [SecondaryAddressComponentMatchScore](API_geoplaces_SecondaryAddressComponentMatchScore.md) objects
Required: No

 ** SubBlock **   <a name="location-Type-geoplaces_AddressComponentMatchScores-SubBlock"></a>
Name of sub-block.
Example: `Sunny Mansion 203 sub-block: 4`
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** SubDistrict **   <a name="location-Type-geoplaces_AddressComponentMatchScores-SubDistrict"></a>
A subdivision of a district.
Example: `Minden-Lübbecke`
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_AddressComponentMatchScores-SubRegion"></a>
The sub-region or county for which results should be present in.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_geoplaces_AddressComponentMatchScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AddressComponentMatchScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AddressComponentMatchScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AddressComponentMatchScores)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
