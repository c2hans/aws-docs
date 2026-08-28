---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_Place.html
---

# Place
<a name="API_Place"></a>

Contains details about addresses or points of interest that match the search criteria.

Not all details are included with all responses. Some details may only be returned by specific data partners.

## Contents
<a name="API_Place_Contents"></a>

 ** Geometry **   <a name="location-Type-Place-Geometry"></a>
Places uses a point geometry to specify a location or a Place.
Type: [PlaceGeometry](API_PlaceGeometry.md) object
Required: Yes

 ** AddressNumber **   <a name="location-Type-Place-AddressNumber"></a>
The numerical portion of an address, such as a building number.
Type: String
Required: No

 ** Categories **   <a name="location-Type-Place-Categories"></a>
The Amazon Location categories that describe this Place.
For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html), in the *Amazon Location Service developer guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

 ** Country **   <a name="location-Type-Place-Country"></a>
A country/region specified using [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) 3-digit country/region code. For example, `CAN`.
Type: String
Required: No

 ** Interpolated **   <a name="location-Type-Place-Interpolated"></a>
 `True` if the result is interpolated from other known places.
 `False` if the Place is a known place.
Not returned when the partner does not provide the information.
For example, returns `False` for an address location that is found in the partner data, but returns `True` if an address does not exist in the partner data and its location is calculated by interpolating between other known addresses.
Type: Boolean
Required: No

 ** Label **   <a name="location-Type-Place-Label"></a>
The full name and address of the point of interest such as a city, region, or country. For example, `123 Any Street, Any Town, USA`.
Type: String
Required: No

 ** Municipality **   <a name="location-Type-Place-Municipality"></a>
A name for a local area, such as a city or town name. For example, `Toronto`.
Type: String
Required: No

 ** Neighborhood **   <a name="location-Type-Place-Neighborhood"></a>
The name of a community district. For example, `Downtown`.
Type: String
Required: No

 ** PostalCode **   <a name="location-Type-Place-PostalCode"></a>
A group of numbers and letters in a country-specific format, which accompanies the address for the purpose of identifying a location.
Type: String
Required: No

 ** Region **   <a name="location-Type-Place-Region"></a>
A name for an area or geographical division, such as a province or state name. For example, `British Columbia`.
Type: String
Required: No

 ** Street **   <a name="location-Type-Place-Street"></a>
The name for a street or a road to identify a location. For example, `Main Street`.
Type: String
Required: No

 ** SubMunicipality **   <a name="location-Type-Place-SubMunicipality"></a>
An area that's part of a larger municipality. For example, `Blissville ` is a submunicipality in the Queen County in New York.
This property supported by Esri and OpenData. The Esri property is `district`, and the OpenData property is `borough`.
Type: String
Required: No

 ** SubRegion **   <a name="location-Type-Place-SubRegion"></a>
A county, or an area that's part of a larger region. For example, `Metro Vancouver`.
Type: String
Required: No

 ** SupplementalCategories **   <a name="location-Type-Place-SupplementalCategories"></a>
Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

 ** TimeZone **   <a name="location-Type-Place-TimeZone"></a>
The time zone in which the `Place` is located. Returned only when using HERE or Grab as the selected partner.
Type: [TimeZone](API_TimeZone.md) object
Required: No

 ** UnitNumber **   <a name="location-Type-Place-UnitNumber"></a>
For addresses with multiple units, the unit identifier. Can include numbers and letters, for example `3B` or `Unit 123`.
Returned only for a place index that uses Esri or Grab as a data provider. Is not returned for `SearchPlaceIndexForPosition`.
Type: String
Required: No

 ** UnitType **   <a name="location-Type-Place-UnitType"></a>
For addresses with a `UnitNumber`, the type of unit. For example, `Apartment`.
Returned only for a place index that uses Esri as a data provider.
Type: String
Required: No

## See Also
<a name="API_Place_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/Place)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/Place)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/Place)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
