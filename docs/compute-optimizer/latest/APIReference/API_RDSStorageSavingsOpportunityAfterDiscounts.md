---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSStorageSavingsOpportunityAfterDiscounts.html
---

# RDSStorageSavingsOpportunityAfterDiscounts
<a name="API_RDSStorageSavingsOpportunityAfterDiscounts"></a>

 Describes the savings opportunity for Amazon RDS storage recommendations after applying Savings Plans discounts.

 Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.

## Contents
<a name="API_RDSStorageSavingsOpportunityAfterDiscounts_Contents"></a>

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-RDSStorageSavingsOpportunityAfterDiscounts-estimatedMonthlySavings"></a>
 The estimated monthly savings possible by adopting Compute Optimizer’s DB instance storage recommendations. This includes any applicable Savings Plans discounts.
Type: [RDSStorageEstimatedMonthlySavings](API_RDSStorageEstimatedMonthlySavings.md) object
Required: No

 ** savingsOpportunityPercentage **   <a name="computeoptimizer-Type-RDSStorageSavingsOpportunityAfterDiscounts-savingsOpportunityPercentage"></a>
 The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer’s DB instance storage recommendations. This includes any applicable Savings Plans discounts.
Type: Double
Required: No

## See Also
<a name="API_RDSStorageSavingsOpportunityAfterDiscounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSStorageSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSStorageSavingsOpportunityAfterDiscounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSStorageSavingsOpportunityAfterDiscounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
