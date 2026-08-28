---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayVirtualInterfaceGroup.html
---

# LocalGatewayVirtualInterfaceGroup
<a name="API_LocalGatewayVirtualInterfaceGroup"></a>

Describes a local gateway virtual interface group.

## Contents
<a name="API_LocalGatewayVirtualInterfaceGroup_Contents"></a>

 ** configurationState **
The current state of the local gateway virtual interface group.
Type: String
Valid Values: `pending | incomplete | available | deleting | deleted`
Required: No

 ** localBgpAsn **
The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).
Type: Integer
Required: No

 ** localBgpAsnExtended **
The extended 32-bit ASN for the local BGP configuration.
Type: Long
Required: No

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** localGatewayVirtualInterfaceGroupArn **
The Amazon Resource Number (ARN) of the local gateway virtual interface group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayVirtualInterfaceGroupId **
The ID of the virtual interface group.
Type: String
Required: No

 ** LocalGatewayVirtualInterfaceIdSet.N **
The IDs of the virtual interfaces.
Type: Array of strings
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway virtual interface group.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the virtual interface group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LocalGatewayVirtualInterfaceGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayVirtualInterfaceGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayVirtualInterfaceGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayVirtualInterfaceGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
