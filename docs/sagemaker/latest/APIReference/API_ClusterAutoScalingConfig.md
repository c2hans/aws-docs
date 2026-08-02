---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterAutoScalingConfig.html
---

# ClusterAutoScalingConfig
<a name="API_ClusterAutoScalingConfig"></a>

Specifies the autoscaling configuration for a HyperPod cluster.

## Contents
<a name="API_ClusterAutoScalingConfig_Contents"></a>

 ** Mode **   <a name="sagemaker-Type-ClusterAutoScalingConfig-Mode"></a>
Describes whether autoscaling is enabled or disabled for the cluster. Valid values are `Enable` and `Disable`.
Type: String
Valid Values: `Enable | Disable`
Required: Yes

 ** AutoScalerType **   <a name="sagemaker-Type-ClusterAutoScalingConfig-AutoScalerType"></a>
The type of autoscaler to use. Currently supported value is `Karpenter`.
Type: String
Valid Values: `Karpenter`
Required: No

## See Also
<a name="API_ClusterAutoScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterAutoScalingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterAutoScalingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterAutoScalingConfig)
