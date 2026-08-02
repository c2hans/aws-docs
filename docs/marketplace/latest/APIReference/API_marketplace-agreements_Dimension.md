---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Dimension.html
---

# Dimension
<a name="API_marketplace-agreements_Dimension"></a>

Defines the dimensions that the acceptor has purchased from the overall set of dimensions presented in the rate card.

## Contents
<a name="API_marketplace-agreements_Dimension_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Dimension-dimensionKey"></a>
The name of key value of the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** dimensionValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Dimension-dimensionValue"></a>
The number of units of the dimension the acceptor has purchased.
For Agreements with `ConfigurableUpfrontPricingTerm`, the `RateCard` section will define the prices and dimensions defined by the seller (proposer), whereas the `Configuration` section will define the actual dimensions, prices, and units the buyer has chosen to accept.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_marketplace-agreements_Dimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Dimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Dimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Dimension)
