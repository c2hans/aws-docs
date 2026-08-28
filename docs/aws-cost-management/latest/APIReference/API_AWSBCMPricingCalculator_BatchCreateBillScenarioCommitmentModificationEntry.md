---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry.html
---

# BatchCreateBillScenarioCommitmentModificationEntry
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry"></a>

 Represents an entry object in the batch operation to create bill scenario commitment modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry_Contents"></a>

 ** commitmentAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry-commitmentAction"></a>
 The specific commitment action to be taken (e.g., adding a Reserved Instance or Savings Plan).
Type: [BillScenarioCommitmentModificationAction](API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry-key"></a>
 A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry-usageAccountId"></a>
 The AWS account ID to which this commitment will be applied to.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry-group"></a>
 An optional group identifier for the commitment modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
