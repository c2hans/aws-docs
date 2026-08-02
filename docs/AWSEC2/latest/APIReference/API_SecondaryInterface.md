---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecondaryInterface.html
---

# SecondaryInterface
<a name="API_SecondaryInterface"></a>

Describes a secondary interface.

## Contents
<a name="API_SecondaryInterface_Contents"></a>

 ** attachment **
The attachment information for the secondary interface.
Type: [SecondaryInterfaceAttachment](API_SecondaryInterfaceAttachment.md) object
Required: No

 ** availabilityZone **
The Availability Zone of the secondary interface.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone of the secondary interface.
Type: String
Required: No

 ** macAddress **
The MAC address of the secondary interface.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the secondary interface.
Type: String
Required: No

 ** PrivateIpv4AddressSet.N **
The private IPv4 addresses associated with the secondary interface.
Type: Array of [SecondaryInterfaceIpv4Address](API_SecondaryInterfaceIpv4Address.md) objects
Required: No

 ** secondaryInterfaceArn **
The Amazon Resource Name (ARN) of the secondary interface.
Type: String
Required: No

 ** secondaryInterfaceId **
The ID of the secondary interface.
Type: String
Required: No

 ** secondaryInterfaceType **
The type of secondary interface.
Type: String
Valid Values: `secondary`
Required: No

 ** secondaryNetworkId **
The ID of the secondary network.
Type: String
Required: No

 ** secondaryNetworkType **
The type of the secondary network.
Type: String
Valid Values: `rdma`
Required: No

 ** secondarySubnetId **
The ID of the secondary subnet.
Type: String
Required: No

 ** sourceDestCheck **
Indicates whether source/destination checking is enabled.
Type: Boolean
Required: No

 ** status **
The status of the secondary interface.
Type: String
Valid Values: `available | in-use`
Required: No

 ** TagSet.N **
The tags assigned to the secondary interface.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_SecondaryInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecondaryInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecondaryInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecondaryInterface)
