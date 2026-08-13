---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ValidityTerm.html
---

# ValidityTerm
<a name="API_marketplace-discovery_ValidityTerm"></a>

Defines a validity term that specifies the duration or date range of an agreement.

## Contents
<a name="API_marketplace-discovery_ValidityTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ValidityTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ValidityTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm | NetPaymentTerm`
Required: Yes

 ** agreementDuration **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ValidityTerm-agreementDuration"></a>
The duration of the agreement, in ISO 8601 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** agreementEndDate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ValidityTerm-agreementEndDate"></a>
The date when the agreement ends.
Type: Timestamp
Required: No

 ** agreementStartDate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ValidityTerm-agreementStartDate"></a>
The date when the agreement starts.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-discovery_ValidityTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ValidityTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ValidityTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ValidityTerm)
