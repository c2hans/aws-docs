---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendationDetail.html
---

# SavingsPlansPurchaseRecommendationDetail
<a name="API_SavingsPlansPurchaseRecommendationDetail"></a>

Details for your recommended Savings Plans.

## Contents
<a name="API_SavingsPlansPurchaseRecommendationDetail_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-AccountId"></a>
The `AccountID` the recommendation is generated for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrencyCode **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-CurrencyCode"></a>
The currency code that AWS used to generate the recommendations and present potential savings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentAverageHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-CurrentAverageHourlyOnDemandSpend"></a>
The average value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMaximumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-CurrentMaximumHourlyOnDemandSpend"></a>
The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMinimumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-CurrentMinimumHourlyOnDemandSpend"></a>
The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedAverageUtilization **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedAverageUtilization"></a>
The estimated utilization of the recommended Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedMonthlySavingsAmount"></a>
The estimated monthly savings amount based on the recommended Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedOnDemandCost"></a>
The remaining On-Demand cost estimated to not be covered by the recommended Savings Plans, over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCostWithCurrentCommitment **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedOnDemandCostWithCurrentCommitment"></a>
 The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plans you own.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedROI **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedROI"></a>
The estimated return on investment that's based on the recommended Savings Plans that you purchased. This is calculated as `estimatedSavingsAmount`/ `estimatedSPCost`\*100.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedSavingsAmount"></a>
The estimated savings amount that's based on the recommended Savings Plans over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsPercentage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedSavingsPercentage"></a>
The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSPCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-EstimatedSPCost"></a>
The cost of the recommended Savings Plans over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** HourlyCommitmentToPurchase **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-HourlyCommitmentToPurchase"></a>
The recommended hourly commitment level for the Savings Plans type and the configuration that's based on the usage during the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** RecommendationDetailId **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-RecommendationDetailId"></a>
Contains detailed information about a specific Savings Plan recommendation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

 ** SavingsPlansDetails **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-SavingsPlansDetails"></a>
Details for your recommended Savings Plans.
Type: [SavingsPlansDetails](API_SavingsPlansDetails.md) object
Required: No

 ** UpfrontCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationDetail-UpfrontCost"></a>
The upfront cost of the recommended Savings Plans, based on the selected payment option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansPurchaseRecommendationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansPurchaseRecommendationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansPurchaseRecommendationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansPurchaseRecommendationDetail)
