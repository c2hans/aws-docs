---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseAnalysisDetails.html
---

# SavingsPlansPurchaseAnalysisDetails
<a name="API_SavingsPlansPurchaseAnalysisDetails"></a>

Details about the Savings Plans purchase analysis.

## Contents
<a name="API_SavingsPlansPurchaseAnalysisDetails_Contents"></a>

 ** AdditionalMetadata **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-AdditionalMetadata"></a>
Additional metadata that might be applicable to the commitment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrencyCode **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrencyCode"></a>
The currency code used for the analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentAverageCoverage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrentAverageCoverage"></a>
The average value of hourly coverage over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentAverageHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrentAverageHourlyOnDemandSpend"></a>
The average value of hourly On-Demand spend over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMaximumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrentMaximumHourlyOnDemandSpend"></a>
The highest value of hourly On-Demand spend over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentMinimumHourlyOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrentMinimumHourlyOnDemandSpend"></a>
The lowest value of hourly On-Demand spend over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-CurrentOnDemandSpend"></a>
The current total On-Demand spend over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedAverageCoverage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedAverageCoverage"></a>
The estimated coverage of the Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedAverageUtilization **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedAverageUtilization"></a>
The estimated utilization of the Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedCommitmentCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedCommitmentCost"></a>
The estimated cost of the Savings Plan over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedMonthlySavingsAmount"></a>
The estimated monthly savings amount based on the Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedOnDemandCost"></a>
The remaining On-Demand cost estimated to not be covered by the Savings Plan over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCostWithCurrentCommitment **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedOnDemandCostWithCurrentCommitment"></a>
The estimated On-Demand cost you expect with no additional commitment based on your usage of the selected time period and the Savings Plan you own.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedROI **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedROI"></a>
The estimated return on investment that's based on the Savings Plan and estimated savings. This is calculated as estimatedSavingsAmount/estimatedSPCost\*100.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedSavingsAmount"></a>
The estimated savings amount that's based on the Savings Plan over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsPercentage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-EstimatedSavingsPercentage"></a>
The estimated savings percentage relative to the total cost over the cost calculation lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ExistingHourlyCommitment **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-ExistingHourlyCommitment"></a>
The existing hourly commitment for the Savings Plan type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** HourlyCommitmentToPurchase **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-HourlyCommitmentToPurchase"></a>
The recommended or custom hourly commitment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LatestUsageTimestamp **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-LatestUsageTimestamp"></a>
The date and time of the last hour that went into the analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LookbackPeriodInHours **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-LookbackPeriodInHours"></a>
The lookback period in hours that's used to generate the analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MetricsOverLookbackPeriod **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-MetricsOverLookbackPeriod"></a>
The related hourly cost, coverage, and utilization metrics over the lookback period.
Type: Array of [RecommendationDetailHourlyMetrics](API_RecommendationDetailHourlyMetrics.md) objects
Required: No

 ** UpfrontCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseAnalysisDetails-UpfrontCost"></a>
The upfront cost of the Savings Plan based on the selected payment option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansPurchaseAnalysisDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansPurchaseAnalysisDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansPurchaseAnalysisDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansPurchaseAnalysisDetails)
