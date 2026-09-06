---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeParsedQueryAddressComponents.html
---

# GeocodeParsedQueryAddressComponents
<a name="API_geoplaces_GeocodeParsedQueryAddressComponents"></a>

Parsed address components in the provided QueryText.

## Contents
<a name="API_geoplaces_GeocodeParsedQueryAddressComponents_Contents"></a>

 ** AddressNumber **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-AddressNumber"></a>
The number that identifies an address within a street.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Block **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Block"></a>
Name of the block.
Example: `Sunny Mansion 203 block: 2 Chome`
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Building **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Building"></a>
The name of the building at the address.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Country **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Country"></a>
The alpha-2 or alpha-3 character code for the country that the results will be present in.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** District **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-District"></a>
The district or division of a city the results should be present in.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Locality"></a>
The city or locality of the address.
Example: `Vancouver`.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** OtherComponents **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-OtherComponents"></a>
Additional information extracted from the query that does not correspond to standard address components.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Region **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Region"></a>
The region or state results should be present in.
Example: `North Rhine-Westphalia`.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SecondaryAddressComponents **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-SecondaryAddressComponents"></a>
Parsed secondary address components from the provided query text.
Coverage for `ParsedQuery.Address.SecondaryAddressComponents` is available in the following countries:
AUS, AUT, BRA, CAN, ESP, FRA, GBR, HKG, IDN, IND, NZL, TUR, TWN, USA
Type: Array of [ParsedQuerySecondaryAddressComponent](API_geoplaces_ParsedQuerySecondaryAddressComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Street **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-Street"></a>
The name of the street results should be present in.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubBlock **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-SubBlock"></a>
Name of sub-block.
Example: `Sunny Mansion 203 sub-block: 4`
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubDistrict **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-SubDistrict"></a>
A subdivision of a district.
Example: `Minden-Lübbecke`.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_GeocodeParsedQueryAddressComponents-SubRegion"></a>
The sub-region or county for which results should be present in.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_geoplaces_GeocodeParsedQueryAddressComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/GeocodeParsedQueryAddressComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/GeocodeParsedQueryAddressComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/GeocodeParsedQueryAddressComponents)
