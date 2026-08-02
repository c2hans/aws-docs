---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EksResourceScalingConfiguration.html
---

# EksResourceScalingConfiguration
<a name="API_EksResourceScalingConfiguration"></a>

The AWS EKS resource scaling configuration.

## Contents
<a name="API_EksResourceScalingConfiguration_Contents"></a>

 ** kubernetesResourceType **   <a name="regionswitch-Type-EksResourceScalingConfiguration-kubernetesResourceType"></a>
The Kubernetes resource type for the configuration.
Type: [KubernetesResourceType](API_KubernetesResourceType.md) object
Required: Yes

 ** capacityMonitoringApproach **   <a name="regionswitch-Type-EksResourceScalingConfiguration-capacityMonitoringApproach"></a>
The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.
Type: String
Valid Values: `sampledMaxInLast24Hours`
Required: No

 ** eksClusters **   <a name="regionswitch-Type-EksResourceScalingConfiguration-eksClusters"></a>
The clusters for the configuration.
Type: Array of [EksCluster](API_EksCluster.md) objects
Array Members: Minimum number of 2 items.
Required: No

 ** scalingResources **   <a name="regionswitch-Type-EksResourceScalingConfiguration-scalingResources"></a>
The scaling resources for the configuration.
Type: Array of string to string to [KubernetesScalingResource](API_KubernetesScalingResource.md) object map maps
Array Members: Minimum number of 1 item.
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

 ** targetPercent **   <a name="regionswitch-Type-EksResourceScalingConfiguration-targetPercent"></a>
The target percentage for the configuration. The default is 100.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-EksResourceScalingConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-EksResourceScalingConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [EksResourceScalingUngraceful](API_EksResourceScalingUngraceful.md) object
Required: No

## See Also
<a name="API_EksResourceScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/EksResourceScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/EksResourceScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/EksResourceScalingConfiguration)
