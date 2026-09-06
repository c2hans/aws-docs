---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_VpcPeeringConnection.html
---

# VpcPeeringConnection
<a name="API_VpcPeeringConnection"></a>

Represents a peering connection between a VPC on one of your AWS accounts and the VPC for your Amazon GameLift Servers fleets. This record may be for an active peering connection or a pending connection that has not yet been established.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_VpcPeeringConnection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FleetArn **   <a name="gameliftservers-Type-VpcPeeringConnection-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift fleet resource for this connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-VpcPeeringConnection-FleetId"></a>
A unique identifier for the fleet. This ID determines the ID of the Amazon GameLift Servers VPC for your fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** GameLiftVpcId **   <a name="gameliftservers-Type-VpcPeeringConnection-GameLiftVpcId"></a>
A unique identifier for the VPC that contains the Amazon GameLift Servers fleet for this connection. This VPC is managed by Amazon GameLift Servers and does not appear in your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** IpV4CidrBlock **   <a name="gameliftservers-Type-VpcPeeringConnection-IpV4CidrBlock"></a>
CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC. The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot overlap or the peering connection cannot be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PeerVpcId **   <a name="gameliftservers-Type-VpcPeeringConnection-PeerVpcId"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Status **   <a name="gameliftservers-Type-VpcPeeringConnection-Status"></a>
The status information about the connection. Status indicates if a connection is pending, successful, or failed.
Type: [VpcPeeringConnectionStatus](API_VpcPeeringConnectionStatus.md) object
Required: No

 ** VpcPeeringConnectionId **   <a name="gameliftservers-Type-VpcPeeringConnection-VpcPeeringConnectionId"></a>
A unique identifier that is automatically assigned to the connection record. This ID is referenced in VPC peering connection events, and is used when deleting a connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/VpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/VpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/VpcPeeringConnection)
