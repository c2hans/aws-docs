---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecondaryNetwork.html
---

# SecondaryNetwork
<a name="API_SecondaryNetwork"></a>

Describes a secondary network.

## Contents
<a name="API_SecondaryNetwork_Contents"></a>

 ** Ipv4CidrBlockAssociationSet.N **
Information about the IPv4 CIDR blocks associated with the secondary network.
Type: Array of [SecondaryNetworkIpv4CidrBlockAssociation](API_SecondaryNetworkIpv4CidrBlockAssociation.md) objects
Required: No

 ** ownerId **
The ID of the AWS account that owns the secondary network.
Type: String
Required: No

 ** secondaryNetworkArn **
The Amazon Resource Name (ARN) of the secondary network.
Type: String
Required: No

 ** secondaryNetworkId **
The ID of the secondary network.
Type: String
Required: No

 ** state **
The state of the secondary network.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | delete-in-progress | delete-complete | delete-failed`
Required: No

 ** stateReason **
The reason for the current state of the secondary network.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the secondary network.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** type **
The type of the secondary network.
Type: String
Valid Values: `rdma`
Required: No

## See Also
<a name="API_SecondaryNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecondaryNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecondaryNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecondaryNetwork)
