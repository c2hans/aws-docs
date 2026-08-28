---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry.html
---

# BatchUpdateBillScenarioCommitmentModificationEntry
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry"></a>

 Represents an entry in a batch operation to update bill scenario commitment modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry-id"></a>
 The unique identifier of the commitment modification to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry-group"></a>
 The updated group identifier for the commitment modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioCommitmentModificationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioCommitmentModificationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchUpdateBillScenarioCommitmentModificationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
