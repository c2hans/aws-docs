---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchTextResultItem.html
---

# SearchTextResultItem
<a name="API_geoplaces_SearchTextResultItem"></a>

The text search result.

## Contents
<a name="API_geoplaces_SearchTextResultItem_Contents"></a>

 ** PlaceId **   <a name="location-Type-geoplaces_SearchTextResultItem-PlaceId"></a>
The `PlaceId` of the place you wish to receive the information for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** PlaceType **   <a name="location-Type-geoplaces_SearchTextResultItem-PlaceType"></a>
A `PlaceType` is a category that the result place must belong to.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_SearchTextResultItem-Title"></a>
The item's title.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** AccessPoints **   <a name="location-Type-geoplaces_SearchTextResultItem-AccessPoints"></a>
Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** AccessRestrictions **   <a name="location-Type-geoplaces_SearchTextResultItem-AccessRestrictions"></a>
Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction.
Type: Array of [AccessRestriction](API_geoplaces_AccessRestriction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Address **   <a name="location-Type-geoplaces_SearchTextResultItem-Address"></a>
The place's address.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** AddressNumberCorrected **   <a name="location-Type-geoplaces_SearchTextResultItem-AddressNumberCorrected"></a>
Boolean indicating if the address provided has been corrected.
Type: Boolean
Required: No

 ** BusinessChains **   <a name="location-Type-geoplaces_SearchTextResultItem-BusinessChains"></a>
The Business Chains associated with the place.
Type: Array of [BusinessChain](API_geoplaces_BusinessChain.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Categories **   <a name="location-Type-geoplaces_SearchTextResultItem-Categories"></a>
Categories of results that results must belong to.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Contacts **   <a name="location-Type-geoplaces_SearchTextResultItem-Contacts"></a>
List of potential contact methods for the result/place.
Type: [Contacts](API_geoplaces_Contacts.md) object
Required: No

 ** CrossReferences **   <a name="location-Type-geoplaces_SearchTextResultItem-CrossReferences"></a>
The list of supplier references available for this place. Requires the `CrossReferences` additional feature to be enabled.
Type: Array of [CrossReference](API_geoplaces_CrossReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Distance **   <a name="location-Type-geoplaces_SearchTextResultItem-Distance"></a>
The distance in meters from the QueryPosition.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** FoodTypes **   <a name="location-Type-geoplaces_SearchTextResultItem-FoodTypes"></a>
List of food types offered by this result.
Type: Array of [FoodType](API_geoplaces_FoodType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** MapView **   <a name="location-Type-geoplaces_SearchTextResultItem-MapView"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** OpeningHours **   <a name="location-Type-geoplaces_SearchTextResultItem-OpeningHours"></a>
 List of opening hours objects. Not available in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [OpeningHours](API_geoplaces_OpeningHours.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Phonemes **   <a name="location-Type-geoplaces_SearchTextResultItem-Phonemes"></a>
How the various components of the result's address are pronounced in various languages.
Type: [PhonemeDetails](API_geoplaces_PhonemeDetails.md) object
Required: No

 ** PlaceAttributes **   <a name="location-Type-geoplaces_SearchTextResultItem-PlaceAttributes"></a>
A list of place attributes for the result, such as whether the business offers drive-through service.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `DriveThrough`
Required: No

 ** PoliticalView **   <a name="location-Type-geoplaces_SearchTextResultItem-PoliticalView"></a>
The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Position **   <a name="location-Type-geoplaces_SearchTextResultItem-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** TimeZone **   <a name="location-Type-geoplaces_SearchTextResultItem-TimeZone"></a>
The time zone in which the place is located.
Type: [TimeZone](API_geoplaces_TimeZone.md) object
Required: No

## See Also
<a name="API_geoplaces_SearchTextResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SearchTextResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SearchTextResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SearchTextResultItem)
