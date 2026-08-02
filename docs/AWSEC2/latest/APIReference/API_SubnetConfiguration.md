---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SubnetConfiguration.html
---

# SubnetConfiguration
<a name="API_SubnetConfiguration"></a>

Describes the configuration of a subnet for a VPC endpoint.

## Contents
<a name="API_SubnetConfiguration_Contents"></a>

 ** Ipv4 **
The IPv4 address to assign to the endpoint network interface in the subnet. You must provide an IPv4 address if the VPC endpoint supports IPv4.
If you specify an IPv4 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.
Type: String
Required: No

 ** Ipv6 **
The IPv6 address to assign to the endpoint network interface in the subnet. You must provide an IPv6 address if the VPC endpoint supports IPv6.
If you specify an IPv6 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.
Type: String
Required: No

 ** SubnetId **
The ID of the subnet.
Type: String
Required: No

## See Also
<a name="API_SubnetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SubnetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SubnetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SubnetConfiguration)
