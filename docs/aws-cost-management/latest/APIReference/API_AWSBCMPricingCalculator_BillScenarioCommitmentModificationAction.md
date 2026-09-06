---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.html
---

# BillScenarioCommitmentModificationAction
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction"></a>

 Represents an action to modify commitments in a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** addReservedInstanceAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction-addReservedInstanceAction"></a>
 Action to add a Reserved Instance to the scenario.
Type: [AddReservedInstanceAction](API_AWSBCMPricingCalculator_AddReservedInstanceAction.md) object
Required: No

 ** addSavingsPlanAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction-addSavingsPlanAction"></a>
 Action to add a Savings Plan to the scenario.
Type: [AddSavingsPlanAction](API_AWSBCMPricingCalculator_AddSavingsPlanAction.md) object
Required: No

 ** negateReservedInstanceAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction-negateReservedInstanceAction"></a>
 Action to remove a Reserved Instance from the scenario.
Type: [NegateReservedInstanceAction](API_AWSBCMPricingCalculator_NegateReservedInstanceAction.md) object
Required: No

 ** negateSavingsPlanAction **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction-negateSavingsPlanAction"></a>
 Action to remove a Savings Plan from the scenario.
Type: [NegateSavingsPlanAction](API_AWSBCMPricingCalculator_NegateSavingsPlanAction.md) object
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillScenarioCommitmentModificationAction)
