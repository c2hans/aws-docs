---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem.html
---

# BatchCreateBillScenarioUsageModificationItem
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem"></a>

 Represents a successfully created item in a batch operation for bill scenario usage modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem_Contents"></a>

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-operation"></a>
 The specific operation associated with this usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-serviceCode"></a>
 The AWS service code for this usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-usageType"></a>
 The type of usage that was modified.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** availabilityZone **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-availabilityZone"></a>
 The availability zone associated with this usage modification, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-group"></a>
 The group identifier for the created usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-historicalUsage"></a>
 Historical usage data associated with this modification, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-id"></a>
 The unique identifier assigned to the created usage modification.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-key"></a>
 The key of the successfully created entry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-location"></a>
 The location associated with this usage modification.
Type: String
Required: No

 ** quantities **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-quantities"></a>
 The modified usage quantities.
Type: Array of [UsageQuantity](API_AWSBCMPricingCalculator_UsageQuantity.md) objects
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem-usageAccountId"></a>
 The AWS account ID associated with the created usage modification.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationItem)
