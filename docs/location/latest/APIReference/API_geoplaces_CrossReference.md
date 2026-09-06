---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_CrossReference.html
---

# CrossReference
<a name="API_geoplaces_CrossReference"></a>

A reference to a third-party supplier's identifier for a place, enabling correlation of places across external systems.

## Contents
<a name="API_geoplaces_CrossReference_Contents"></a>

 ** Source **   <a name="location-Type-geoplaces_CrossReference-Source"></a>
The name of the third-party data supplier (for example, `Yelp` or `TripAdvisor`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** SourcePlaceId **   <a name="location-Type-geoplaces_CrossReference-SourcePlaceId"></a>
The place identifier assigned by the third-party supplier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** SourceCategories **   <a name="location-Type-geoplaces_CrossReference-SourceCategories"></a>
The list of place category identifiers this supplier reference relates to.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_geoplaces_CrossReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/CrossReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/CrossReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/CrossReference)
