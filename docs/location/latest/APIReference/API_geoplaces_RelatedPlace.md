---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_RelatedPlace.html
---

# RelatedPlace
<a name="API_geoplaces_RelatedPlace"></a>

Place that is related to the result item.

## Contents
<a name="API_geoplaces_RelatedPlace_Contents"></a>

 ** PlaceId **   <a name="location-Type-geoplaces_RelatedPlace-PlaceId"></a>
The `PlaceId` of the place result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** PlaceType **   <a name="location-Type-geoplaces_RelatedPlace-PlaceType"></a>
A `PlaceType` is a category that the result place must belong to.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_RelatedPlace-Title"></a>
The localized display name of this result item based on request parameter `language`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** AccessPoints **   <a name="location-Type-geoplaces_RelatedPlace-AccessPoints"></a>
Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Address **   <a name="location-Type-geoplaces_RelatedPlace-Address"></a>
The place address.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** Position **   <a name="location-Type-geoplaces_RelatedPlace-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

## See Also
<a name="API_geoplaces_RelatedPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/RelatedPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/RelatedPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/RelatedPlace)
