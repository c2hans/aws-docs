---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_FreeTrialPricingTerm.html
---

# FreeTrialPricingTerm
<a name="API_marketplace-discovery_FreeTrialPricingTerm"></a>

Defines a free trial pricing term that enables customers to try the product before purchasing.

## Contents
<a name="API_marketplace-discovery_FreeTrialPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** grants **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FreeTrialPricingTerm-grants"></a>
The entitlements granted to the buyer during the free trial.
Type: Array of [GrantItem](API_marketplace-discovery_GrantItem.md) objects
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FreeTrialPricingTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FreeTrialPricingTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

 ** duration **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FreeTrialPricingTerm-duration"></a>
The duration of the free trial period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-discovery_FreeTrialPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/FreeTrialPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/FreeTrialPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/FreeTrialPricingTerm)
