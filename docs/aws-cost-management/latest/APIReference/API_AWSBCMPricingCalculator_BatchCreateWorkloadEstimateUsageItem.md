---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem.html
---

# BatchCreateWorkloadEstimateUsageItem
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem"></a>

 Represents a successfully created item in a batch operation for workload estimate usage.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem_Contents"></a>

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-operation"></a>
 The specific operation associated with this usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-serviceCode"></a>
 The AWS service code for this usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-usageType"></a>
 The type of usage that was estimated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** cost **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-cost"></a>
 The estimated cost associated with this usage.
Type: Double
Required: No

 ** currency **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-currency"></a>
 The currency of the estimated cost.
Type: String
Valid Values: `USD`
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-group"></a>
 The group identifier for the created usage estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-historicalUsage"></a>
 Historical usage data associated with this estimate, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-id"></a>
 The unique identifier assigned to the created usage estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-key"></a>
 The key of the successfully created entry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-location"></a>
 The location associated with this usage estimate.
Type: String
Required: No

 ** quantity **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-quantity"></a>
 The estimated usage quantity.
Type: [WorkloadEstimateUsageQuantity](API_AWSBCMPricingCalculator_WorkloadEstimateUsageQuantity.md) object
Required: No

 ** status **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-status"></a>
 The current status of the created usage estimate.
Type: String
Valid Values: `VALID | INVALID | STALE`
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem-usageAccountId"></a>
 The AWS account ID associated with the created usage estimate.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateWorkloadEstimateUsageItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
