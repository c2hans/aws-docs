---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Address.html
---

# Address
<a name="API_geoplaces_Address"></a>

The place address.

## Contents
<a name="API_geoplaces_Address_Contents"></a>

 ** AddressNumber **   <a name="location-Type-geoplaces_Address-AddressNumber"></a>
The number that identifies an address within a street.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: No

 ** Block **   <a name="location-Type-geoplaces_Address-Block"></a>
 Name of the block. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Example: `Sunny Mansion 203 block: 2 Chome`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Building **   <a name="location-Type-geoplaces_Address-Building"></a>
 The name of the building at the address. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Country **   <a name="location-Type-geoplaces_Address-Country"></a>
The country component of the address.
Type: [Country](API_geoplaces_Country.md) object
Required: No

 ** District **   <a name="location-Type-geoplaces_Address-District"></a>
The district or division of a locality associated with this address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Intersection **   <a name="location-Type-geoplaces_Address-Intersection"></a>
 Name of the streets in the intersection. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Example: `["Friedrichstraße","Unter den Linden"]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Label **   <a name="location-Type-geoplaces_Address-Label"></a>
Assembled address value built out of the address components, according to the regional postal rules. This is the correctly formatted address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_Address-Locality"></a>
The city or locality of the address.
Example: `Vancouver`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_Address-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** Region **   <a name="location-Type-geoplaces_Address-Region"></a>
The region or state results should be present in.
Example: `North Rhine-Westphalia`.
Type: [Region](API_geoplaces_Region.md) object
Required: No

 ** SecondaryAddressComponents **   <a name="location-Type-geoplaces_Address-SecondaryAddressComponents"></a>
 Components that correspond to secondary identifiers on an Address. Secondary address components include information such as Suite or Unit Number, Building, or Floor. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Coverage for `Address.SecondaryAddressComponents` is available in the following countries:
AUS, CAN, NZL, USA, PRI
Type: Array of [SecondaryAddressComponent](API_geoplaces_SecondaryAddressComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** Street **   <a name="location-Type-geoplaces_Address-Street"></a>
The name of the street results should be present in.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** StreetComponents **   <a name="location-Type-geoplaces_Address-StreetComponents"></a>
 Components of the street. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Example: Yonge from "Yonge street".
Type: Array of [StreetComponents](API_geoplaces_StreetComponents.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SubBlock **   <a name="location-Type-geoplaces_Address-SubBlock"></a>
 Name of sub-block. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Example: `Sunny Mansion 203 sub-block: 4`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** SubDistrict **   <a name="location-Type-geoplaces_Address-SubDistrict"></a>
A subdivision of a district.
Example: `Minden-Lübbecke`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_Address-SubRegion"></a>
The sub-region or county for which results should be present in.
Type: [SubRegion](API_geoplaces_SubRegion.md) object
Required: No

## See Also
<a name="API_geoplaces_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Address)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
