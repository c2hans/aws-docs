---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterOperationScalingDetails.html
---

# ClusterOperationScalingDetails

The scaling details for a single instance group that is affected by a cluster operation.

## Contents
<a name="API_ClusterOperationScalingDetails_Contents"></a>

 ** Desired **   <a name="sagemaker-Type-ClusterOperationScalingDetails-Desired"></a>
The desired scaling configuration of the instance group for the scaling operation, including its target and minimum instance counts.
Type: [ClusterOperationScalingConfiguration](API_ClusterOperationScalingConfiguration.md) object
Required: No

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterOperationScalingDetails-InstanceGroupName"></a>
The name of the instance group being scaled.
Type: String
Required: No

 ** Original **   <a name="sagemaker-Type-ClusterOperationScalingDetails-Original"></a>
The scaling configuration of the instance group before the scaling operation was applied, including its current, target, and minimum instance counts.
Type: [ClusterOperationScalingConfiguration](API_ClusterOperationScalingConfiguration.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-ClusterOperationScalingDetails-Status"></a>
The status of the scaling operation for this instance group. Valid values are `InProgress`, `Superseded`, or `Done`.
Type: String
Valid Values: `InProgress | Superseded | Done`
Required: No

## See Also
<a name="API_ClusterOperationScalingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterOperationScalingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterOperationScalingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterOperationScalingDetails)
