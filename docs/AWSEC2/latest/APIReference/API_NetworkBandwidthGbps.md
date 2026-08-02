---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkBandwidthGbps.html
---

# NetworkBandwidthGbps
<a name="API_NetworkBandwidthGbps"></a>

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

**Note**
Setting the minimum bandwidth does not guarantee that your instance will achieve the minimum bandwidth. Amazon EC2 will identify instance types that support the specified minimum bandwidth, but the actual bandwidth of your instance might go below the specified minimum at times. For more information, see [Available instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_NetworkBandwidthGbps_Contents"></a>

 ** Max ** (request), ** max ** (response)
The maximum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no maximum limit.
Type: Double
Required: No

 ** Min ** (request), ** min ** (response)
The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.
Type: Double
Required: No

## See Also
<a name="API_NetworkBandwidthGbps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkBandwidthGbps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkBandwidthGbps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkBandwidthGbps)
