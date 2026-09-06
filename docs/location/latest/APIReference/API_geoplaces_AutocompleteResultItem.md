---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteResultItem.html
---

# AutocompleteResultItem
<a name="API_geoplaces_AutocompleteResultItem"></a>

A result matching the input query text.

## Contents
<a name="API_geoplaces_AutocompleteResultItem_Contents"></a>

 ** PlaceId **   <a name="location-Type-geoplaces_AutocompleteResultItem-PlaceId"></a>
The PlaceId of the place associated with this result. This can be used to look up additional details about the result via GetPlace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** PlaceType **   <a name="location-Type-geoplaces_AutocompleteResultItem-PlaceType"></a>
PlaceType describes the type of result entry returned.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_AutocompleteResultItem-Title"></a>
A formatted string for display when presenting this result to an end user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** Address **   <a name="location-Type-geoplaces_AutocompleteResultItem-Address"></a>
The address associated with this result.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** Distance **   <a name="location-Type-geoplaces_AutocompleteResultItem-Distance"></a>
The distance in meters between the center of the search area and this result. Useful to evaluate how far away from the original bias position the result is.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** EstimatedPointAddress **   <a name="location-Type-geoplaces_AutocompleteResultItem-EstimatedPointAddress"></a>
If `true`, indicates that the coordinates of the position and access points of the point address are estimated.
Type: Boolean
Required: No

 ** Highlights **   <a name="location-Type-geoplaces_AutocompleteResultItem-Highlights"></a>
Indicates the starting and ending index of the place in the text query that match the found title.
Type: [AutocompleteHighlights](API_geoplaces_AutocompleteHighlights.md) object
Required: No

 ** Language **   <a name="location-Type-geoplaces_AutocompleteResultItem-Language"></a>
A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** PoliticalView **   <a name="location-Type-geoplaces_AutocompleteResultItem-PoliticalView"></a>
The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

## See Also
<a name="API_geoplaces_AutocompleteResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AutocompleteResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AutocompleteResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AutocompleteResultItem)
