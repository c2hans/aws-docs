---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListingFacet.html
---

# ListingFacet
<a name="API_marketplace-discovery_ListingFacet"></a>

A facet value with display information and a count of matching listings. Used to build filter and browse experiences.

## Contents
<a name="API_marketplace-discovery_ListingFacet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** count **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingFacet-count"></a>
The number of listings matching this facet value.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingFacet-displayName"></a>
The human-readable name of the facet value, suitable for display in a user interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingFacet-value"></a>
The internal value used for filtering when passed back in a search filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** parent **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingFacet-parent"></a>
The parent facet value for hierarchical facets, such as subcategories.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_ListingFacet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListingFacet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListingFacet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListingFacet)
