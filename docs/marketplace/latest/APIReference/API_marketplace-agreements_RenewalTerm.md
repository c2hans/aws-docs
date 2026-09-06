---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RenewalTerm.html
---

# RenewalTerm
<a name="API_marketplace-agreements_RenewalTerm"></a>

Defines that on graceful expiration of the agreement (when the agreement ends on its pre-defined end date), a new agreement will be created using the accepted terms on the existing agreement. In other words, the agreement will be renewed. Presence of `RenewalTerm` in the offer document means that auto-renewal is allowed. The acceptor will have the option to accept or decline auto-renewal at the offer acceptance/agreement creation. The acceptor can also change this flag from `True` to `False` or `False` to `True`, within the limits set by `LockoutPeriod` and `MaxRenewals`. Setting the flag to `True` doesn't by itself guarantee that the agreement renews, because the proposer can also opt out.

## Contents
<a name="API_marketplace-agreements_RenewalTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** adjustmentDeadline **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-adjustmentDeadline"></a>
The date by which the proposer must finalize the price increase for the next renewal, measured back from the end date of the agreement. The duration is represented in the ISO 8601 format in whole days (for example, `P30D` for 30 days or `P60D` for 60 days).
This field applies only when `PriceIncrease` is a `PercentageRange`. The field is `null` when `PriceIncrease` is a `FixedPercentage`, because the price increase is already fixed and there is nothing for the proposer to finalize. If the proposer doesn't finalize a value by the adjustment deadline, the `DefaultValue` of the range applies.
 `AdjustmentDeadline` must be greater than `LockoutPeriod`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 9.
Pattern: `P([1-9]\d{0,6}D)`
Required: No

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-configuration"></a>
Additional parameters specified by the acceptor while accepting the term.
Type: [RenewalTermConfiguration](API_marketplace-agreements_RenewalTermConfiguration.md) object
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** lockoutPeriod **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-lockoutPeriod"></a>
The renewal decision deadline, measured back from the end date of the agreement. This is the last day either party can opt in to or opt out of the renewal. The duration is represented in the ISO 8601 format in whole days (for example, `P30D` for 30 days or `P60D` for 60 days).
The field is `null` when no renewal decision deadline is set. In that case, either party can change the auto-renewal decision up to the end date of the agreement.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 9.
Pattern: `P([1-9]\d{0,6}D)`
Required: No

 ** maxRenewals **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-maxRenewals"></a>
The maximum number of times the agreement can be renewed. The field is `null` when the number of renewals is unlimited.
After the agreement reaches this limit, it expires on its end date instead of renewing.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** priceIncrease **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-priceIncrease"></a>
The price increase that is applied each time the agreement renews. The field is `null` when the price doesn't change at renewal.
Type: [PriceIncrease](API_marketplace-agreements_PriceIncrease.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** termTemplates **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-termTemplates"></a>
Defines how specific terms change each time the agreement renews. The field is `null` when no terms change at renewal.
Type: Array of [TermTemplate](API_marketplace-agreements_TermTemplate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RenewalTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_RenewalTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RenewalTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RenewalTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RenewalTerm)
