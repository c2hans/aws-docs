---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayVirtualInterface.html
---

# LocalGatewayVirtualInterface
<a name="API_LocalGatewayVirtualInterface"></a>

Describes a local gateway virtual interface.

## Contents
<a name="API_LocalGatewayVirtualInterface_Contents"></a>

 ** configurationState **
The current state of the local gateway virtual interface.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** localAddress **
The local address.
Type: String
Required: No

 ** localBgpAsn **
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.
Type: Integer
Required: No

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** localGatewayVirtualInterfaceArn **
The Amazon Resource Number (ARN) of the local gateway virtual interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayVirtualInterfaceGroupId **
The ID of the local gateway virtual interface group.
Type: String
Required: No

 ** localGatewayVirtualInterfaceId **
The ID of the virtual interface.
Type: String
Required: No

 ** outpostLagId **
The Outpost LAG ID.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway virtual interface.
Type: String
Required: No

 ** peerAddress **
The peer address.
Type: String
Required: No

 ** peerBgpAsn **
The peer BGP ASN.
Type: Integer
Required: No

 ** peerBgpAsnExtended **
The extended 32-bit ASN of the BGP peer for use with larger ASN values.
Type: Long
Required: No

 ** TagSet.N **
The tags assigned to the virtual interface.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vlan **
The ID of the VLAN.
Type: Integer
Required: No

## See Also
<a name="API_LocalGatewayVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayVirtualInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
