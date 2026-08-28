---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry.html
---

# BatchUpdateWorkloadEstimateUsageEntry
<a name="API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry"></a>

 Represents an entry in a batch operation to update workload estimate usage.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry-id"></a>
 The unique identifier of the usage estimate to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** amount **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry-amount"></a>
 The updated estimated usage amount.
Type: Double
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry-group"></a>
 The updated group identifier for the usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchUpdateWorkloadEstimateUsageEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchUpdateWorkloadEstimateUsageEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchUpdateWorkloadEstimateUsageEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
