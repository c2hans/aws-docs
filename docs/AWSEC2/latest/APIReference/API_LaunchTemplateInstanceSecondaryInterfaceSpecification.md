---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceSecondaryInterfaceSpecification.html
---

# LaunchTemplateInstanceSecondaryInterfaceSpecification
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecification"></a>

Describes a secondary interface specification in a launch template.

## Contents
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecification_Contents"></a>

 ** deleteOnTermination **
Indicates whether the secondary interface is deleted when the instance is terminated.
The only supported value for this field is `true`.
Type: Boolean
Required: No

 ** deviceIndex **
The device index for the secondary interface attachment.
Type: Integer
Required: No

 ** interfaceType **
The type of secondary interface.
Type: String
Valid Values: `secondary`
Required: No

 ** networkCardIndex **
The index of the network card.
Type: Integer
Required: No

 ** privateIpAddressCount **
The number of private IPv4 addresses to assign to the secondary interface.
If you specify `privateIpAddressCount` you cannot specify `privateIpAddresses`
Type: Integer
Required: No

 ** PrivateIpAddressesSet.N **
The private IPv4 addresses to assign to the secondary interface.
If you specify `privateIpAddresses` you cannot specify `privateIpAddressCount`
Type: Array of [SecondaryInterfacePrivateIpAddressSpecification](API_SecondaryInterfacePrivateIpAddressSpecification.md) objects
Required: No

 ** secondarySubnetId **
The ID of the secondary subnet.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecification)
