---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantManagedInstanceScalingScaleInPolicy.html
---

# ProductionVariantManagedInstanceScalingScaleInPolicy
<a name="API_ProductionVariantManagedInstanceScalingScaleInPolicy"></a>

Configures the scale-in behavior for managed instance scaling.

## Contents
<a name="API_ProductionVariantManagedInstanceScalingScaleInPolicy_Contents"></a>

 ** Strategy **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScalingScaleInPolicy-Strategy"></a>
The strategy for scaling in instances.
IDLE\_RELEASE
Releases instances that have no hosted inference component copies.
CONSOLIDATION
Consolidates inference component copies onto fewer instances to release more instances. Consolidation honors the scheduling configuration of each inference component. For example, if an inference component specifies Availability Zone balance, consolidation only proceeds when the resulting distribution does not increase the imbalance.
Type: String
Valid Values: `IDLE_RELEASE | CONSOLIDATION`
Required: Yes

 ** CooldownInMinutes **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScalingScaleInPolicy-CooldownInMinutes"></a>
The cooldown period, in minutes, after the last endpoint operation before the endpoint evaluates consolidation scale-in opportunities.
Default value: `20`.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1440.
Required: No

 ** MaximumStepSize **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScalingScaleInPolicy-MaximumStepSize"></a>
The maximum number of instances that the endpoint can terminate at a time during a consolidation scale-in operation.
Default value: `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_ProductionVariantManagedInstanceScalingScaleInPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantManagedInstanceScalingScaleInPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantManagedInstanceScalingScaleInPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantManagedInstanceScalingScaleInPolicy)
