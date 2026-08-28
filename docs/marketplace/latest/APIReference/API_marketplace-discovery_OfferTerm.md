---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_OfferTerm.html
---

# OfferTerm
<a name="API_marketplace-discovery_OfferTerm"></a>

A term attached to an offer. Each element contains exactly one term type, such as a pricing term, legal term, or payment schedule term.

## Contents
<a name="API_marketplace-discovery_OfferTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** byolPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-byolPricingTerm"></a>
Defines a Bring Your Own License (BYOL) pricing term, where buyers use their existing license for the product.
Type: [ByolPricingTerm](API_marketplace-discovery_ByolPricingTerm.md) object
Required: No

 ** configurableUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-configurableUpfrontPricingTerm"></a>
Defines a configurable upfront pricing term with selectable rate cards, where buyers choose from predefined pricing configurations.
Type: [ConfigurableUpfrontPricingTerm](API_marketplace-discovery_ConfigurableUpfrontPricingTerm.md) object
Required: No

 ** fixedUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-fixedUpfrontPricingTerm"></a>
Defines a fixed upfront pricing term with a pre-paid amount and granted entitlements.
Type: [FixedUpfrontPricingTerm](API_marketplace-discovery_FixedUpfrontPricingTerm.md) object
Required: No

 ** freeTrialPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-freeTrialPricingTerm"></a>
Defines a free trial pricing term that enables customers to try the product before purchasing.
Type: [FreeTrialPricingTerm](API_marketplace-discovery_FreeTrialPricingTerm.md) object
Required: No

 ** legalTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-legalTerm"></a>
Defines a legal term containing documents proposed to buyers, such as EULAs and data subscription agreements.
Type: [LegalTerm](API_marketplace-discovery_LegalTerm.md) object
Required: No

 ** netPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-netPaymentTerm"></a>
A net payment term.
Type: [NetPaymentTerm](API_marketplace-discovery_NetPaymentTerm.md) object
Required: No

 ** paymentScheduleTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-paymentScheduleTerm"></a>
Defines a payment schedule term with installment payments at specified dates.
Type: [PaymentScheduleTerm](API_marketplace-discovery_PaymentScheduleTerm.md) object
Required: No

 ** recurringPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-recurringPaymentTerm"></a>
Defines a recurring payment term with fixed charges at regular billing intervals.
Type: [RecurringPaymentTerm](API_marketplace-discovery_RecurringPaymentTerm.md) object
Required: No

 ** renewalTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-renewalTerm"></a>
Defines a renewal term that enables automatic agreement renewal.
Type: [RenewalTerm](API_marketplace-discovery_RenewalTerm.md) object
Required: No

 ** supportTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-supportTerm"></a>
Defines a support term that includes the refund policy for the offer.
Type: [SupportTerm](API_marketplace-discovery_SupportTerm.md) object
Required: No

 ** usageBasedPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-usageBasedPricingTerm"></a>
Defines a usage-based pricing term (typically pay-as-you-go), where buyers are charged based on product usage.
Type: [UsageBasedPricingTerm](API_marketplace-discovery_UsageBasedPricingTerm.md) object
Required: No

 ** validityTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-validityTerm"></a>
Defines a validity term that specifies the duration or date range of an agreement.
Type: [ValidityTerm](API_marketplace-discovery_ValidityTerm.md) object
Required: No

 ** variablePaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferTerm-variablePaymentTerm"></a>
Defines a variable payment term with a maximum total charge amount.
Type: [VariablePaymentTerm](API_marketplace-discovery_VariablePaymentTerm.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_OfferTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/OfferTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/OfferTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/OfferTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
