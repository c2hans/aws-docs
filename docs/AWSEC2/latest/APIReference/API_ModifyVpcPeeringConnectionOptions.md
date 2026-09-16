---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcPeeringConnectionOptions.html
---

# ModifyVpcPeeringConnectionOptions
<a name="API_ModifyVpcPeeringConnectionOptions"></a>

Modifies the VPC peering connection options on one side of a VPC peering connection.

If the peered VPCs are in the same AWS account, you can enable DNS resolution for queries from the local VPC. This ensures that queries from the local VPC resolve to private IP addresses in the peer VPC. This option is not available if the peered VPCs are in different AWS accounts or different Regions. For peered VPCs in different AWS accounts, each AWS account owner must initiate a separate request to modify the peering connection options. For inter-region peering connections, you must use the Region for the requester VPC to modify the requester VPC peering options and the Region for the accepter VPC to modify the accepter VPC peering options. To verify which VPCs are the accepter and the requester for a VPC peering connection, use the [DescribeVpcPeeringConnections](API_DescribeVpcPeeringConnections.md) command.

## Request Parameters
<a name="API_ModifyVpcPeeringConnectionOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AccepterPeeringConnectionOptions**
The VPC peering connection options for the accepter VPC.
Type: [PeeringConnectionOptionsRequest](API_PeeringConnectionOptionsRequest.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RequesterPeeringConnectionOptions**
The VPC peering connection options for the requester VPC.
Type: [PeeringConnectionOptionsRequest](API_PeeringConnectionOptionsRequest.md) object
Required: No

 **VpcPeeringConnectionId**
The ID of the VPC peering connection.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcPeeringConnectionOptions_ResponseElements"></a>

The following elements are returned by the service.

 **accepterPeeringConnectionOptions**
Information about the VPC peering connection options for the accepter VPC.
Type: [PeeringConnectionOptions](API_PeeringConnectionOptions.md) object

 **requesterPeeringConnectionOptions**
Information about the VPC peering connection options for the requester VPC.
Type: [PeeringConnectionOptions](API_PeeringConnectionOptions.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyVpcPeeringConnectionOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcPeeringConnectionOptions_Examples"></a>

### Example
<a name="API_ModifyVpcPeeringConnectionOptions_Example_1"></a>

In this example, you want the public DNS hostnames of your instances in your VPC to resolve to private IP addresses when queried from instances in the peer VPC. You were the accepter of the VPC peering connection, therefore you modify the accepter VPC peering connection options.

#### Sample Request
<a name="API_ModifyVpcPeeringConnectionOptions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcPeeringConnectionOptions
&VpcPeeringConnectionId=pcx-1a2b3c4d
&AccepterPeeringConnectionOptions.AllowDnsResolutionFromRemoteVpc=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcPeeringConnectionOptions_Example_1_Response"></a>

```
<ModifyVpcPeeringConnectionOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>f5131846-7920-4359-b565-example</requestId>
  <accepterPeeringConnectionOptions>
    <allowDnsResolutionFromRemoteVpc>true</allowDnsResolutionFromRemoteVpc>
  </accepterPeeringConnectionOptions>
</ModifyVpcPeeringConnectionOptionsResponse>
```

## See Also
<a name="API_ModifyVpcPeeringConnectionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)
