---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteFilter.html
---

# AutocompleteFilter
<a name="API_geoplaces_AutocompleteFilter"></a>

Autocomplete structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.

## Contents
<a name="API_geoplaces_AutocompleteFilter_Contents"></a>

 ** BoundingBox **   <a name="location-Type-geoplaces_AutocompleteFilter-BoundingBox"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Circle **   <a name="location-Type-geoplaces_AutocompleteFilter-Circle"></a>
The `Circle` that all results must be in.
Type: [FilterCircle](API_geoplaces_FilterCircle.md) object
Required: No

 ** IncludeCountries **   <a name="location-Type-geoplaces_AutocompleteFilter-IncludeCountries"></a>
 A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** IncludePlaceTypes **   <a name="location-Type-geoplaces_AutocompleteFilter-IncludePlaceTypes"></a>
The included place types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `Locality | PostalCode | Street | Intersection | PointAddress | InterpolatedAddress | Country | Region`
Required: No

## See Also
<a name="API_geoplaces_AutocompleteFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AutocompleteFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AutocompleteFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AutocompleteFilter)
