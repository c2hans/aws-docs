---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PriceIncrease.html
---

# PriceIncrease
<a name="API_marketplace-agreements_PriceIncrease"></a>

The price increase that is applied each time the agreement renews. Exactly one of the following fields is set.

## Contents
<a name="API_marketplace-agreements_PriceIncrease_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fixedPercentage **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PriceIncrease-fixedPercentage"></a>
A fixed price increase percentage that is applied at each renewal.
Type: [FixedPercentage](API_marketplace-agreements_FixedPercentage.md) object
Required: No

 ** percentageRange **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PriceIncrease-percentageRange"></a>
A range of price increase percentages that the proposer can choose from before the adjustment deadline of the agreement.
Type: [PercentageRange](API_marketplace-agreements_PercentageRange.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_PriceIncrease_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PriceIncrease)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PriceIncrease)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PriceIncrease)
