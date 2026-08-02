---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry.html
---

# BatchCreateBillScenarioUsageModificationEntry
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry"></a>

 Represents an entry in a batch operation to create bill scenario usage modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-key"></a>
 A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any usage entry as any error is returned with this key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-operation"></a>
 The specific operation associated with this usage modification. Describes the specific AWS operation that this usage line models. For example, `RunInstances` indicates the operation of an Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-serviceCode"></a>
 The AWS service code for this usage modification. This identifies the specific AWS service to the customer as a unique short abbreviation. For example, `AmazonEC2` and `AWSKMS`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-usageAccountId"></a>
 The AWS account ID to which this usage will be applied to.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-usageType"></a>
 Describes the usage details of the usage line item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** amounts **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-amounts"></a>
 The amount of usage you want to create for the service use you are modeling.
Type: Array of [UsageAmount](API_AWSBCMPricingCalculator_UsageAmount.md) objects
Required: No

 ** availabilityZone **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-availabilityZone"></a>
 The Availability Zone that this usage line uses.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-group"></a>
 An optional group identifier for the usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry-historicalUsage"></a>
 Historical usage data associated with this modification, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationEntry)
