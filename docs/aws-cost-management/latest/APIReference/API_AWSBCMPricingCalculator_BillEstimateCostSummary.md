---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateCostSummary.html
---

# BillEstimateCostSummary
<a name="API_AWSBCMPricingCalculator_BillEstimateCostSummary"></a>

 Provides a summary of cost-related information for a bill estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_BillEstimateCostSummary_Contents"></a>

 ** serviceCostDifferences **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCostSummary-serviceCostDifferences"></a>
 A breakdown of cost differences by AWS service.
Type: String to [CostDifference](API_AWSBCMPricingCalculator_CostDifference.md) object map
Required: No

 ** totalCostDifference **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCostSummary-totalCostDifference"></a>
 The total difference in cost between the estimated and historical costs.
Type: [CostDifference](API_AWSBCMPricingCalculator_CostDifference.md) object
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillEstimateCostSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillEstimateCostSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillEstimateCostSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillEstimateCostSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
