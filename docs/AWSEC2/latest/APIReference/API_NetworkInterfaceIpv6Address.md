---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfaceIpv6Address.html
---

# NetworkInterfaceIpv6Address
<a name="API_NetworkInterfaceIpv6Address"></a>

Describes an IPv6 address associated with a network interface.

## Contents
<a name="API_NetworkInterfaceIpv6Address_Contents"></a>

 ** ipv6Address **
The IPv6 address.
Type: String
Required: No

 ** isPrimaryIpv6 **
Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html).
Type: Boolean
Required: No

 ** publicIpv6DnsName **
An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

## See Also
<a name="API_NetworkInterfaceIpv6Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfaceIpv6Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfaceIpv6Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfaceIpv6Address)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
