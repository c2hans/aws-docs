---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ConfigurableUpfrontPricingTerm.html
---

# ConfigurableUpfrontPricingTerm
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTerm"></a>

Defines a prepaid payment model that allows buyers to configure the entitlements they want to purchase and the duration.

## Contents
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTerm-configuration"></a>
Additional parameters specified by the acceptor while accepting the term.
Type: [ConfigurableUpfrontPricingTermConfiguration](API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration.md) object
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTerm-currencyCode"></a>
Defines the currency for the prices mentioned in the term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** rateCards **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTerm-rateCards"></a>
A rate card defines the per unit rates for product dimensions.
Type: Array of [ConfigurableUpfrontRateCardItem](API_marketplace-agreements_ConfigurableUpfrontRateCardItem.md) objects
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ConfigurableUpfrontPricingTerm-type"></a>
Category of selector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_ConfigurableUpfrontPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ConfigurableUpfrontPricingTerm)
