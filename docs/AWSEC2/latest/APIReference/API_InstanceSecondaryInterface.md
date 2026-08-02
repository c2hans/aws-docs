---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceSecondaryInterface.html
---

# InstanceSecondaryInterface
<a name="API_InstanceSecondaryInterface"></a>

Describes a secondary interface attached to an instance.

## Contents
<a name="API_InstanceSecondaryInterface_Contents"></a>

 ** attachment **
The attachment information for the secondary interface.
Type: [InstanceSecondaryInterfaceAttachment](API_InstanceSecondaryInterfaceAttachment.md) object
Required: No

 ** interfaceType **
The type of secondary interface.
Type: String
Valid Values: `secondary`
Required: No

 ** macAddress **
The MAC address of the secondary interface.
Type: String
Required: No

 ** ownerId **
The AWS account ID of the owner of the secondary interface.
Type: String
Required: No

 ** PrivateIpAddressSet.N **
The private IPv4 addresses associated with the secondary interface.
Type: Array of [InstanceSecondaryInterfacePrivateIpAddress](API_InstanceSecondaryInterfacePrivateIpAddress.md) objects
Required: No

 ** secondaryInterfaceId **
The ID of the secondary interface.
Type: String
Required: No

 ** secondaryNetworkId **
The ID of the secondary network.
Type: String
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

## See Also
<a name="API_InstanceSecondaryInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceSecondaryInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceSecondaryInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceSecondaryInterface)
