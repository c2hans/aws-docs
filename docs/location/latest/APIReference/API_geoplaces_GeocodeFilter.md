---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeFilter.html
---

# GeocodeFilter
<a name="API_geoplaces_GeocodeFilter"></a>

Geocode structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.

## Contents
<a name="API_geoplaces_GeocodeFilter_Contents"></a>

 ** IncludeCountries **   <a name="location-Type-geoplaces_GeocodeFilter-IncludeCountries"></a>
 A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** IncludePlaceTypes **   <a name="location-Type-geoplaces_GeocodeFilter-IncludePlaceTypes"></a>
The included place types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `Locality | PostalCode | Intersection | Street | PointAddress | InterpolatedAddress | SecondaryAddress | PointOfInterest | Country | Region`
Required: No

## See Also
<a name="API_geoplaces_GeocodeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/GeocodeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/GeocodeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/GeocodeFilter)
