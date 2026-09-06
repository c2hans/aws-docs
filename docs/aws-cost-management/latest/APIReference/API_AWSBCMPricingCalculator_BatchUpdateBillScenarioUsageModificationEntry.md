---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry.html
---

# BatchUpdateBillScenarioUsageModificationEntry
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry"></a>

 Represents an entry in a batch operation to update bill scenario usage modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry-id"></a>
 The unique identifier of the usage modification to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** amounts **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry-amounts"></a>
 The updated usage amounts for the modification.
Type: Array of [UsageAmount](API_AWSBCMPricingCalculator_UsageAmount.md) objects
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry-group"></a>
 The updated group identifier for the usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationEntry)
