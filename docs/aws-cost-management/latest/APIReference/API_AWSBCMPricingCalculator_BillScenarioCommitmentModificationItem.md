---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem.html
---

# BillScenarioCommitmentModificationItem
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem"></a>

 Represents a commitment modification item in a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem_Contents"></a>

 ** commitmentAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem-commitmentAction"></a>
 The specific commitment action taken in this modification.
Type: [BillScenarioCommitmentModificationAction](API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem-group"></a>
 The group identifier for the commitment modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem-id"></a>
 The unique identifier of the commitment modification.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem-usageAccountId"></a>
 The AWS account ID associated with this commitment modification.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationItem)
