---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnection.html
---

# VpcPeeringConnection

Describes a VPC peering connection.

## Contents
<a name="API_VpcPeeringConnection_Contents"></a>

 ** accepterVpcInfo **
Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.
Type: [VpcPeeringConnectionVpcInfo](API_VpcPeeringConnectionVpcInfo.md) object
Required: No

 ** expirationTime **
The time that an unaccepted VPC peering connection will expire.
Type: Timestamp
Required: No

 ** multipathResilienceStatus **
The multipath resilience status of the VPC peering connection. The possible values are:
+  `enabled` – Both the requester and the accepter allow multipath resilience.
+  `pending` – Either the requester or the accepter allows multipath resilience, but not both.
+  `disabled` – Neither the requester nor the accepter allows multipath resilience.
Type: String
Valid Values: `pending | enabled | disabled`
Required: No

 ** requesterVpcInfo **
Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.
Type: [VpcPeeringConnectionVpcInfo](API_VpcPeeringConnectionVpcInfo.md) object
Required: No

 ** status **
The status of the VPC peering connection.
Type: [VpcPeeringConnectionStateReason](API_VpcPeeringConnectionStateReason.md) object
Required: No

 ** TagSet.N **
Any tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcPeeringConnectionId **
The ID of the VPC peering connection.
Type: String
Required: No

## See Also
<a name="API_VpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcPeeringConnection)
