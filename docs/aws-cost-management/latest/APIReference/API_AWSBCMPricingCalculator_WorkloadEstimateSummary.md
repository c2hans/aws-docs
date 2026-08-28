---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_WorkloadEstimateSummary.html
---

# WorkloadEstimateSummary
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateSummary"></a>

 Provides a summary of a workload estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateSummary_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-id"></a>
 The unique identifier of the workload estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** costCurrency **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-costCurrency"></a>
 The currency of the estimated cost.
Type: String
Valid Values: `USD`
Required: No

 ** createdAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-createdAt"></a>
 The timestamp when the workload estimate was created.
Type: Timestamp
Required: No

 ** expiresAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-expiresAt"></a>
 The timestamp when the workload estimate will expire.
Type: Timestamp
Required: No

 ** failureMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-failureMessage"></a>
 An error message if the workload estimate creation or processing failed.
Type: String
Required: No

 ** name **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-name"></a>
 The name of the workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** rateTimestamp **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-rateTimestamp"></a>
 The timestamp of the pricing rates used for the estimate.
Type: Timestamp
Required: No

 ** rateType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-rateType"></a>
 The type of pricing rates used for the estimate.
Type: String
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`
Required: No

 ** status **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-status"></a>
 The current status of the workload estimate.
Type: String
Valid Values: `UPDATING | VALID | INVALID | ACTION_NEEDED`
Required: No

 ** totalCost **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateSummary-totalCost"></a>
 The total estimated cost for the workload.
Type: Double
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/WorkloadEstimateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/WorkloadEstimateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/WorkloadEstimateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
