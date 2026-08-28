---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PurchaseOptionSummary.html
---

# PurchaseOptionSummary
<a name="API_marketplace-discovery_PurchaseOptionSummary"></a>

Summary information about a purchase option (offer or offer set) available to the buyer, including the seller, badges, and associated products.

## Contents
<a name="API_marketplace-discovery_PurchaseOptionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** associatedEntities **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-associatedEntities"></a>
The products, offers, and offer sets associated with this purchase option.
Type: Array of [PurchaseOptionAssociatedEntity](API_marketplace-discovery_PurchaseOptionAssociatedEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** catalog **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-catalog"></a>
The name of the catalog that the purchase option belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** purchaseOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-purchaseOptionId"></a>
The unique identifier of the purchase option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** purchaseOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-purchaseOptionType"></a>
The type of purchase option. Values are `OFFER` for a single-product offer or `OFFERSET` for a bundled offer set.
Type: String
Valid Values: `OFFER | OFFERSET`
Required: Yes

 ** sellerOfRecord **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-sellerOfRecord"></a>
The entity responsible for selling the product under this purchase option.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object
Required: Yes

 ** availableFromTime **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-availableFromTime"></a>
The date and time when the purchase option became available to the buyer.
Type: Timestamp
Required: No

 ** badges **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-badges"></a>
Badges indicating special attributes of the purchase option, such as private pricing or future dated.
Type: Array of [PurchaseOptionBadge](API_marketplace-discovery_PurchaseOptionBadge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** expirationTime **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-expirationTime"></a>
The date and time when the purchase option expires and is no longer available for procurement.
Type: Timestamp
Required: No

 ** purchaseOptionName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionSummary-purchaseOptionName"></a>
The display name of the purchase option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_marketplace-discovery_PurchaseOptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PurchaseOptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PurchaseOptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PurchaseOptionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
