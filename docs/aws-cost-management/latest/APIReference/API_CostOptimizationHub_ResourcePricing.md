---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ResourcePricing.html
---

# ResourcePricing
<a name="API_CostOptimizationHub_ResourcePricing"></a>

Contains pricing information about the specified resource.

## Contents
<a name="API_CostOptimizationHub_ResourcePricing_Contents"></a>

 ** estimatedCostAfterDiscounts **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourcePricing-estimatedCostAfterDiscounts"></a>
The savings estimate incorporating all discounts with AWS, such as Reserved Instances and Savings Plans.
Type: Double
Required: No

 ** estimatedCostBeforeDiscounts **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourcePricing-estimatedCostBeforeDiscounts"></a>
The savings estimate using AWS public pricing without incorporating any discounts.
Type: Double
Required: No

 ** estimatedDiscounts **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourcePricing-estimatedDiscounts"></a>
The estimated discounts for a recommendation.
Type: [EstimatedDiscounts](API_CostOptimizationHub_EstimatedDiscounts.md) object
Required: No

 ** estimatedNetUnusedAmortizedCommitments **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourcePricing-estimatedNetUnusedAmortizedCommitments"></a>
The estimated net unused amortized commitment for the recommendation.
Type: Double
Required: No

## See Also
<a name="API_CostOptimizationHub_ResourcePricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ResourcePricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ResourcePricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ResourcePricing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
