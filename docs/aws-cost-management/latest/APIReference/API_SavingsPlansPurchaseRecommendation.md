---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendation.html
---

# SavingsPlansPurchaseRecommendation
<a name="API_SavingsPlansPurchaseRecommendation"></a>

Contains your request parameters, Savings Plan Recommendations Summary, and Details.

## Contents
<a name="API_SavingsPlansPurchaseRecommendation_Contents"></a>

 ** AccountScope **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-AccountScope"></a>
The account scope that you want your recommendations for. Amazon Web Services calculates recommendations that include the management account and member accounts if the value is set to `PAYER`. If the value is `LINKED`, recommendations are calculated for individual member accounts only.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** LookbackPeriodInDays **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-LookbackPeriodInDays"></a>
The lookback period in days that's used to generate the recommendation.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: No

 ** PaymentOption **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-PaymentOption"></a>
The payment option that's used to generate the recommendation.
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: No

 ** SavingsPlansPurchaseRecommendationDetails **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-SavingsPlansPurchaseRecommendationDetails"></a>
Details for the Savings Plans that we recommend that you purchase to cover existing Savings Plans eligible workloads.
Type: Array of [SavingsPlansPurchaseRecommendationDetail](API_SavingsPlansPurchaseRecommendationDetail.md) objects
Required: No

 ** SavingsPlansPurchaseRecommendationSummary **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-SavingsPlansPurchaseRecommendationSummary"></a>
Summary metrics for your Savings Plans Recommendations.
Type: [SavingsPlansPurchaseRecommendationSummary](API_SavingsPlansPurchaseRecommendationSummary.md) object
Required: No

 ** SavingsPlansType **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-SavingsPlansType"></a>
The requested Savings Plans recommendation type.
Type: String
Valid Values: `COMPUTE_SP | EC2_INSTANCE_SP | SAGEMAKER_SP | DATABASE_SP`
Required: No

 ** TermInYears **   <a name="awscostmanagement-Type-SavingsPlansPurchaseRecommendation-TermInYears"></a>
The Savings Plans recommendation term in years. It's used to generate the recommendation.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: No

## See Also
<a name="API_SavingsPlansPurchaseRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansPurchaseRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansPurchaseRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansPurchaseRecommendation)
