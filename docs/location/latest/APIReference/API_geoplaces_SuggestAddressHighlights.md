---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestAddressHighlights.html
---

# SuggestAddressHighlights
<a name="API_geoplaces_SuggestAddressHighlights"></a>

Describes how the parts of the textQuery matched the input query by returning the sections of the response which matched to textQuery terms.

## Contents
<a name="API_geoplaces_SuggestAddressHighlights_Contents"></a>

 ** Label **   <a name="location-Type-geoplaces_SuggestAddressHighlights-Label"></a>
Indicates the starting and ending indexes of the places in the result which were identified to match the textQuery. This result is useful for providing emphasis to results where the user query directly matched to make selecting the correct result from a list easier for an end user.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_geoplaces_SuggestAddressHighlights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SuggestAddressHighlights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SuggestAddressHighlights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SuggestAddressHighlights)
