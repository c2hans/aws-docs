---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcPeeringConnection.html
---

# CreateVpcPeeringConnection
<a name="API_CreateVpcPeeringConnection"></a>

Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another AWS account and can be in a different Region to the requester VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks.

**Note**
Limitations and rules apply to a VPC peering connection. For more information, see the [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations) in the *VPC Peering Guide*.

The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected.

If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of `failed`.

## Request Parameters
<a name="API_CreateVpcPeeringConnection_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PeerOwnerId**
The AWS account ID of the owner of the accepter VPC.
Default: Your AWS account ID
Type: String
Required: No

 **PeerRegion**
The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.
Default: The Region in which you make the request.
Type: String
Required: No

 **PeerVpcId**
The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.
Type: String
Required: No

 **TagSpecification.N**
The tags to assign to the peering connection.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the requester VPC. You must specify this parameter in the request.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateVpcPeeringConnection_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpcPeeringConnection**
Information about the VPC peering connection.
Type: [VpcPeeringConnection](API_VpcPeeringConnection.md) object

## Errors
<a name="API_CreateVpcPeeringConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpcPeeringConnection_Examples"></a>

### Example 1
<a name="API_CreateVpcPeeringConnection_Example_1"></a>

This example requests a peering connection between your VPC (`vpc-1a2b3c4d`), and a VPC (`vpc-a1b2c3d4`) that belongs to AWS account 123456789012.

#### Sample Request
<a name="API_CreateVpcPeeringConnection_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcPeeringConnection
&VpcId=vpc-1a2b3c4d
&PeerVpcId=vpc-a1b2c3d4
&PeerOwnerId=123456789012
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpcPeeringConnection_Example_1_Response"></a>

```
<CreateVpcPeeringConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
 <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
 <vpcPeeringConnection>
  <vpcPeeringConnectionId>pcx-73a5401a</vpcPeeringConnectionId>
    <requesterVpcInfo>
     <ownerId>777788889999</ownerId>
     <vpcId>vpc-1a2b3c4d</vpcId>
     <cidrBlock>10.0.0.0/28</cidrBlock>
     <peeringOptions>
       <allowEgressFromLocalClassicLinkToRemoteVpc>false</allowEgressFromLocalClassicLinkToRemoteVpc>
       <allowEgressFromLocalVpcToRemoteClassicLink>false</allowEgressFromLocalVpcToRemoteClassicLink>
       <allowDnsResolutionFromRemoteVpc>false</allowDnsResolutionFromRemoteVpc>
     </peeringOptions>
    </requesterVpcInfo>
    <accepterVpcInfo>
      <ownerId>123456789012</ownerId>
      <vpcId>vpc-a1b2c3d4</vpcId>
    </accepterVpcInfo>
    <status>
     <code>initiating-request</code>
     <message>Initiating Request to 123456789012</message>
    </status>
    <expirationTime>2014-02-18T14:37:25.000Z</expirationTime>
    <tagSet/>
 </vpcPeeringConnection>
</CreateVpcPeeringConnectionResponse>
```

### Example 2
<a name="API_CreateVpcPeeringConnection_Example_2"></a>

This example requests a peering connection between your VPCs `vpc-1a2b3c4d` and `vpc-11122233`.

#### Sample Request
<a name="API_CreateVpcPeeringConnection_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcPeeringConnection
&VpcId=vpc-1a2b3c4d
&PeerVpcId=vpc-11122233
&AUTHPARAMS
```

### Example 3
<a name="API_CreateVpcPeeringConnection_Example_3"></a>

This example requests an inter-region peering connection between two VPCs in your account. VPC `vpc-1a2b3c4d` is located in the US East (N. Virginia) Region (`us-east-1`), and accepter VPC `vpc-a1b2c3d4` is located in the US West (Oregon) Region (`us-west-2`). The VPC peering connection must be accepted in the `us-west-2` Region.

#### Sample Request
<a name="API_CreateVpcPeeringConnection_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcPeeringConnection
&VpcId=vpc-1a2b3c4d
&PeerVpcId=vpc-a1b2c3d4
&PeerRegion=us-west-2
&AUTHPARAMS
```

## See Also
<a name="API_CreateVpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpcPeeringConnection)
