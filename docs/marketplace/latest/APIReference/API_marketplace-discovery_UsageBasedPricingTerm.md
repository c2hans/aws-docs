---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_UsageBasedPricingTerm.html
---

# UsageBasedPricingTerm
<a name="API_marketplace-discovery_UsageBasedPricingTerm"></a>

Defines a usage-based pricing term (typically pay-as-you-go), where buyers are charged based on product usage.

## Contents
<a name="API_marketplace-discovery_UsageBasedPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-discovery_UsageBasedPricingTerm-currencyCode"></a>
Defines the currency for the prices in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_UsageBasedPricingTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** rateCards **   <a name="AWSMarketplaceService-Type-marketplace-discovery_UsageBasedPricingTerm-rateCards"></a>
The rate cards containing per-unit rates for usage-based pricing.
Type: Array of [UsageBasedRateCardItem](API_marketplace-discovery_UsageBasedRateCardItem.md) objects
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_UsageBasedPricingTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

## See Also
<a name="API_marketplace-discovery_UsageBasedPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/UsageBasedPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/UsageBasedPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/UsageBasedPricingTerm)
