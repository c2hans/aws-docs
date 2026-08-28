---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_PreferredCommitment.html
---

# PreferredCommitment
<a name="API_CostOptimizationHub_PreferredCommitment"></a>

The preferred configuration for Reserved Instances and Savings Plans commitment-based discounts, consisting of a payment option and a commitment duration.

## Contents
<a name="API_CostOptimizationHub_PreferredCommitment_Contents"></a>

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_PreferredCommitment-paymentOption"></a>
The preferred upfront payment structure for commitments. If the value is null, it will default to `AllUpfront` (highest savings) where applicable.
Type: String
Valid Values: `AllUpfront | PartialUpfront | NoUpfront`
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_PreferredCommitment-term"></a>
The preferred length of the commitment period. If the value is null, it will default to `ThreeYears` (highest savings) where applicable.
Type: String
Valid Values: `OneYear | ThreeYears`
Required: No

## See Also
<a name="API_CostOptimizationHub_PreferredCommitment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/PreferredCommitment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/PreferredCommitment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/PreferredCommitment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
