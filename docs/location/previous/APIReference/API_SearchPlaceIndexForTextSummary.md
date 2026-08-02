---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForTextSummary.html
---

# SearchPlaceIndexForTextSummary
<a name="API_SearchPlaceIndexForTextSummary"></a>

A summary of the request sent by using `SearchPlaceIndexForText`.

## Contents
<a name="API_SearchPlaceIndexForTextSummary_Contents"></a>

 ** DataSource **   <a name="location-Type-SearchPlaceIndexForTextSummary-DataSource"></a>
The geospatial data provider attached to the place index resource specified in the request. Values can be one of the following:
+ Esri
+ Grab
+ Here
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** Text **   <a name="location-Type-SearchPlaceIndexForTextSummary-Text"></a>
The search text specified in the request.
Type: String
Required: Yes

 ** BiasPosition **   <a name="location-Type-SearchPlaceIndexForTextSummary-BiasPosition"></a>
Contains the coordinates for the optional bias position specified in the request.
This parameter contains a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.
For example, `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** FilterBBox **   <a name="location-Type-SearchPlaceIndexForTextSummary-FilterBBox"></a>
Contains the coordinates for the optional bounding box specified in the request.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** FilterCategories **   <a name="location-Type-SearchPlaceIndexForTextSummary-FilterCategories"></a>
The optional category filter specified in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

 ** FilterCountries **   <a name="location-Type-SearchPlaceIndexForTextSummary-FilterCountries"></a>
Contains the optional country filter specified in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Language **   <a name="location-Type-SearchPlaceIndexForTextSummary-Language"></a>
The preferred language used to return results. Matches the language in the request. The value is a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** MaxResults **   <a name="location-Type-SearchPlaceIndexForTextSummary-MaxResults"></a>
Contains the optional result count limit specified in the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** ResultBBox **   <a name="location-Type-SearchPlaceIndexForTextSummary-ResultBBox"></a>
The bounding box that fully contains all search results.
If you specified the optional `FilterBBox` parameter in the request, `ResultBBox` is contained within `FilterBBox`.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

## See Also
<a name="API_SearchPlaceIndexForTextSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchPlaceIndexForTextSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchPlaceIndexForTextSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchPlaceIndexForTextSummary)
