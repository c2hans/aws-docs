---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Ec2NetworkInterface.html
---

# Ec2NetworkInterface
<a name="API_Ec2NetworkInterface"></a>

Contains information about the elastic network interface of the Amazon EC2 instance.

## Contents
<a name="API_Ec2NetworkInterface_Contents"></a>

 ** ipv6Addresses **   <a name="guardduty-Type-Ec2NetworkInterface-ipv6Addresses"></a>
A list of IPv6 addresses for the Amazon EC2 instance.
Type: Array of strings
Required: No

 ** privateIpAddresses **   <a name="guardduty-Type-Ec2NetworkInterface-privateIpAddresses"></a>
Other private IP address information of the Amazon EC2 instance.
Type: Array of [PrivateIpAddressDetails](API_PrivateIpAddressDetails.md) objects
Required: No

 ** publicIp **   <a name="guardduty-Type-Ec2NetworkInterface-publicIp"></a>
The public IP address of the Amazon EC2 instance.
Type: String
Required: No

 ** securityGroups **   <a name="guardduty-Type-Ec2NetworkInterface-securityGroups"></a>
The security groups associated with the Amazon EC2 instance.
Type: Array of [SecurityGroup](API_SecurityGroup.md) objects
Required: No

 ** subNetId **   <a name="guardduty-Type-Ec2NetworkInterface-subNetId"></a>
The subnet ID of the Amazon EC2 instance.
Type: String
Required: No

 ** vpcId **   <a name="guardduty-Type-Ec2NetworkInterface-vpcId"></a>
The VPC ID of the Amazon EC2 instance.
Type: String
Required: No

## See Also
<a name="API_Ec2NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Ec2NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Ec2NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Ec2NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
