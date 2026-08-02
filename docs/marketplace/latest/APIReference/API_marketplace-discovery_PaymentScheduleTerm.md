---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PaymentScheduleTerm.html
---

# PaymentScheduleTerm
<a name="API_marketplace-discovery_PaymentScheduleTerm"></a>

Defines a payment schedule term with installment payments at specified dates.

## Contents
<a name="API_marketplace-discovery_PaymentScheduleTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleTerm-currencyCode"></a>
Defines the currency for the prices in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** schedule **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleTerm-schedule"></a>
The payment schedule installments, each with a charge date and amount.
Type: Array of [ScheduleItem](API_marketplace-discovery_ScheduleItem.md) objects
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PaymentScheduleTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

## See Also
<a name="API_marketplace-discovery_PaymentScheduleTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PaymentScheduleTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PaymentScheduleTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PaymentScheduleTerm)
