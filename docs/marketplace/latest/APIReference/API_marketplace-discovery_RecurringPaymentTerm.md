---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_RecurringPaymentTerm.html
---

# RecurringPaymentTerm
<a name="API_marketplace-discovery_RecurringPaymentTerm"></a>

Defines a recurring payment term with fixed charges at regular billing intervals.

## Contents
<a name="API_marketplace-discovery_RecurringPaymentTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** billingPeriod **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RecurringPaymentTerm-billingPeriod"></a>
The billing period frequency, such as `Monthly`.
Type: String
Valid Values: `Monthly`
Required: Yes

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RecurringPaymentTerm-currencyCode"></a>
Defines the currency for the prices in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RecurringPaymentTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RecurringPaymentTerm-price"></a>
The amount charged each billing period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RecurringPaymentTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm | NetPaymentTerm`
Required: Yes

## See Also
<a name="API_marketplace-discovery_RecurringPaymentTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/RecurringPaymentTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/RecurringPaymentTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/RecurringPaymentTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
