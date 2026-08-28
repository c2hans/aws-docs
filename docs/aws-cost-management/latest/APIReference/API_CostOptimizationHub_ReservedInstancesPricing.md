---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ReservedInstancesPricing.html
---

# ReservedInstancesPricing
<a name="API_CostOptimizationHub_ReservedInstancesPricing"></a>

Pricing details for your recommended reserved instance.

## Contents
<a name="API_CostOptimizationHub_ReservedInstancesPricing_Contents"></a>

 ** estimatedMonthlyAmortizedReservationCost **   <a name="awscostmanagement-Type-CostOptimizationHub_ReservedInstancesPricing-estimatedMonthlyAmortizedReservationCost"></a>
The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.
Type: Double
Required: No

 ** estimatedOnDemandCost **   <a name="awscostmanagement-Type-CostOptimizationHub_ReservedInstancesPricing-estimatedOnDemandCost"></a>
The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.
Type: Double
Required: No

 ** monthlyReservationEligibleCost **   <a name="awscostmanagement-Type-CostOptimizationHub_ReservedInstancesPricing-monthlyReservationEligibleCost"></a>
The cost of paying for the recommended reserved instance monthly.
Type: Double
Required: No

 ** savingsPercentage **   <a name="awscostmanagement-Type-CostOptimizationHub_ReservedInstancesPricing-savingsPercentage"></a>
The savings percentage relative to the total On-Demand costs that are associated with this instance.
Type: Double
Required: No

## See Also
<a name="API_CostOptimizationHub_ReservedInstancesPricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ReservedInstancesPricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ReservedInstancesPricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ReservedInstancesPricing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
