---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestPlaceResult.html
---

# SuggestPlaceResult
<a name="API_geoplaces_SuggestPlaceResult"></a>

The suggested place results.

## Contents
<a name="API_geoplaces_SuggestPlaceResult_Contents"></a>

 ** AccessPoints **   <a name="location-Type-geoplaces_SuggestPlaceResult-AccessPoints"></a>
 Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** AccessRestrictions **   <a name="location-Type-geoplaces_SuggestPlaceResult-AccessRestrictions"></a>
 Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [AccessRestriction](API_geoplaces_AccessRestriction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Address **   <a name="location-Type-geoplaces_SuggestPlaceResult-Address"></a>
The place's address.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** BusinessChains **   <a name="location-Type-geoplaces_SuggestPlaceResult-BusinessChains"></a>
 The Business Chains associated with the place. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [BusinessChain](API_geoplaces_BusinessChain.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Categories **   <a name="location-Type-geoplaces_SuggestPlaceResult-Categories"></a>
Categories of results that results must belong to.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** CrossReferences **   <a name="location-Type-geoplaces_SuggestPlaceResult-CrossReferences"></a>
The list of supplier references available for this place. Requires the `CrossReferences` additional feature to be enabled.
Type: Array of [CrossReference](API_geoplaces_CrossReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Distance **   <a name="location-Type-geoplaces_SuggestPlaceResult-Distance"></a>
The distance in meters from the QueryPosition.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** FoodTypes **   <a name="location-Type-geoplaces_SuggestPlaceResult-FoodTypes"></a>
 List of food types offered by this result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [FoodType](API_geoplaces_FoodType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** MapView **   <a name="location-Type-geoplaces_SuggestPlaceResult-MapView"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Phonemes **   <a name="location-Type-geoplaces_SuggestPlaceResult-Phonemes"></a>
 How the various components of the result's address are pronounced in various languages. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: [PhonemeDetails](API_geoplaces_PhonemeDetails.md) object
Required: No

 ** PlaceAttributes **   <a name="location-Type-geoplaces_SuggestPlaceResult-PlaceAttributes"></a>
A list of place attributes for the result, such as whether the business offers drive-through service.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `DriveThrough`
Required: No

 ** PlaceId **   <a name="location-Type-geoplaces_SuggestPlaceResult-PlaceId"></a>
The `PlaceId` of the place you wish to receive the information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** PlaceType **   <a name="location-Type-geoplaces_SuggestPlaceResult-PlaceType"></a>
A `PlaceType` is a category that the result place must belong to.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`
Required: No

 ** PoliticalView **   <a name="location-Type-geoplaces_SuggestPlaceResult-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Position **   <a name="location-Type-geoplaces_SuggestPlaceResult-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** TimeZone **   <a name="location-Type-geoplaces_SuggestPlaceResult-TimeZone"></a>
The time zone in which the place is located.
Type: [TimeZone](API_geoplaces_TimeZone.md) object
Required: No

## See Also
<a name="API_geoplaces_SuggestPlaceResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SuggestPlaceResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SuggestPlaceResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SuggestPlaceResult)
