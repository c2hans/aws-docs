---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_AddSavingsPlanAction.html
---

# AddSavingsPlanAction
<a name="API_AWSBCMPricingCalculator_AddSavingsPlanAction"></a>

 Represents an action to add a Savings Plan to a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_AddSavingsPlanAction_Contents"></a>

 ** commitment **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_AddSavingsPlanAction-commitment"></a>
 The hourly commitment, in the same currency of the `savingsPlanOfferingId`. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.
Type: Double
Valid Range: Minimum value of 0.001. Maximum value of 1000000.
Required: No

 ** savingsPlanOfferingId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_AddSavingsPlanAction-savingsPlanOfferingId"></a>
 The ID of the Savings Plan offering to add. For more information, see [ DescribeSavingsPlansOfferings](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_AddSavingsPlanAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/AddSavingsPlanAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/AddSavingsPlanAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/AddSavingsPlanAction)
