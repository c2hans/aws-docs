---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration.html
---

# ConfigurableUpfrontPricingTermConfiguration
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration"></a>

Defines a prepaid payment model that allows buyers to configure the entitlements they want to purchase and the duration.

## Contents
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensions **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration-dimensions"></a>
Defines the dimensions that the acceptor has purchased from the overall set of dimensions presented in the rate card.
Type: Array of [Dimension](API_marketplace-agreements_Dimension.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** selectorValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration-selectorValue"></a>
Defines the length of time for which the particular pricing/dimension is being purchased by the acceptor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

## See Also
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTermConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTermConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTermConfiguration)
