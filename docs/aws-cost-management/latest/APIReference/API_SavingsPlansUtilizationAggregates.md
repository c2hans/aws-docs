---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilizationAggregates.html
---

# SavingsPlansUtilizationAggregates
<a name="API_SavingsPlansUtilizationAggregates"></a>

The aggregated utilization metrics for your Savings Plans usage.

## Contents
<a name="API_SavingsPlansUtilizationAggregates_Contents"></a>

 ** Utilization **   <a name="awscostmanagement-Type-SavingsPlansUtilizationAggregates-Utilization"></a>
A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.
Type: [SavingsPlansUtilization](API_SavingsPlansUtilization.md) object
Required: Yes

 ** AmortizedCommitment **   <a name="awscostmanagement-Type-SavingsPlansUtilizationAggregates-AmortizedCommitment"></a>
The total amortized commitment for a Savings Plans. This includes the sum of the upfront and recurring Savings Plans fees.
Type: [SavingsPlansAmortizedCommitment](API_SavingsPlansAmortizedCommitment.md) object
Required: No

 ** Savings **   <a name="awscostmanagement-Type-SavingsPlansUtilizationAggregates-Savings"></a>
The amount that's saved by using existing Savings Plans. Savings returns both net savings from Savings Plans and also the `onDemandCostEquivalent` of the Savings Plans when considering the utilization rate.
Type: [SavingsPlansSavings](API_SavingsPlansSavings.md) object
Required: No

## See Also
<a name="API_SavingsPlansUtilizationAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlansUtilizationAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlansUtilizationAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlansUtilizationAggregates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
