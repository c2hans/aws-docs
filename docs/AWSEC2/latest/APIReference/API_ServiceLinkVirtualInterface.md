---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ServiceLinkVirtualInterface.html
---

# ServiceLinkVirtualInterface
<a name="API_ServiceLinkVirtualInterface"></a>

Describes the service link virtual interfaces that establish connectivity between AWS Outpost and on-premises networks.

## Contents
<a name="API_ServiceLinkVirtualInterface_Contents"></a>

 ** configurationState **
The current state of the service link virtual interface.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** localAddress **
The IPv4 address assigned to the local gateway virtual interface on the Outpost side.
Type: String
Required: No

 ** outpostArn **
The Outpost Amazon Resource Number (ARN) for the service link virtual interface.
Type: String
Required: No

 ** outpostId **
The Outpost ID for the service link virtual interface.
Type: String
Required: No

 ** outpostLagId **
The link aggregation group (LAG) ID for the service link virtual interface.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the service link virtual interface..
Type: String
Required: No

 ** peerAddress **
The IPv4 peer address for the service link virtual interface.
Type: String
Required: No

 ** peerBgpAsn **
The ASN for the Border Gateway Protocol (BGP) associated with the service link virtual interface.
Type: Long
Required: No

 ** serviceLinkVirtualInterfaceArn **
The Amazon Resource Number (ARN) for the service link virtual interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** serviceLinkVirtualInterfaceId **
The ID of the service link virtual interface.
Type: String
Required: No

 ** TagSet.N **
The tags associated with the service link virtual interface.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vlan **
The virtual local area network for the service link virtual interface.
Type: Integer
Required: No

## See Also
<a name="API_ServiceLinkVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ServiceLinkVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ServiceLinkVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ServiceLinkVirtualInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
