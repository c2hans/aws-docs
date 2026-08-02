---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ConfigurableUpfrontRateCardItem.html
---

# ConfigurableUpfrontRateCardItem
<a name="API_marketplace-discovery_ConfigurableUpfrontRateCardItem"></a>

A rate card item within a configurable upfront pricing term, including a selector for choosing the configuration and per-unit rates.

## Contents
<a name="API_marketplace-discovery_ConfigurableUpfrontRateCardItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** constraints **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontRateCardItem-constraints"></a>
Constraints on how the buyer can configure this rate card, such as whether multiple dimensions can be selected.
Type: [Constraints](API_marketplace-discovery_Constraints.md) object
Required: Yes

 ** rateCard **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontRateCardItem-rateCard"></a>
The per-unit rates for this configuration.
Type: Array of [RateCardItem](API_marketplace-discovery_RateCardItem.md) objects
Required: Yes

 ** selector **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontRateCardItem-selector"></a>
The selector criteria for this rate card, such as duration.
Type: [Selector](API_marketplace-discovery_Selector.md) object
Required: Yes

## See Also
<a name="API_marketplace-discovery_ConfigurableUpfrontRateCardItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ConfigurableUpfrontRateCardItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ConfigurableUpfrontRateCardItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ConfigurableUpfrontRateCardItem)
