---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PurchaseOptionFilter.html
---

# PurchaseOptionFilter
<a name="API_marketplace-discovery_PurchaseOptionFilter"></a>

A filter used to narrow purchase option results by product, seller, type, visibility, or availability.

## Contents
<a name="API_marketplace-discovery_PurchaseOptionFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** filterType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionFilter-filterType"></a>
The type of filter to apply, such as `PRODUCT_ID`, `VISIBILITY_SCOPE`, or `PURCHASE_OPTION_TYPE`.
Type: String
Valid Values: `PRODUCT_ID | SELLER_OF_RECORD_PROFILE_ID | PURCHASE_OPTION_TYPE | VISIBILITY_SCOPE | AVAILABILITY_STATUS`
Required: Yes

 ** filterValues **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionFilter-filterValues"></a>
The values to filter by. Supported values depend on `filterType`:
+  `PRODUCT_ID` – One or more product identifiers to filter by.
+  `SELLER_OF_RECORD_PROFILE_ID` – One or more seller profile identifiers to filter by.
+  `PURCHASE_OPTION_TYPE` – One or more purchase option types to filter by: `OFFER` or `OFFERSET`.
+  `VISIBILITY_SCOPE` – The visibility scope to filter by: `PRIVATE`.
+  `AVAILABILITY_STATUS` – One or more availability statuses to filter by: `AVAILABLE` or `EXPIRED`.
To retrieve private offers and offer sets visible to you, use `VISIBILITY_SCOPE` with `PRIVATE`. OR logic combines multiple values within the same filter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_PurchaseOptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PurchaseOptionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PurchaseOptionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PurchaseOptionFilter)
