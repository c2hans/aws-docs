---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_LegalTerm.html
---

# LegalTerm
<a name="API_marketplace-discovery_LegalTerm"></a>

Defines a legal term containing documents proposed to buyers, such as EULAs and data subscription agreements.

## Contents
<a name="API_marketplace-discovery_LegalTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** documents **   <a name="AWSMarketplaceService-Type-marketplace-discovery_LegalTerm-documents"></a>
The legal documents proposed to the buyer as part of this term.
Type: Array of [DocumentItem](API_marketplace-discovery_DocumentItem.md) objects
Required: Yes

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_LegalTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_LegalTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm`
Required: Yes

## See Also
<a name="API_marketplace-discovery_LegalTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/LegalTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/LegalTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/LegalTerm)
