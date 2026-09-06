---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroupReference.html
---

# SecurityGroupReference
<a name="API_SecurityGroupReference"></a>

Describes a VPC with a security group that references your security group.

## Contents
<a name="API_SecurityGroupReference_Contents"></a>

 ** groupId **
The ID of your security group.
Type: String
Required: No

 ** referencingVpcId **
The ID of the VPC with the referencing security group.
Type: String
Required: No

 ** transitGatewayId **
The ID of the transit gateway (if applicable).
Type: String
Required: No

 ** vpcPeeringConnectionId **
The ID of the VPC peering connection (if applicable). For more information about security group referencing for peering connections, see [Update your security groups to reference peer security groups](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html) in the *VPC Peering Guide*.
Type: String
Required: No

## See Also
<a name="API_SecurityGroupReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecurityGroupReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecurityGroupReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecurityGroupReference)
