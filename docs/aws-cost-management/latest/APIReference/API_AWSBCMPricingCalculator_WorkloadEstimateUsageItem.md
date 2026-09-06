---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_WorkloadEstimateUsageItem.html
---

# WorkloadEstimateUsageItem
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateUsageItem"></a>

 Represents a usage item in a workload estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateUsageItem_Contents"></a>

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-operation"></a>
 The specific operation associated with this usage item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-serviceCode"></a>
 The AWS service code associated with this usage item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-usageType"></a>
 The type of usage for this item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** cost **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-cost"></a>
 The estimated cost for this usage item.
Type: Double
Required: No

 ** currency **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-currency"></a>
 The currency of the estimated cost.
Type: String
Valid Values: `USD`
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-group"></a>
 The group identifier for this usage item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-historicalUsage"></a>
 Historical usage data associated with this item, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-id"></a>
 The unique identifier of this usage item.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-location"></a>
 The location associated with this usage item.
Type: String
Required: No

 ** quantity **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-quantity"></a>
 The estimated usage quantity for this item.
Type: [WorkloadEstimateUsageQuantity](API_AWSBCMPricingCalculator_WorkloadEstimateUsageQuantity.md) object
Required: No

 ** status **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-status"></a>
 The current status of this usage item.
Type: String
Valid Values: `VALID | INVALID | STALE`
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_WorkloadEstimateUsageItem-usageAccountId"></a>
 The AWS account ID associated with this usage item.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_WorkloadEstimateUsageItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/WorkloadEstimateUsageItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/WorkloadEstimateUsageItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/WorkloadEstimateUsageItem)
