---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationSummary.html
---

# ReservationPurchaseRecommendationSummary
<a name="API_ReservationPurchaseRecommendationSummary"></a>

A summary about this recommendation, such as the currency code, the amount that AWS estimates that you could save, and the total amount of reservation to purchase.

## Contents
<a name="API_ReservationPurchaseRecommendationSummary_Contents"></a>

 ** CurrencyCode **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationSummary-CurrencyCode"></a>
The currency code used for this recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalEstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationSummary-TotalEstimatedMonthlySavingsAmount"></a>
The total amount that AWS estimates that this recommendation could save you in a month.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalEstimatedMonthlySavingsPercentage **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationSummary-TotalEstimatedMonthlySavingsPercentage"></a>
The total amount that AWS estimates that this recommendation could save you in a month, as a percentage of your costs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ReservationPurchaseRecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ReservationPurchaseRecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ReservationPurchaseRecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ReservationPurchaseRecommendationSummary)
