---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem.html
---

# BatchCreateBillScenarioCommitmentModificationItem
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem"></a>

 Represents a successfully created item in a batch operation for bill scenario commitment modifications.

## Contents
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem_Contents"></a>

 ** commitmentAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem-commitmentAction"></a>
 The specific commitment action that was taken.
Type: [BillScenarioCommitmentModificationAction](API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem-group"></a>
 The group identifier for the created commitment modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem-id"></a>
 The unique identifier assigned to the created commitment modification.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** key **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem-key"></a>
 The key of the successfully created entry. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem-usageAccountId"></a>
 The AWS account ID associated with the created commitment modification.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModificationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
