---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterOperationScalingConfiguration.html
---

# ClusterOperationScalingConfiguration
<a name="API_ClusterOperationScalingConfiguration"></a>

A point-in-time snapshot of an instance group's scaling configuration. This structure represents both the original configuration before the operation and the desired configuration requested by the operation.

## Contents
<a name="API_ClusterOperationScalingConfiguration_Contents"></a>

 ** CurrentCount **   <a name="sagemaker-Type-ClusterOperationScalingConfiguration-CurrentCount"></a>
The number of instances that were in the instance group at the time of the operation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MinCount **   <a name="sagemaker-Type-ClusterOperationScalingConfiguration-MinCount"></a>
The minimum number of instances that must be available in the instance group of a HyperPod cluster before it transitions to `InService` status.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TargetCount **   <a name="sagemaker-Type-ClusterOperationScalingConfiguration-TargetCount"></a>
The target number of instances for the instance group.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ClusterOperationScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterOperationScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterOperationScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterOperationScalingConfiguration)
