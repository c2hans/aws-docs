---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSSavingsOpportunityAfterDiscounts.html
---

# EBSSavingsOpportunityAfterDiscounts
<a name="API_EBSSavingsOpportunityAfterDiscounts"></a>

 Describes the savings opportunity for Amazon EBS volume recommendations after applying specific discounts.

## Contents
<a name="API_EBSSavingsOpportunityAfterDiscounts_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-EBSSavingsOpportunityAfterDiscounts-estimatedMonthlySavings"></a>
 The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer’s Amazon EBS volume recommendations. This saving includes any applicable discounts.
Type: [EBSEstimatedMonthlySavings](API_EBSEstimatedMonthlySavings.md) object
Required: No

 ** savingsOpportunityPercentage **   <a name="computeoptimizer-Type-EBSSavingsOpportunityAfterDiscounts-savingsOpportunityPercentage"></a>
 The estimated monthly savings possible as a percentage of monthly cost after applying the specific discounts. This saving can be achieved by adopting Compute Optimizer’s Amazon EBS volume recommendations.
Type: Double
Required: No

## See Also
<a name="API_EBSSavingsOpportunityAfterDiscounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EBSSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EBSSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EBSSavingsOpportunityAfterDiscounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
