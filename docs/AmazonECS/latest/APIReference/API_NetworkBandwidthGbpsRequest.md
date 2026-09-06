---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkBandwidthGbpsRequest.html
---

# NetworkBandwidthGbpsRequest
<a name="API_NetworkBandwidthGbpsRequest"></a>

The minimum and maximum network bandwidth in gigabits per second (Gbps) for instance type selection. This is important for network-intensive workloads.

## Contents
<a name="API_NetworkBandwidthGbpsRequest_Contents"></a>

 ** max **   <a name="ECS-Type-NetworkBandwidthGbpsRequest-max"></a>
The maximum network bandwidth in Gbps. Instance types with higher network bandwidth are excluded from selection.
Type: Double
Required: No

 ** min **   <a name="ECS-Type-NetworkBandwidthGbpsRequest-min"></a>
The minimum network bandwidth in Gbps. Instance types with lower network bandwidth are excluded from selection.
Type: Double
Required: No

## See Also
<a name="API_NetworkBandwidthGbpsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/NetworkBandwidthGbpsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/NetworkBandwidthGbpsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/NetworkBandwidthGbpsRequest)
