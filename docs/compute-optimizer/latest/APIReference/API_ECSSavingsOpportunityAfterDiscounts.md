---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSSavingsOpportunityAfterDiscounts.html
---

# ECSSavingsOpportunityAfterDiscounts
<a name="API_ECSSavingsOpportunityAfterDiscounts"></a>

 Describes the savings opportunity for Amazon ECS service recommendations after applying Savings Plans discounts.

Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.

## Contents
<a name="API_ECSSavingsOpportunityAfterDiscounts_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-ECSSavingsOpportunityAfterDiscounts-estimatedMonthlySavings"></a>
 The estimated monthly savings possible by adopting Compute Optimizer’s Amazon ECS service recommendations. This includes any applicable Savings Plans discounts.
Type: [ECSEstimatedMonthlySavings](API_ECSEstimatedMonthlySavings.md) object
Required: No

 ** savingsOpportunityPercentage **   <a name="computeoptimizer-Type-ECSSavingsOpportunityAfterDiscounts-savingsOpportunityPercentage"></a>
 The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer’s Amazon ECS service recommendations. This includes any applicable Savings Plans discounts.
Type: Double
Required: No

## See Also
<a name="API_ECSSavingsOpportunityAfterDiscounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSSavingsOpportunityAfterDiscounts)
