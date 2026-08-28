---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GrantItem.html
---

# GrantItem
<a name="API_marketplace-discovery_GrantItem"></a>

An entitlement granted to the buyer as part of a pricing term.

## Contents
<a name="API_marketplace-discovery_GrantItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-dimensionKey"></a>
The machine-readable key identifying the entitlement dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-displayName"></a>
The human-readable name of the entitlement dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** unit **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-unit"></a>
The unit of measurement for the entitlement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-description"></a>
A description of the entitlement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** dimensionLabels **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-dimensionLabels"></a>
Labels used to categorize this entitlement, such as by region.
Type: Array of [DimensionLabel](API_marketplace-discovery_DimensionLabel.md) objects
Required: No

 ** maxQuantity **   <a name="AWSMarketplaceService-Type-marketplace-discovery_GrantItem-maxQuantity"></a>
The maximum quantity of the entitlement that can be granted.
Type: Integer
Required: No

## See Also
<a name="API_marketplace-discovery_GrantItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GrantItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GrantItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GrantItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
