---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError.html
---

# BatchDeleteBillScenarioCommitmentModificationError
<a name="API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError"></a>

 Represents an error that occurred when deleting a commitment in a Bill Scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError_Contents"></a>

 ** errorCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError-errorCode"></a>
 The code associated with the error.
Type: String
Valid Values: `BAD_REQUEST | CONFLICT | INTERNAL_SERVER_ERROR`
Required: No

 ** errorMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError-errorMessage"></a>
 The message that describes the error.
Type: String
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError-id"></a>
 The ID of the error.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchDeleteBillScenarioCommitmentModificationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchDeleteBillScenarioCommitmentModificationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchDeleteBillScenarioCommitmentModificationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
