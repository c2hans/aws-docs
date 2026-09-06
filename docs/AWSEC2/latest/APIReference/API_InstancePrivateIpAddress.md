---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstancePrivateIpAddress.html
---

# InstancePrivateIpAddress
<a name="API_InstancePrivateIpAddress"></a>

Describes a private IPv4 address.

## Contents
<a name="API_InstancePrivateIpAddress_Contents"></a>

 ** association **
The association information for an Elastic IP address for the network interface.
Type: [InstanceNetworkInterfaceAssociation](API_InstanceNetworkInterfaceAssociation.md) object
Required: No

 ** primary **
Indicates whether this IPv4 address is the primary private IP address of the network interface.
Type: Boolean
Required: No

 ** privateDnsName **
The private IPv4 DNS name.
Type: String
Required: No

 ** privateIpAddress **
The private IPv4 address of the network interface.
Type: String
Required: No

## See Also
<a name="API_InstancePrivateIpAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstancePrivateIpAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstancePrivateIpAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstancePrivateIpAddress)
