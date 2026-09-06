---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteAddressHighlights.html
---

# AutocompleteAddressHighlights
<a name="API_geoplaces_AutocompleteAddressHighlights"></a>

Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms.

## Contents
<a name="API_geoplaces_AutocompleteAddressHighlights_Contents"></a>

 ** AddressNumber **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-AddressNumber"></a>
The house number or address results should have.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Block **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Block"></a>
Name of the block.
Example: `Sunny Mansion 203 block: 2 Chome`
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Building **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Building"></a>
The name of the building at the address.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Country **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Country"></a>
The alpha-2 or alpha-3 character code for the country that the results will be present in.
Type: [CountryHighlights](API_geoplaces_CountryHighlights.md) object
Required: No

 ** District **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-District"></a>
The district or division of a city the results should be present in.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Intersection **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Intersection"></a>
Name of the streets in the intersection. For example: e.g. ["Friedrichstraße","Unter den Linden"]
Type: Array of arrays of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Label **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Label"></a>
Indicates the starting and ending indexes for result items where they are identified to match the input query. This should be used to provide emphasis to output display to make selecting the correct result from a list easier for end users.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Locality"></a>
The city or locality results should be present in.
Example: `Vancouver`.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Region **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Region"></a>
The region or state results should be to be present in.
Example: `North Rhine-Westphalia`.
Type: [RegionHighlights](API_geoplaces_RegionHighlights.md) object
Required: No

 ** Street **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-Street"></a>
The name of the street results should be present in.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubBlock **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-SubBlock"></a>
Name of sub-block.
Example: `Sunny Mansion 203 sub-block: 4`
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubDistrict **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-SubDistrict"></a>
Indicates the starting and ending index of the title in the text query that match the found title.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_AutocompleteAddressHighlights-SubRegion"></a>
The sub-region or county for which results should be present in.
Type: [SubRegionHighlights](API_geoplaces_SubRegionHighlights.md) object
Required: No

## See Also
<a name="API_geoplaces_AutocompleteAddressHighlights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AutocompleteAddressHighlights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AutocompleteAddressHighlights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AutocompleteAddressHighlights)
