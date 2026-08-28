---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest.html
---

# LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest"></a>

Describes a secondary interface specification for a launch template request.

## Contents
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest_Contents"></a>

 ** DeleteOnTermination **
Indicates whether the secondary interface is deleted when the instance is terminated.
The only supported value for this field is `true`.
Type: Boolean
Required: No

 ** DeviceIndex **
The device index for the secondary interface attachment.
Type: Integer
Required: No

 ** InterfaceType **
The type of secondary interface.
Type: String
Valid Values: `secondary`
Required: No

 ** NetworkCardIndex **
The index of the network card.
Type: Integer
Required: No

 ** PrivateIpAddress.N **
The private IPv4 addresses to assign to the secondary interface.
Type: Array of [SecondaryInterfacePrivateIpAddressSpecificationRequest](API_SecondaryInterfacePrivateIpAddressSpecificationRequest.md) objects
Required: No

 ** PrivateIpAddressCount **
The number of private IPv4 addresses to assign to the secondary interface.
Type: Integer
Required: No

 ** SecondarySubnetId **
The ID of the secondary subnet.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
