---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchFilter.html
---

# SearchFilter

A filter used to narrow search results by attribute, such as category, pricing model, or fulfillment type.

## Contents
<a name="API_marketplace-discovery_SearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** filterType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SearchFilter-filterType"></a>
The type of filter to apply. See `filterValues` for the supported types and their values.
Type: String
Valid Values: `MIN_AVERAGE_CUSTOMER_RATING | MAX_AVERAGE_CUSTOMER_RATING | CATEGORY | PUBLISHER | FULFILLMENT_OPTION_TYPE | PRICING_MODEL | PRICING_UNIT | DEPLOYED_ON_AWS | NUMBER_OF_PRODUCTS | CERTIFICATES | PRODUCT_ID | SPECIALIZATION | SPECIALIZATION_CATEGORY | SELLER_ENGAGEMENT | TRUST_CENTER`
Required: Yes

 ** filterValues **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SearchFilter-filterValues"></a>
The values to filter by. Term filters accept multiple values, and a result matches if it has any of them. Range filters accept a single value. The supported values for each `filterType` are as follows:
CATEGORY
One or more category identifiers. Matches listings in those categories.
CERTIFICATES
One or more certification identifiers, such as `ISO_27001` or `SOC2_TYPE_2`. Matches listings that hold those certifications.
DEPLOYED\_ON\_AWS
The single value `DEPLOYED_ON_AWS`. Matches listings whose products are deployed on AWS infrastructure.
FULFILLMENT\_OPTION\_TYPE
One or more fulfillment option types, such as `SAAS`, `AMAZON_MACHINE_IMAGE`, or `CONTAINER`. Matches listings that you can deploy or access in those ways.
MAX\_AVERAGE\_CUSTOMER\_RATING
A single rating between `0.0` and `5.0`. Matches listings whose average customer rating is at or below that value.
MIN\_AVERAGE\_CUSTOMER\_RATING
A single rating between `0.0` and `5.0`. Matches listings whose average customer rating is at or above that value.
NUMBER\_OF\_PRODUCTS
 `SINGLE_PRODUCT` or `MULTI_PRODUCT`. Matches single-product listings or multi-product solutions.
PRICING\_MODEL
One or more of `BYOL`, `CONTRACT`, `FREE`, and `USAGE`. Matches listings with offers that use those pricing models.
PRICING\_UNIT
One or more pricing units, such as `USERS`, `HOSTS`, or `REQUESTS`. Matches listings that bill by those units.
PRODUCT\_ID
One or more product identifiers. Matches listings that contain those products.
PUBLISHER
One or more publisher identifiers. Matches listings from those sellers.
SELLER\_ENGAGEMENT
One or more `SellerEngagementType` values, such as `BUY_NOW` or `REQUEST_FOR_DEMO`. Matches listings that offer those ways to engage with the seller.
SPECIALIZATION
One or more specialization identifiers. Matches listings that earned those specializations.
SPECIALIZATION\_CATEGORY
One or more specialization category identifiers. Matches listings that earned a category under a specialization.
TRUST\_CENTER
The single value `HAS_TRUST_CENTER`. Matches listings that have a trust center.
Use `SearchFacets` to retrieve the values available for `CATEGORY`, `PUBLISHER`, `CERTIFICATES`, `SPECIALIZATION`, and `SPECIALIZATION_CATEGORY`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\-\.]+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_SearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SearchFilter)
