---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

Contains information about the elastic network interface of the EC2 instance.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** ipv6Addresses **   <a name="guardduty-Type-NetworkInterface-ipv6Addresses"></a>
A list of IPv6 addresses for the EC2 instance.
Type: Array of strings
Required: No

 ** networkInterfaceId **   <a name="guardduty-Type-NetworkInterface-networkInterfaceId"></a>
The ID of the network interface.
Type: String
Required: No

 ** privateDnsName **   <a name="guardduty-Type-NetworkInterface-privateDnsName"></a>
The private DNS name of the EC2 instance.
Type: String
Required: No

 ** privateIpAddress **   <a name="guardduty-Type-NetworkInterface-privateIpAddress"></a>
The private IP address of the EC2 instance.
Type: String
Required: No

 ** privateIpAddresses **   <a name="guardduty-Type-NetworkInterface-privateIpAddresses"></a>
Other private IP address information of the EC2 instance.
Type: Array of [PrivateIpAddressDetails](API_PrivateIpAddressDetails.md) objects
Required: No

 ** publicDnsName **   <a name="guardduty-Type-NetworkInterface-publicDnsName"></a>
The public DNS name of the EC2 instance.
Type: String
Required: No

 ** publicIp **   <a name="guardduty-Type-NetworkInterface-publicIp"></a>
The public IP address of the EC2 instance.
Type: String
Required: No

 ** securityGroups **   <a name="guardduty-Type-NetworkInterface-securityGroups"></a>
The security groups associated with the EC2 instance.
Type: Array of [SecurityGroup](API_SecurityGroup.md) objects
Required: No

 ** subnetId **   <a name="guardduty-Type-NetworkInterface-subnetId"></a>
The subnet ID of the EC2 instance.
Type: String
Required: No

 ** vpcId **   <a name="guardduty-Type-NetworkInterface-vpcId"></a>
The VPC ID of the EC2 instance.
Type: String
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
