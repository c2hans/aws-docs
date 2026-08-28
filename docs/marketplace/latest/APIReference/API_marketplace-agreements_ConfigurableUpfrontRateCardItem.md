---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ConfigurableUpfrontRateCardItem.html
---

# ConfigurableUpfrontRateCardItem
<a name="API_marketplace-agreements_ConfigurableUpfrontRateCardItem"></a>

Within the prepaid payment model defined under `ConfigurableUpfrontPricingTerm`, the `RateCardItem` defines all the various rate cards (including pricing and dimensions) that have been proposed.

## Contents
<a name="API_marketplace-agreements_ConfigurableUpfrontRateCardItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** constraints **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontRateCardItem-constraints"></a>
Defines limits on how the term can be configured by acceptors.
Type: [Constraints](API_marketplace-agreements_Constraints.md) object
Required: No

 ** rateCard **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontRateCardItem-rateCard"></a>
Defines the per unit rates for product dimensions.
Type: Array of [RateCardItem](API_marketplace-agreements_RateCardItem.md) objects
Required: No

 ** selector **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontRateCardItem-selector"></a>
Differentiates between the mutually exclusive rate cards in the same pricing term to be selected by the buyer.
Type: [Selector](API_marketplace-agreements_Selector.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_ConfigurableUpfrontRateCardItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ConfigurableUpfrontRateCardItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ConfigurableUpfrontRateCardItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ConfigurableUpfrontRateCardItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
