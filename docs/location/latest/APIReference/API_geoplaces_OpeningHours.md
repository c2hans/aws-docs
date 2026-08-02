---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_OpeningHours.html
---

# OpeningHours
<a name="API_geoplaces_OpeningHours"></a>

List of opening hours objects.

## Contents
<a name="API_geoplaces_OpeningHours_Contents"></a>

 ** Categories **   <a name="location-Type-geoplaces_OpeningHours-Categories"></a>
Categories of results that results must belong too.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Components **   <a name="location-Type-geoplaces_OpeningHours-Components"></a>
Components of the opening hours object.
Type: Array of [OpeningHoursComponents](API_geoplaces_OpeningHoursComponents.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Display **   <a name="location-Type-geoplaces_OpeningHours-Display"></a>
List of opening hours in the format they are displayed in. This can vary by result and in most cases represents how the result uniquely formats their opening hours.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** OpenNow **   <a name="location-Type-geoplaces_OpeningHours-OpenNow"></a>
Boolean which indicates if the result/place is currently open.
Type: Boolean
Required: No

## See Also
<a name="API_geoplaces_OpeningHours_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/OpeningHours)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/OpeningHours)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/OpeningHours)
