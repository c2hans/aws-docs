---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_NetworkBandwidthGbpsRequest.html
---

# NetworkBandwidthGbpsRequest
<a name="API_NetworkBandwidthGbpsRequest"></a>

Specifies the minimum and maximum for the `NetworkBandwidthGbps` object when you specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) for an Auto Scaling group.

**Note**
Setting the minimum bandwidth does not guarantee that your instance will achieve the minimum bandwidth. Amazon EC2 will identify instance types that support the specified minimum bandwidth, but the actual bandwidth of your instance might go below the specified minimum at times. For more information, see [Available instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_NetworkBandwidthGbpsRequest_Contents"></a>

 ** Max **
The maximum amount of network bandwidth, in gigabits per second (Gbps).
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Min **
The minimum amount of network bandwidth, in gigabits per second (Gbps).
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_NetworkBandwidthGbpsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/NetworkBandwidthGbpsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/NetworkBandwidthGbpsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/NetworkBandwidthGbpsRequest)
