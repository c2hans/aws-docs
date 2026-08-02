---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocodeResultItem.html
---

# ReverseGeocodeResultItem
<a name="API_geoplaces_ReverseGeocodeResultItem"></a>

The returned location from the `Reverse Geocode` action.

## Contents
<a name="API_geoplaces_ReverseGeocodeResultItem_Contents"></a>

 ** PlaceId **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-PlaceId"></a>
The `PlaceId` of the place you wish to receive the information for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** PlaceType **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-PlaceType"></a>
A `PlaceType` is a category that the result place must belong to.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Title"></a>
The localized display name of this result item based on request parameter `language`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** AccessPoints **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-AccessPoints"></a>
 Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Address **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Address"></a>
The place's address.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** AddressNumberCorrected **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-AddressNumberCorrected"></a>
 Boolean indicating if the address provided has been corrected. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** Categories **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Categories"></a>
Categories of results that results must belong to.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Distance **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Distance"></a>
The distance in meters from the QueryPosition.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** EstimatedPointAddress **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-EstimatedPointAddress"></a>
If `true`, indicates that the coordinates of the position and access points of the point address are estimated.
Type: Boolean
Required: No

 ** FoodTypes **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-FoodTypes"></a>
 List of food types offered by this result. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [FoodType](API_geoplaces_FoodType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Intersections **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Intersections"></a>
 All Intersections that are near the provided address. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [Intersection](API_geoplaces_Intersection.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** MainAddress **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-MainAddress"></a>
The main address corresponding to a place of type Secondary Address.
Type: [RelatedPlace](API_geoplaces_RelatedPlace.md) object
Required: No

 ** MapView **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-MapView"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** PoliticalView **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Position **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** PostalCodeDetails **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-PostalCodeDetails"></a>
 Contains details about the postal code of the place/result. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [PostalCodeDetails](API_geoplaces_PostalCodeDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** TimeZone **   <a name="location-Type-geoplaces_ReverseGeocodeResultItem-TimeZone"></a>
The time zone in which the place is located.
Type: [TimeZone](API_geoplaces_TimeZone.md) object
Required: No

## See Also
<a name="API_geoplaces_ReverseGeocodeResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/ReverseGeocodeResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/ReverseGeocodeResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/ReverseGeocodeResultItem)
