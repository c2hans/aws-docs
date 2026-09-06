---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ComputationPreference.html
---

# ComputationPreference
<a name="API_ComputationPreference"></a>

The preferences and settings that will be used to compute the AWS charges for a billing group.

## Contents
<a name="API_ComputationPreference_Contents"></a>

 ** PricingPlanArn **   <a name="billingconductor-Type-ComputationPreference-PricingPlanArn"></a>
 The Amazon Resource Name (ARN) of the pricing plan that's used to compute the AWS charges for a billing group.
Type: String
Pattern: `arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`
Required: Yes

## See Also
<a name="API_ComputationPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ComputationPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ComputationPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ComputationPreference)
