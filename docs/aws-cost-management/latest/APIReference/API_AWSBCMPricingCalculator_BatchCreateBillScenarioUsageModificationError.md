---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError.html
---

# BatchCreateBillScenarioUsageModificationError
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError"></a>

 Represents an error that occurred during a batch create operation for bill scenario usage modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError_Contents"></a>

 ** errorCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError-errorCode"></a>
 The error code associated with the failed operation.
Type: String
Valid Values: `BAD_REQUEST | NOT_FOUND | CONFLICT | INTERNAL_SERVER_ERROR`
Required: No

 ** errorMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError-errorMessage"></a>
 A descriptive message for the error that occurred.
Type: String
Required: No

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError-key"></a>
 The key of the entry that caused the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModificationError)
