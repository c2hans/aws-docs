---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError.html
---

# BatchCreateBillScenarioCommitmentModificationError
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError"></a>

 Represents an error that occurred during a batch create operation for bill scenario commitment modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError_Contents"></a>

 ** errorCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError-errorCode"></a>
 The error code associated with the failed operation.
Type: String
Valid Values: `CONFLICT | INTERNAL_SERVER_ERROR | INVALID_ACCOUNT`
Required: No

 ** errorMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError-errorMessage"></a>
 A descriptive message for the error that occurred.
Type: String
Required: No

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError-key"></a>
 The key of the entry that caused the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
