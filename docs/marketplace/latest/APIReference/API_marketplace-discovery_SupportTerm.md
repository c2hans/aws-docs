---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SupportTerm.html
---

# SupportTerm
<a name="API_marketplace-discovery_SupportTerm"></a>

Defines a support term that includes the refund policy for the offer.

## Contents
<a name="API_marketplace-discovery_SupportTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SupportTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** refundPolicy **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SupportTerm-refundPolicy"></a>
The refund policy description for the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SupportTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

## See Also
<a name="API_marketplace-discovery_SupportTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SupportTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SupportTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SupportTerm)
