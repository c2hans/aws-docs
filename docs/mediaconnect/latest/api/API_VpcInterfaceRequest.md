---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_VpcInterfaceRequest.html
---

# VpcInterfaceRequest
<a name="API_VpcInterfaceRequest"></a>

The details of the VPC interfaces that you want to add to the flow.

## Contents
<a name="API_VpcInterfaceRequest_Contents"></a>

 ** name **   <a name="mediaconnect-Type-VpcInterfaceRequest-name"></a>
The name for the VPC interface. This name must be unique within the flow.
Type: String
Required: Yes

 ** roleArn **   <a name="mediaconnect-Type-VpcInterfaceRequest-roleArn"></a>
The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.
Type: String
Required: Yes

 ** securityGroupIds **   <a name="mediaconnect-Type-VpcInterfaceRequest-securityGroupIds"></a>
A virtual firewall to control inbound and outbound traffic.
Type: Array of strings
Required: Yes

 ** subnetId **   <a name="mediaconnect-Type-VpcInterfaceRequest-subnetId"></a>
 The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.
Type: String
Required: Yes

 ** networkInterfaceType **   <a name="mediaconnect-Type-VpcInterfaceRequest-networkInterfaceType"></a>
The type of network interface.
Type: String
Valid Values: `ena | efa`
Required: No

 ** vpcInterfaceTags **   <a name="mediaconnect-Type-VpcInterfaceRequest-vpcInterfaceTags"></a>
 The key-value pairs that can be used to tag and organize the VPC network interface.
Type: String to string map
Required: No

## See Also
<a name="API_VpcInterfaceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/VpcInterfaceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/VpcInterfaceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/VpcInterfaceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
