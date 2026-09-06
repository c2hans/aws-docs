---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_SubscriptionPricingDetails.html
---

# SubscriptionPricingDetails
<a name="API_SubscriptionPricingDetails"></a>

The pricing details for a subscription.

## Contents
<a name="API_SubscriptionPricingDetails_Contents"></a>

 ** Currency **   <a name="outposts-Type-SubscriptionPricingDetails-Currency"></a>
The currency of the price. Currently only `USD` is supported.
Type: String
Valid Values: `USD`
Required: No

 ** MonthlyRecurringPrice **   <a name="outposts-Type-SubscriptionPricingDetails-MonthlyRecurringPrice"></a>
The monthly recurring price.
Type: Float
Required: No

 ** PaymentOption **   <a name="outposts-Type-SubscriptionPricingDetails-PaymentOption"></a>
The payment option.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** PaymentTerm **   <a name="outposts-Type-SubscriptionPricingDetails-PaymentTerm"></a>
The payment term.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

 ** UpfrontPrice **   <a name="outposts-Type-SubscriptionPricingDetails-UpfrontPrice"></a>
The upfront price.
Type: Float
Required: No

## See Also
<a name="API_SubscriptionPricingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/SubscriptionPricingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/SubscriptionPricingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/SubscriptionPricingDetails)
