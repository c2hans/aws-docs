---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_AddReservedInstanceAction.html
---

# AddReservedInstanceAction
<a name="API_AWSBCMPricingCalculator_AddReservedInstanceAction"></a>

 Represents an action to add a Reserved Instance to a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_AddReservedInstanceAction_Contents"></a>

 ** instanceCount **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_AddReservedInstanceAction-instanceCount"></a>
 The number of instances to add for this Reserved Instance offering.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** reservedInstancesOfferingId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_AddReservedInstanceAction-reservedInstancesOfferingId"></a>
 The ID of the Reserved Instance offering to add. For more information, see [ DescribeReservedInstancesOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_AddReservedInstanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/AddReservedInstanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/AddReservedInstanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/AddReservedInstanceAction)
