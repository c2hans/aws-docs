---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PriceIncrease.html
---

# PriceIncrease
<a name="API_marketplace-discovery_PriceIncrease"></a>

The pricing adjustment that applies at each renewal cycle, expressed as either a fixed percentage or a percentage range. Exactly one variant is present.

## Contents
<a name="API_marketplace-discovery_PriceIncrease_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fixedPercentage **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PriceIncrease-fixedPercentage"></a>
A single fixed percentage applied uniformly at every renewal cycle.
Type: [FixedPercentage](API_marketplace-discovery_FixedPercentage.md) object
Required: No

 ** percentageRange **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PriceIncrease-percentageRange"></a>
A percentage band with minimum, maximum, and default values that bound the price increase at each renewal cycle.
Type: [PercentageRange](API_marketplace-discovery_PercentageRange.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_PriceIncrease_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PriceIncrease)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PriceIncrease)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PriceIncrease)
