---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Ec2InstanceConnectEndpoint.html
---

# Ec2InstanceConnectEndpoint
<a name="API_Ec2InstanceConnectEndpoint"></a>

Describes an EC2 Instance Connect Endpoint.

## Contents
<a name="API_Ec2InstanceConnectEndpoint_Contents"></a>

 ** availabilityZone **
The Availability Zone of the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone of the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** createdAt **
The date and time that the EC2 Instance Connect Endpoint was created.
Type: Timestamp
Required: No

 ** dnsName **
The DNS name of the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** fipsDnsName **
The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** instanceConnectEndpointArn **
The Amazon Resource Name (ARN) of the EC2 Instance Connect Endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** instanceConnectEndpointId **
The ID of the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** ipAddressType **
The IP address type of the endpoint.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 ** NetworkInterfaceIdSet.N **
The ID of the elastic network interface that Amazon EC2 automatically created when creating the EC2 Instance Connect Endpoint.
Type: Array of strings
Required: No

 ** ownerId **
The ID of the AWS account that created the EC2 Instance Connect Endpoint.
Type: String
Required: No

 ** preserveClientIp **
Indicates whether your client's IP address is preserved as the source when you connect to a resource. The following are the possible values.
+  `true` - Use the IP address of the client. Your instance must have an IPv4 address.
+  `false` - Use the IP address of the network interface.
Default: `false`
Type: Boolean
Required: No

 ** publicDnsNames **
The public DNS names of the endpoint.
Type: [InstanceConnectEndpointPublicDnsNames](API_InstanceConnectEndpointPublicDnsNames.md) object
Required: No

 ** SecurityGroupIdSet.N **
The security groups associated with the endpoint. If you didn't specify a security group, the default security group for your VPC is associated with the endpoint.
Type: Array of strings
Required: No

 ** state **
The current state of the EC2 Instance Connect Endpoint.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | delete-in-progress | delete-complete | delete-failed | update-in-progress | update-complete | update-failed`
Required: No

 ** stateMessage **
The message for the current state of the EC2 Instance Connect Endpoint. Can include a failure message.
Type: String
Required: No

 ** subnetId **
The ID of the subnet in which the EC2 Instance Connect Endpoint was created.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the EC2 Instance Connect Endpoint.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC in which the EC2 Instance Connect Endpoint was created.
Type: String
Required: No

## See Also
<a name="API_Ec2InstanceConnectEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Ec2InstanceConnectEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Ec2InstanceConnectEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Ec2InstanceConnectEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
