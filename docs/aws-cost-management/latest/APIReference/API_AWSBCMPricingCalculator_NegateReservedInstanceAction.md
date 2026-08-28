---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_NegateReservedInstanceAction.html
---

# NegateReservedInstanceAction
<a name="API_AWSBCMPricingCalculator_NegateReservedInstanceAction"></a>

 Represents an action to remove a Reserved Instance from a bill scenario.

 This is the ID of an existing Reserved Instance in your account.

## Contents
<a name="API_AWSBCMPricingCalculator_NegateReservedInstanceAction_Contents"></a>

 ** reservedInstancesId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_NegateReservedInstanceAction-reservedInstancesId"></a>
 The ID of the Reserved Instance to remove.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_NegateReservedInstanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/NegateReservedInstanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/NegateReservedInstanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/NegateReservedInstanceAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
