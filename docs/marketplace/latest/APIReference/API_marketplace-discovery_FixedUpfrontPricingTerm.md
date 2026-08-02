---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_FixedUpfrontPricingTerm.html
---

# FixedUpfrontPricingTerm
<a name="API_marketplace-discovery_FixedUpfrontPricingTerm"></a>

Defines a fixed upfront pricing term with a pre-paid amount and granted entitlements.

## Contents
<a name="API_marketplace-discovery_FixedUpfrontPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-currencyCode"></a>
Defines the currency for the prices in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** grants **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-grants"></a>
The entitlements granted to the buyer as part of this term.
Type: Array of [GrantItem](API_marketplace-discovery_GrantItem.md) objects
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-price"></a>
The price charged upfront for this term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

 ** duration **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FixedUpfrontPricingTerm-duration"></a>
The duration of the fixed pricing term, in ISO 8601 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-discovery_FixedUpfrontPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/FixedUpfrontPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/FixedUpfrontPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/FixedUpfrontPricingTerm)
