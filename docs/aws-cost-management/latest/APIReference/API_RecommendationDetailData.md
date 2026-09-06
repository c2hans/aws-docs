---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RecommendationDetailData.html
---

# RecommendationDetailData
<a name="API_RecommendationDetailData"></a>

The details and metrics for the given recommendation.

## Contents
<a name="API_RecommendationDetailData_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-RecommendationDetailData-AccountId"></a>
The AccountID that the recommendation is generated for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AccountScope **   <a name="awscostmanagement-Type-RecommendationDetailData-AccountScope"></a>
The account scope that you want your recommendations for. AWS calculates recommendations including the management account and member accounts if the value is set to PAYER. If the value is LINKED, recommendations are calculated for individual member accounts only.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** CurrencyCode **   <a name="awscostmanagement-Type-RecommendationDetailData-CurrencyCode"></a>
The currency code that AWS used to generate the recommendation and present potential savings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentAverageCoverage **   <a name="awscostmanagement-Type-RecommendationDetailData-CurrentAverageCoverage"></a>
The average value of hourly coverage over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentAverageHourlyOnDemandSpend **   <a name="awscostmanagement-Type-RecommendationDetailData-CurrentAverageHourlyOnDemandSpend"></a>
The average value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMaximumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-RecommendationDetailData-CurrentMaximumHourlyOnDemandSpend"></a>
The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMinimumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-RecommendationDetailData-CurrentMinimumHourlyOnDemandSpend"></a>
The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedAverageCoverage **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedAverageCoverage"></a>
The estimated coverage of the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedAverageUtilization **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedAverageUtilization"></a>
The estimated utilization of the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedMonthlySavingsAmount"></a>
The estimated monthly savings amount based on the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCost **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedOnDemandCost"></a>
The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCostWithCurrentCommitment **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedOnDemandCostWithCurrentCommitment"></a>
The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plan you own.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedROI **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedROI"></a>
The estimated return on investment that's based on the recommended Savings Plan that you purchased. This is calculated as estimatedSavingsAmount/estimatedSPCost\*100.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsAmount **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedSavingsAmount"></a>
The estimated savings amount that's based on the recommended Savings Plan over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsPercentage **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedSavingsPercentage"></a>
The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSPCost **   <a name="awscostmanagement-Type-RecommendationDetailData-EstimatedSPCost"></a>
The cost of the recommended Savings Plan over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ExistingHourlyCommitment **   <a name="awscostmanagement-Type-RecommendationDetailData-ExistingHourlyCommitment"></a>
The existing hourly commitment for the Savings Plan type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** GenerationTimestamp **   <a name="awscostmanagement-Type-RecommendationDetailData-GenerationTimestamp"></a>
The period of time that you want the usage and costs for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** HourlyCommitmentToPurchase **   <a name="awscostmanagement-Type-RecommendationDetailData-HourlyCommitmentToPurchase"></a>
The recommended hourly commitment level for the Savings Plan type and the configuration that's based on the usage during the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceFamily **   <a name="awscostmanagement-Type-RecommendationDetailData-InstanceFamily"></a>
The instance family of the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LatestUsageTimestamp **   <a name="awscostmanagement-Type-RecommendationDetailData-LatestUsageTimestamp"></a>
The period of time that you want the usage and costs for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** LookbackPeriodInDays **   <a name="awscostmanagement-Type-RecommendationDetailData-LookbackPeriodInDays"></a>
How many days of previous usage that AWS considers when making this recommendation.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: No

 ** MetricsOverLookbackPeriod **   <a name="awscostmanagement-Type-RecommendationDetailData-MetricsOverLookbackPeriod"></a>
The related hourly cost, coverage, and utilization metrics over the lookback period.
Type: Array of [RecommendationDetailHourlyMetrics](API_RecommendationDetailHourlyMetrics.md) objects
Required: No

 ** OfferingId **   <a name="awscostmanagement-Type-RecommendationDetailData-OfferingId"></a>
The unique ID that's used to distinguish Savings Plans from one another.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** PaymentOption **   <a name="awscostmanagement-Type-RecommendationDetailData-PaymentOption"></a>
The payment option for the commitment (for example, All Upfront or No Upfront).
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: No

 ** Region **   <a name="awscostmanagement-Type-RecommendationDetailData-Region"></a>
The region the recommendation is generated for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SavingsPlansType **   <a name="awscostmanagement-Type-RecommendationDetailData-SavingsPlansType"></a>
The requested Savings Plan recommendation type.
Type: String
Valid Values: `COMPUTE_SP | EC2_INSTANCE_SP | SAGEMAKER_SP | DATABASE_SP`
Required: No

 ** TermInYears **   <a name="awscostmanagement-Type-RecommendationDetailData-TermInYears"></a>
The term of the commitment in years.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: No

 ** UpfrontCost **   <a name="awscostmanagement-Type-RecommendationDetailData-UpfrontCost"></a>
The upfront cost of the recommended Savings Plan, based on the selected payment option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_RecommendationDetailData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RecommendationDetailData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RecommendationDetailData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RecommendationDetailData)
