---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ComputeSavingsPlansConfiguration.html
---

# ComputeSavingsPlansConfiguration
<a name="API_CostOptimizationHub_ComputeSavingsPlansConfiguration"></a>

The Compute Savings Plans configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_ComputeSavingsPlansConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_ComputeSavingsPlansConfiguration-accountScope"></a>
The account scope for which you want recommendations. AWS calculates recommendations including the management account and member accounts if the value is set to `PAYER`. If the value is `LINKED`, recommendations are calculated for individual member accounts only.
Type: String
Required: No

 ** hourlyCommitment **   <a name="awscostmanagement-Type-CostOptimizationHub_ComputeSavingsPlansConfiguration-hourlyCommitment"></a>
The hourly commitment for the Savings Plans type.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_ComputeSavingsPlansConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_ComputeSavingsPlansConfiguration-term"></a>
The Savings Plans recommendation term in years.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_ComputeSavingsPlansConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ComputeSavingsPlansConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ComputeSavingsPlansConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ComputeSavingsPlansConfiguration)
