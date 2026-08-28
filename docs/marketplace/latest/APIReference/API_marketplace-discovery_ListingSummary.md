---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListingSummary.html
---

# ListingSummary
<a name="API_marketplace-discovery_ListingSummary"></a>

Summary information about a listing returned by search operations, including the listing name, description, badges, categories, pricing models, reviews, and associated products.

## Contents
<a name="API_marketplace-discovery_ListingSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** associatedEntities **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-associatedEntities"></a>
The products associated with this listing.
Type: Array of [ListingSummaryAssociatedEntity](API_marketplace-discovery_ListingSummaryAssociatedEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** badges **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-badges"></a>
Badges indicating special attributes of the listing.
Type: Array of [ListingBadge](API_marketplace-discovery_ListingBadge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** catalog **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-catalog"></a>
The name of the catalog that the listing belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** categories **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-categories"></a>
The categories used to classify this listing into logical groups.
Type: Array of [Category](API_marketplace-discovery_Category.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: Yes

 ** fulfillmentOptionSummaries **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-fulfillmentOptionSummaries"></a>
A summary of fulfillment options available for the listing.
Type: Array of [FulfillmentOptionSummary](API_marketplace-discovery_FulfillmentOptionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** listingId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-listingId"></a>
The unique identifier of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** listingName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-listingName"></a>
The human-readable display name of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** logoThumbnailUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-logoThumbnailUrl"></a>
The URL of the logo thumbnail image for the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** pricingModels **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-pricingModels"></a>
The pricing models for offers associated with this listing.
Type: Array of [PricingModel](API_marketplace-discovery_PricingModel.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** pricingUnits **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-pricingUnits"></a>
The pricing units that define the billing dimensions for offers associated with this listing.
Type: Array of [PricingUnit](API_marketplace-discovery_PricingUnit.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** publisher **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-publisher"></a>
The entity who created and published the listing.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object
Required: Yes

 ** reviewSummary **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-reviewSummary"></a>
A summary of customer reviews for the listing.
Type: [ReviewSummary](API_marketplace-discovery_ReviewSummary.md) object
Required: Yes

 ** shortDescription **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingSummary-shortDescription"></a>
A 1–3 sentence summary describing the key aspects of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_ListingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListingSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
