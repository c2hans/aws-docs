---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_OfferSetInformation.html
---

# OfferSetInformation
<a name="API_marketplace-discovery_OfferSetInformation"></a>

Summary information about an offer set, including the identifier and seller of record.

## Contents
<a name="API_marketplace-discovery_OfferSetInformation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** offerSetId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferSetInformation-offerSetId"></a>
The unique identifier of the offer set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** sellerOfRecord **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferSetInformation-sellerOfRecord"></a>
The entity responsible for selling the products under this offer set.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object
Required: Yes

## See Also
<a name="API_marketplace-discovery_OfferSetInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/OfferSetInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/OfferSetInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/OfferSetInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
