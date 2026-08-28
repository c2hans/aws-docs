---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TrunkInterfaceAssociation.html
---

# TrunkInterfaceAssociation
<a name="API_TrunkInterfaceAssociation"></a>

Information about an association between a branch network interface with a trunk network interface.

## Contents
<a name="API_TrunkInterfaceAssociation_Contents"></a>

 ** associationId **
The ID of the association.
Type: String
Required: No

 ** branchInterfaceId **
The ID of the branch network interface.
Type: String
Required: No

 ** greKey **
The application key when you use the GRE protocol.
Type: Integer
Required: No

 ** interfaceProtocol **
The interface protocol. Valid values are `VLAN` and `GRE`.
Type: String
Valid Values: `VLAN | GRE`
Required: No

 ** TagSet.N **
The tags for the trunk interface association.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trunkInterfaceId **
The ID of the trunk network interface.
Type: String
Required: No

 ** vlanId **
The ID of the VLAN when you use the VLAN protocol.
Type: Integer
Required: No

## See Also
<a name="API_TrunkInterfaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TrunkInterfaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TrunkInterfaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TrunkInterfaceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
