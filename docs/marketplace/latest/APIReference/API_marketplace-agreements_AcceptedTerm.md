---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptedTerm.html
---

# AcceptedTerm
<a name="API_marketplace-agreements_AcceptedTerm"></a>

A subset of terms proposed by the proposer, which have been accepted by the acceptor as part of agreement creation.

## Contents
<a name="API_marketplace-agreements_AcceptedTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** byolPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-byolPricingTerm"></a>
Enables you and your customers to move your existing agreements to AWS Marketplace. The customer won't be charged for product usage in AWS Marketplace because they already paid for the product outside of AWS Marketplace.
Type: [ByolPricingTerm](API_marketplace-agreements_ByolPricingTerm.md) object
Required: No

 ** configurableUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-configurableUpfrontPricingTerm"></a>
Defines a prepaid payment model that allows buyers to configure the entitlements they want to purchase and the duration.
Type: [ConfigurableUpfrontPricingTerm](API_marketplace-agreements_ConfigurableUpfrontPricingTerm.md) object
Required: No

 ** fixedUpfrontPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-fixedUpfrontPricingTerm"></a>
Defines a pre-paid pricing model where the customers are charged a fixed upfront amount.
Type: [FixedUpfrontPricingTerm](API_marketplace-agreements_FixedUpfrontPricingTerm.md) object
Required: No

 ** freeTrialPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-freeTrialPricingTerm"></a>
Defines a short-term free pricing model where the buyers aren’t charged anything within a specified limit.
Type: [FreeTrialPricingTerm](API_marketplace-agreements_FreeTrialPricingTerm.md) object
Required: No

 ** legalTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-legalTerm"></a>
Defines the list of text agreements proposed to the acceptors. An example is the end user license agreement (EULA).
Type: [LegalTerm](API_marketplace-agreements_LegalTerm.md) object
Required: No

 ** netPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-netPaymentTerm"></a>
Defines the net payment due period for the agreement, specifying when payment is due after an invoice is issued.
Type: [NetPaymentTerm](API_marketplace-agreements_NetPaymentTerm.md) object
Required: No

 ** paymentScheduleTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-paymentScheduleTerm"></a>
Defines an installment-based pricing model where customers are charged a fixed price on different dates during the agreement validity period. This is used most commonly for flexible payment schedule pricing.
Type: [PaymentScheduleTerm](API_marketplace-agreements_PaymentScheduleTerm.md) object
Required: No

 ** recurringPaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-recurringPaymentTerm"></a>
Defines a pricing model where customers are charged a fixed recurring price at the end of each billing period.
Type: [RecurringPaymentTerm](API_marketplace-agreements_RecurringPaymentTerm.md) object
Required: No

 ** renewalTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-renewalTerm"></a>
Defines that on graceful expiration of the agreement (when the agreement ends on its pre-defined end date), a new agreement will be created using the accepted terms on the existing agreement. In other words, the agreement will be renewed. Presence of `RenewalTerm` in the offer document means that auto-renewal is allowed. Buyers will have the option to accept or decline auto-renewal at the offer acceptance/agreement creation. Buyers can also change this flag from `True` to `False` or `False` to `True` at anytime during the agreement's lifecycle.
Type: [RenewalTerm](API_marketplace-agreements_RenewalTerm.md) object
Required: No

 ** supportTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-supportTerm"></a>
Defines the customer support available for the acceptors when they purchase the software.
Type: [SupportTerm](API_marketplace-agreements_SupportTerm.md) object
Required: No

 ** usageBasedPricingTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-usageBasedPricingTerm"></a>
Defines a usage-based pricing model (typically, pay-as-you-go pricing), where the customers are charged based on product usage.
Type: [UsageBasedPricingTerm](API_marketplace-agreements_UsageBasedPricingTerm.md) object
Required: No

 ** validityTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-validityTerm"></a>
Defines the conditions that will keep an agreement created from this offer valid.
Type: [ValidityTerm](API_marketplace-agreements_ValidityTerm.md) object
Required: No

 ** variablePaymentTerm **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AcceptedTerm-variablePaymentTerm"></a>
Defines a payment model where sellers can submit variable payment requests up to a maximum charge amount, with configurable approval strategies and expiration timelines.
Type: [VariablePaymentTerm](API_marketplace-agreements_VariablePaymentTerm.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_AcceptedTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AcceptedTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AcceptedTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AcceptedTerm)
