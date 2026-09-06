---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceIpv6Address.html
---

# InstanceIpv6Address
<a name="API_InstanceIpv6Address"></a>

Describes an IPv6 address.

## Contents
<a name="API_InstanceIpv6Address_Contents"></a>

 ** Ipv6Address ** (request), ** ipv6Address ** (response)
The IPv6 address.
Type: String
Required: No

 ** IsPrimaryIpv6 ** (request), ** isPrimaryIpv6 ** (response)
Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html).
Type: Boolean
Required: No

## See Also
<a name="API_InstanceIpv6Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceIpv6Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceIpv6Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceIpv6Address)
