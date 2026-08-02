---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearbyFilter.html
---

# SearchNearbyFilter
<a name="API_geoplaces_SearchNearbyFilter"></a>

SearchNearby structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.

## Contents
<a name="API_geoplaces_SearchNearbyFilter_Contents"></a>

 ** BoundingBox **   <a name="location-Type-geoplaces_SearchNearbyFilter-BoundingBox"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** ExcludeBusinessChains **   <a name="location-Type-geoplaces_SearchNearbyFilter-ExcludeBusinessChains"></a>
The Business Chains associated with the place.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ExcludeCategories **   <a name="location-Type-geoplaces_SearchNearbyFilter-ExcludeCategories"></a>
Categories of results that results are excluded from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ExcludeFoodTypes **   <a name="location-Type-geoplaces_SearchNearbyFilter-ExcludeFoodTypes"></a>
Food types that results are excluded from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IncludeBusinessChains **   <a name="location-Type-geoplaces_SearchNearbyFilter-IncludeBusinessChains"></a>
The Business Chains associated with the place.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IncludeCategories **   <a name="location-Type-geoplaces_SearchNearbyFilter-IncludeCategories"></a>
Categories of results that results must belong too.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IncludeCountries **   <a name="location-Type-geoplaces_SearchNearbyFilter-IncludeCountries"></a>
A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** IncludeFoodTypes **   <a name="location-Type-geoplaces_SearchNearbyFilter-IncludeFoodTypes"></a>
Food types that results are included from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_geoplaces_SearchNearbyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SearchNearbyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SearchNearbyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SearchNearbyFilter)
