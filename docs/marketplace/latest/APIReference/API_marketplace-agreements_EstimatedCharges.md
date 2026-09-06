---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_EstimatedCharges.html
---

# EstimatedCharges
<a name="API_marketplace-agreements_EstimatedCharges"></a>

Estimated cost of the agreement.

## Contents
<a name="API_marketplace-agreements_EstimatedCharges_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EstimatedCharges-agreementValue"></a>
The total known amount customer has to pay across the lifecycle of the agreement.
This is the total contract value if accepted terms contain `ConfigurableUpfrontPricingTerm` or `FixedUpfrontPricingTerm`. In the case of pure contract pricing, this will be the total value of the contract. In the case of contracts with consumption pricing, this will only include the committed value and not include any overages that occur.
If the accepted terms contain `PaymentScheduleTerm`, it will be the total payment schedule amount. This occurs when flexible payment schedule is used, and is the sum of all invoice charges in the payment schedule.
In case a customer has amended an agreement, by purchasing more units of any dimension, this will include both the original cost as well as the added cost incurred due to addition of new units.
This is `0` if the accepted terms contain `UsageBasedPricingTerm` without `ConfigurableUpfrontPricingTerm` or `RecurringPaymentTerm`. This occurs for usage-based pricing (such as SaaS metered or AMI/container hourly or monthly), because the exact usage is not known upfront.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EstimatedCharges-currencyCode"></a>
Defines the currency code for the charge.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_EstimatedCharges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/EstimatedCharges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/EstimatedCharges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/EstimatedCharges)
