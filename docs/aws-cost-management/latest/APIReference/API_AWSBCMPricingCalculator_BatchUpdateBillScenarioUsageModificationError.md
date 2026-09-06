---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError.html
---

# BatchUpdateBillScenarioUsageModificationError
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError"></a>

 Represents an error that occurred when updating usage in a Bill Scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError_Contents"></a>

 ** errorCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError-errorCode"></a>
 The code associated with the error.
Type: String
Valid Values: `BAD_REQUEST | NOT_FOUND | CONFLICT | INTERNAL_SERVER_ERROR`
Required: No

 ** errorMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError-errorMessage"></a>
 The message that describes the error.
Type: String
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError-id"></a>
 The ID of the error.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioUsageModificationError)
