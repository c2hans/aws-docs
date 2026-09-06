---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestResultItem.html
---

# SuggestResultItem
<a name="API_geoplaces_SuggestResultItem"></a>

The resulting item from the suggested query.

## Contents
<a name="API_geoplaces_SuggestResultItem_Contents"></a>

 ** SuggestResultItemType **   <a name="location-Type-geoplaces_SuggestResultItem-SuggestResultItemType"></a>
The result type. Place results represent the final result for a point of interest, Query results represent a follow up query which can be completed through the SearchText operation.
Type: String
Valid Values: `Place | Query`
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_SuggestResultItem-Title"></a>
The display title that should be used when presenting this option to the end user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** Highlights **   <a name="location-Type-geoplaces_SuggestResultItem-Highlights"></a>
Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms.
Type: [SuggestHighlights](API_geoplaces_SuggestHighlights.md) object
Required: No

 ** Place **   <a name="location-Type-geoplaces_SuggestResultItem-Place"></a>
The suggested place by its unique ID.
Type: [SuggestPlaceResult](API_geoplaces_SuggestPlaceResult.md) object
Required: No

 ** Query **   <a name="location-Type-geoplaces_SuggestResultItem-Query"></a>
The suggested query results.
Type: [SuggestQueryResult](API_geoplaces_SuggestQueryResult.md) object
Required: No

## See Also
<a name="API_geoplaces_SuggestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SuggestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SuggestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SuggestResultItem)
