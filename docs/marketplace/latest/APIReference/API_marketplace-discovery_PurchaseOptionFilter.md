---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PurchaseOptionFilter.html
---

# PurchaseOptionFilter

A filter used to narrow purchase option results by product, seller, type, visibility, or availability.

## Contents
<a name="API_marketplace-discovery_PurchaseOptionFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** filterType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionFilter-filterType"></a>
The type of filter to apply. This field has one of the following values:
AVAILABILITY\_STATUS
Filters by whether the purchase option is available or expired.
PRODUCT\_ID
Filters by product.
PURCHASE\_OPTION\_TYPE
Filters by offer or offer set.
SELLER\_OF\_RECORD\_PROFILE\_ID
Filters by seller.
VISIBILITY\_SCOPE
Filters by visibility.
See `filterValues` for the values that each type accepts.
Type: String
Valid Values: `PRODUCT_ID | SELLER_OF_RECORD_PROFILE_ID | PURCHASE_OPTION_TYPE | VISIBILITY_SCOPE | AVAILABILITY_STATUS`
Required: Yes

 ** filterValues **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionFilter-filterValues"></a>
The values to filter by. Supported values depend on `filterType`:
AVAILABILITY\_STATUS
One or more availability statuses to filter by: `AVAILABLE` or `EXPIRED`.
PRODUCT\_ID
One or more product identifiers to filter by.
PURCHASE\_OPTION\_TYPE
One or more purchase option types to filter by: `OFFER` or `OFFERSET`.
SELLER\_OF\_RECORD\_PROFILE\_ID
One or more seller profile identifiers to filter by.
VISIBILITY\_SCOPE
The visibility scope to filter by: `PRIVATE`.
To retrieve private offers and offer sets visible to you, use `VISIBILITY_SCOPE` with `PRIVATE`. Within one filter, a result matches if it has any of the values.
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
