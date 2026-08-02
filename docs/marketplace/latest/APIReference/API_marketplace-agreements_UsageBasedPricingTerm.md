---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_UsageBasedPricingTerm.html
---

# UsageBasedPricingTerm
<a name="API_marketplace-agreements_UsageBasedPricingTerm"></a>

Defines a usage-based pricing model (typically, pay-as-you-go pricing), where the customers are charged based on product usage.

## Contents
<a name="API_marketplace-agreements_UsageBasedPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_UsageBasedPricingTerm-currencyCode"></a>
Defines the currency for the prices mentioned in the term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_UsageBasedPricingTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** rateCards **   <a name="AWSMarketplaceService-Type-marketplace-agreements_UsageBasedPricingTerm-rateCards"></a>
List of rate cards.
Type: Array of [UsageBasedRateCardItem](API_marketplace-agreements_UsageBasedRateCardItem.md) objects
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_UsageBasedPricingTerm-type"></a>
Category of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_UsageBasedPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/UsageBasedPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/UsageBasedPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/UsageBasedPricingTerm)
