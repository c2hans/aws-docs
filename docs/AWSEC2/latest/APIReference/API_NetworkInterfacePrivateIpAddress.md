---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfacePrivateIpAddress.html
---

# NetworkInterfacePrivateIpAddress
<a name="API_NetworkInterfacePrivateIpAddress"></a>

Describes the private IPv4 address of a network interface.

## Contents
<a name="API_NetworkInterfacePrivateIpAddress_Contents"></a>

 ** association **
The association information for an Elastic IP address (IPv4) associated with the network interface.
Type: [NetworkInterfaceAssociation](API_NetworkInterfaceAssociation.md) object
Required: No

 ** primary **
Indicates whether this IPv4 address is the primary private IPv4 address of the network interface.
Type: Boolean
Required: No

 ** privateDnsName **
The private DNS name.
Type: String
Required: No

 ** privateIpAddress **
The private IPv4 address.
Type: String
Required: No

## See Also
<a name="API_NetworkInterfacePrivateIpAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfacePrivateIpAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfacePrivateIpAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfacePrivateIpAddress)
