---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchForSuggestionsResult.html
---

# SearchForSuggestionsResult
<a name="API_SearchForSuggestionsResult"></a>

Contains a place suggestion resulting from a place suggestion query that is run on a place index resource.

## Contents
<a name="API_SearchForSuggestionsResult_Contents"></a>

 ** Text **   <a name="location-Type-SearchForSuggestionsResult-Text"></a>
The text of the place suggestion, typically formatted as an address string.
Type: String
Required: Yes

 ** Categories **   <a name="location-Type-SearchForSuggestionsResult-Categories"></a>
The Amazon Location categories that describe the Place.
For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html), in the *Amazon Location Service developer guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

 ** PlaceId **   <a name="location-Type-SearchForSuggestionsResult-PlaceId"></a>
The unique identifier of the Place. You can use this with the `GetPlace` operation to find the place again later, or to get full information for the Place.
The `GetPlace` request must use the same `PlaceIndex` resource as the `SearchPlaceIndexForSuggestions` that generated the Place ID.
For `SearchPlaceIndexForSuggestions` operations, the `PlaceId` is returned by place indexes that use Esri, Grab, or HERE as data providers.
Type: String
Required: No

 ** SupplementalCategories **   <a name="location-Type-SearchForSuggestionsResult-SupplementalCategories"></a>
Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

## See Also
<a name="API_SearchForSuggestionsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchForSuggestionsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchForSuggestionsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchForSuggestionsResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
