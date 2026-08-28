---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry.html
---

# BatchCreateWorkloadEstimateUsageEntry
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry"></a>

 Represents an entry in a batch operation to create workload estimate usage.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry_Contents"></a>

 ** amount **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-amount"></a>
 The estimated usage amount.
Type: Double
Required: Yes

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-key"></a>
 A unique identifier for this entry in the batch operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-operation"></a>
 The specific operation associated with this usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-serviceCode"></a>
 The AWS service code for this usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-usageAccountId"></a>
 The AWS account ID associated with this usage estimate.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-usageType"></a>
 The type of usage being estimated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-group"></a>
 An optional group identifier for the usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry-historicalUsage"></a>
 Historical usage data associated with this estimate, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
