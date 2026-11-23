---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_OfferTerm.html
---

# OfferTerm

A term attached to an offer. Each element contains exactly one term type, such as a pricing term, legal term, or payment schedule term.

## Contents
<a name="API_marketplace-discovery_OfferTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** byolPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-byolPricingTerm"></a>
Describes a Bring Your Own License (BYOL) pricing term. With this term, you use your existing license for the product.
Type: [ByolPricingTerm](API_marketplace-discovery_ByolPricingTerm.md) object
Required: No

 ** configurableUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-configurableUpfrontPricingTerm"></a>
Describes a configurable upfront pricing term with selectable rate cards. You choose from predefined pricing configurations.
Type: [ConfigurableUpfrontPricingTerm](API_marketplace-discovery_ConfigurableUpfrontPricingTerm.md) object
Required: No

 ** fixedUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-fixedUpfrontPricingTerm"></a>
Describes a fixed upfront pricing term with a pre-paid amount and granted entitlements.
Type: [FixedUpfrontPricingTerm](API_marketplace-discovery_FixedUpfrontPricingTerm.md) object
Required: No

 ** freeTrialPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-freeTrialPricingTerm"></a>
Describes a free trial pricing term. With this term, you can try the product before you purchase it.
Type: [FreeTrialPricingTerm](API_marketplace-discovery_FreeTrialPricingTerm.md) object
Required: No

 ** legalTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-legalTerm"></a>
Describes a legal term containing documents proposed to you, such as End User License Agreements (EULAs) and data subscription agreements.
Type: [LegalTerm](API_marketplace-discovery_LegalTerm.md) object
Required: No

 ** netPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-netPaymentTerm"></a>
A net payment term.
Type: [NetPaymentTerm](API_marketplace-discovery_NetPaymentTerm.md) object
Required: No

 ** paymentScheduleTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-paymentScheduleTerm"></a>
Describes a payment schedule term with installment payments at specified dates.
Type: [PaymentScheduleTerm](API_marketplace-discovery_PaymentScheduleTerm.md) object
Required: No

 ** recurringPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-recurringPaymentTerm"></a>
Describes a recurring payment term with fixed charges at regular billing intervals.
Type: [RecurringPaymentTerm](API_marketplace-discovery_RecurringPaymentTerm.md) object
Required: No

 ** renewalTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-renewalTerm"></a>
Describes a renewal term that renews the agreement automatically.
Type: [RenewalTerm](API_marketplace-discovery_RenewalTerm.md) object
Required: No

 ** supportTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-supportTerm"></a>
Describes a support term that includes the refund policy for the offer.
Type: [SupportTerm](API_marketplace-discovery_SupportTerm.md) object
Required: No

 ** usageBasedPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-usageBasedPricingTerm"></a>
Describes a usage-based pricing term, typically pay-as-you-go. You are charged based on your use of the product.
Type: [UsageBasedPricingTerm](API_marketplace-discovery_UsageBasedPricingTerm.md) object
Required: No

 ** validityTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-validityTerm"></a>
Describes a validity term that specifies the duration or date range of an agreement.
Type: [ValidityTerm](API_marketplace-discovery_ValidityTerm.md) object
Required: No

 ** variablePaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-variablePaymentTerm"></a>
Describes a variable payment term with a maximum total charge amount.
Type: [VariablePaymentTerm](API_marketplace-discovery_VariablePaymentTerm.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_OfferTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/OfferTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/OfferTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/OfferTerm)
