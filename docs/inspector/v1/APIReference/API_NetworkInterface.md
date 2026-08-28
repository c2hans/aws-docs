---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

Contains information about the network interfaces interacting with an EC2 instance. This data type is used as one of the elements of the [AssetAttributes](API_AssetAttributes.md) data type.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** ipv6Addresses **   <a name="Inspector-Type-NetworkInterface-ipv6Addresses"></a>
The IP addresses associated with the network interface.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** networkInterfaceId **   <a name="Inspector-Type-NetworkInterface-networkInterfaceId"></a>
The ID of the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** privateDnsName **   <a name="Inspector-Type-NetworkInterface-privateDnsName"></a>
The name of a private DNS associated with the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** privateIpAddress **   <a name="Inspector-Type-NetworkInterface-privateIpAddress"></a>
The private IP address associated with the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** privateIpAddresses **   <a name="Inspector-Type-NetworkInterface-privateIpAddresses"></a>
A list of the private IP addresses associated with the network interface. Includes the privateDnsName and privateIpAddress.
Type: Array of [PrivateIp](API_PrivateIp.md) objects
Required: No

 ** publicDnsName **   <a name="Inspector-Type-NetworkInterface-publicDnsName"></a>
The name of a public DNS associated with the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** publicIp **   <a name="Inspector-Type-NetworkInterface-publicIp"></a>
The public IP address from which the network interface is reachable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** securityGroups **   <a name="Inspector-Type-NetworkInterface-securityGroups"></a>
A list of the security groups associated with the network interface. Includes the groupId and groupName.
Type: Array of [SecurityGroup](API_SecurityGroup.md) objects
Required: No

 ** subnetId **   <a name="Inspector-Type-NetworkInterface-subnetId"></a>
The ID of a subnet associated with the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** vpcId **   <a name="Inspector-Type-NetworkInterface-vpcId"></a>
The ID of a VPC associated with the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
