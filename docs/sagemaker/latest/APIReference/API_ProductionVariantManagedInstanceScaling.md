---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantManagedInstanceScaling.html
---

# ProductionVariantManagedInstanceScaling
<a name="API_ProductionVariantManagedInstanceScaling"></a>

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

## Contents
<a name="API_ProductionVariantManagedInstanceScaling_Contents"></a>

 ** MaxInstanceCount **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScaling-MaxInstanceCount"></a>
The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MinInstanceCount **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScaling-MinInstanceCount"></a>
The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ScaleInPolicy **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScaling-ScaleInPolicy"></a>
Configures the scale-in behavior for managed instance scaling.
Type: [ProductionVariantManagedInstanceScalingScaleInPolicy](API_ProductionVariantManagedInstanceScalingScaleInPolicy.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-ProductionVariantManagedInstanceScaling-Status"></a>
Indicates whether managed instance scaling is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ProductionVariantManagedInstanceScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantManagedInstanceScaling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantManagedInstanceScaling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantManagedInstanceScaling)
