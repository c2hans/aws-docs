---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendationSummary.html
---

# SavingsPlansPurchaseRecommendationSummary
<a name="API_SavingsPlansPurchaseRecommendationSummary"></a>

Summary metrics for your Savings Plans Purchase Recommendations.

## Contents
<a name="API_SavingsPlansPurchaseRecommendationSummary_Contents"></a>

 ** CurrencyCode **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-CurrencyCode"></a>
The currency code that AWS used to generate the recommendations and present potential savings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentOnDemandSpend **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-CurrentOnDemandSpend"></a>
The current total on demand spend of the applicable usage types over the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DailyCommitmentToPurchase **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-DailyCommitmentToPurchase"></a>
The recommended Savings Plans cost on a daily (24 hourly) basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedMonthlySavingsAmount"></a>
The estimated monthly savings amount that's based on the recommended Savings Plans purchase.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCostWithCurrentCommitment **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedOnDemandCostWithCurrentCommitment"></a>
The estimated On-Demand costs you expect with no additional commitment. It's based on your usage of the selected time period and the Savings Plans you own.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedROI **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedROI"></a>
The estimated return on investment that's based on the recommended Savings Plans and estimated savings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsAmount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedSavingsAmount"></a>
The estimated total savings over the lookback period, based on the purchase of the recommended Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedSavingsPercentage **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedSavingsPercentage"></a>
The estimated savings relative to the total cost of On-Demand usage, over the lookback period. This is calculated as `estimatedSavingsAmount`/ `CurrentOnDemandSpend`\*100.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedTotalCost **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-EstimatedTotalCost"></a>
The estimated total cost of the usage after purchasing the recommended Savings Plans. This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand usage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** HourlyCommitmentToPurchase **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-HourlyCommitmentToPurchase"></a>
The recommended hourly commitment that's based on the recommendation parameters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalRecommendationCount **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendationSummary-TotalRecommendationCount"></a>
The aggregate number of Savings Plans recommendations that exist for your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SavingsPlansPurchaseRecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansPurchaseRecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansPurchaseRecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansPurchaseRecommendationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
