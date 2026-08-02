---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ConfigurableUpfrontPricingTerm.html
---

# ConfigurableUpfrontPricingTerm
<a name="API_marketplace-discovery_ConfigurableUpfrontPricingTerm"></a>

Defines a configurable upfront pricing term with selectable rate cards, where buyers choose from predefined pricing configurations.

## Contents
<a name="API_marketplace-discovery_ConfigurableUpfrontPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontPricingTerm-currencyCode"></a>
Defines the currency for the prices in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontPricingTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontPricingTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

 ** rateCards **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ConfigurableUpfrontPricingTerm-rateCards"></a>
The rate cards available for selection, each with a selector, constraints, and per-unit rates.
Type: Array of [ConfigurableUpfrontRateCardItem](API_marketplace-discovery_ConfigurableUpfrontRateCardItem.md) objects
Required: No

## See Also
<a name="API_marketplace-discovery_ConfigurableUpfrontPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ConfigurableUpfrontPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ConfigurableUpfrontPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ConfigurableUpfrontPricingTerm)
