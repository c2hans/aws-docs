---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterNetworkInterface.html
---

# ClusterNetworkInterface
<a name="API_ClusterNetworkInterface"></a>

The network interface configuration for a Amazon SageMaker HyperPod cluster instance group.

## Contents
<a name="API_ClusterNetworkInterface_Contents"></a>

 ** InterfaceType **   <a name="sagemaker-Type-ClusterNetworkInterface-InterfaceType"></a>
The type of network interface for the instance group. Valid values:
+  `efa` – An EFA with ENA interface, which provides both the EFA device for low-latency, high-throughput communication and the ENA device for IP networking.
+  `efa-only` – An EFA-only interface, which provides only the EFA device capabilities without the ENA device for traditional IP networking.
For more information, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html).
Type: String
Valid Values: `efa | efa-only`
Required: No

## See Also
<a name="API_ClusterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterNetworkInterface)
