---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_RenewalTerm.html
---

# RenewalTerm
<a name="API_marketplace-discovery_RenewalTerm"></a>

Defines a renewal term that enables automatic agreement renewal.

## Contents
<a name="API_marketplace-discovery_RenewalTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-id"></a>
The unique identifier of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-type"></a>
The category of the term.
Type: String
Valid Values: `ByolPricingTerm | ConfigurableUpfrontPricingTerm | FixedUpfrontPricingTerm | UsageBasedPricingTerm | FreeTrialPricingTerm | LegalTerm | PaymentScheduleTerm | RecurringPaymentTerm | RenewalTerm | SupportTerm | ValidityTerm | VariablePaymentTerm | NetPaymentTerm`
Required: Yes

 ** adjustmentDeadline **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-adjustmentDeadline"></a>
The duration before the agreement end date by which the renewal price is finalized, represented in ISO 8601 format (for example, P30D). Only applicable with `PercentageRange`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** lockoutPeriod **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-lockoutPeriod"></a>
The duration before the agreement end date when the lockout window begins, in ISO 8601 format (for example, P30D). Absent means no lockout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** maxRenewals **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-maxRenewals"></a>
The maximum number of renewals allowed on this offer. Absent means unlimited renewals.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** priceIncrease **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-priceIncrease"></a>
The price increase applied at each renewal cycle. Absent means identical pricing on renewal.
Type: [PriceIncrease](API_marketplace-discovery_PriceIncrease.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** termTemplates **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RenewalTerm-termTemplates"></a>
Structural templates defining how specific terms are reshaped on each renewal cycle. Absent for upfront-only offers.
Type: Array of [TermTemplate](API_marketplace-discovery_TermTemplate.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_marketplace-discovery_RenewalTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/RenewalTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/RenewalTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/RenewalTerm)
