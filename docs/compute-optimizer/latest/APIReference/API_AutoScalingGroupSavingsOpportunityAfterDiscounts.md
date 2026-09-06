---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupSavingsOpportunityAfterDiscounts.html
---

# AutoScalingGroupSavingsOpportunityAfterDiscounts
<a name="API_AutoScalingGroupSavingsOpportunityAfterDiscounts"></a>

 Describes the savings opportunity for Auto Scaling group recommendations after applying the Savings Plans and Reserved Instances discounts.

Savings opportunity represents the estimated monthly savings you can achieve by implementing Compute Optimizer recommendations.

## Contents
<a name="API_AutoScalingGroupSavingsOpportunityAfterDiscounts_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-AutoScalingGroupSavingsOpportunityAfterDiscounts-estimatedMonthlySavings"></a>
 An object that describes the estimated monthly savings possible by adopting Compute Optimizer’s Auto Scaling group recommendations. This is based on the Savings Plans and Reserved Instances pricing discounts.
Type: [AutoScalingGroupEstimatedMonthlySavings](API_AutoScalingGroupEstimatedMonthlySavings.md) object
Required: No

 ** savingsOpportunityPercentage **   <a name="computeoptimizer-Type-AutoScalingGroupSavingsOpportunityAfterDiscounts-savingsOpportunityPercentage"></a>
 The estimated monthly savings possible as a percentage of monthly cost after applying the Savings Plans and Reserved Instances discounts. This saving can be achieved by adopting Compute Optimizer’s Auto Scaling group recommendations.
Type: Double
Required: No

## See Also
<a name="API_AutoScalingGroupSavingsOpportunityAfterDiscounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/AutoScalingGroupSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/AutoScalingGroupSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/AutoScalingGroupSavingsOpportunityAfterDiscounts)
