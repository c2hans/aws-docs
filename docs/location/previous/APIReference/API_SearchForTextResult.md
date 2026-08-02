---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchForTextResult.html
---

# SearchForTextResult
<a name="API_SearchForTextResult"></a>

Contains a search result from a text search query that is run on a place index resource.

## Contents
<a name="API_SearchForTextResult_Contents"></a>

 ** Place **   <a name="location-Type-SearchForTextResult-Place"></a>
Details about the search result, such as its address and position.
Type: [Place](API_Place.md) object
Required: Yes

 ** Distance **   <a name="location-Type-SearchForTextResult-Distance"></a>
The distance in meters of a great-circle arc between the bias position specified and the result. `Distance` will be returned only if a bias position was specified in the query.
A great-circle arc is the shortest path on a sphere, in this case the Earth. This returns the shortest distance between two locations.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** PlaceId **   <a name="location-Type-SearchForTextResult-PlaceId"></a>
The unique identifier of the place. You can use this with the `GetPlace` operation to find the place again later.
For `SearchPlaceIndexForText` operations, the `PlaceId` is returned only by place indexes that use HERE or Grab as a data provider.
Type: String
Required: No

 ** Relevance **   <a name="location-Type-SearchForTextResult-Relevance"></a>
The relative confidence in the match for a result among the results returned. For example, if more fields for an address match (including house number, street, city, country/region, and postal code), the relevance score is closer to 1.
Returned only when the partner selected is Esri or Grab.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_SearchForTextResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchForTextResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchForTextResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchForTextResult)
