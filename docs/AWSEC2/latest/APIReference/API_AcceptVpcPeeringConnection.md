---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcPeeringConnection.html
---

# AcceptVpcPeeringConnection
<a name="API_AcceptVpcPeeringConnection"></a>

Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the `pending-acceptance` state, and you must be the owner of the peer VPC. Use [DescribeVpcPeeringConnections](API_DescribeVpcPeeringConnections.md) to view your outstanding VPC peering connection requests.

For an inter-Region VPC peering connection request, you must accept the VPC peering connection in the Region of the accepter VPC.

## Request Parameters
<a name="API_AcceptVpcPeeringConnection_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpcPeeringConnectionId**
The ID of the VPC peering connection. You must specify this parameter in the request.
Type: String
Required: Yes

## Response Elements
<a name="API_AcceptVpcPeeringConnection_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpcPeeringConnection**
Information about the VPC peering connection.
Type: [VpcPeeringConnection](API_VpcPeeringConnection.md) object

## Errors
<a name="API_AcceptVpcPeeringConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AcceptVpcPeeringConnection_Examples"></a>

### Example
<a name="API_AcceptVpcPeeringConnection_Example_1"></a>

This example accepts the specified VPC peering connection request.

#### Sample Request
<a name="API_AcceptVpcPeeringConnection_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AcceptVpcPeeringConnection
&VpcPeeringConnectionId=pcx-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_AcceptVpcPeeringConnection_Example_1_Response"></a>

```
<AcceptVpcPeeringConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <vpcPeeringConnection>
   <vpcPeeringConnectionId>pcx-1a2b3c4d</vpcPeeringConnectionId>
   <requesterVpcInfo>
     <ownerId>123456789012</ownerId>
     <vpcId>vpc-1a2b3c4d</vpcId>
     <cidrBlock>10.0.0.0/28</cidrBlock>
   </requesterVpcInfo>
   <accepterVpcInfo>
     <ownerId>777788889999</ownerId>
     <vpcId>vpc-111aaa22</vpcId>
     <cidrBlock>10.0.1.0/28</cidrBlock>
     <peeringOptions>
       <allowEgressFromLocalClassicLinkToRemoteVpc>false</allowEgressFromLocalClassicLinkToRemoteVpc>
       <allowEgressFromLocalVpcToRemoteClassicLink>false</allowEgressFromLocalVpcToRemoteClassicLink>
       <allowDnsResolutionFromRemoteVpc>false</allowDnsResolutionFromRemoteVpc>
     </peeringOptions>
   </accepterVpcInfo>
   <status>
     <code>active</code>
     <message>Active</message>
    </status>
   <tagSet/>
  </vpcPeeringConnection>
 </AcceptVpcPeeringConnectionResponse>"
```

## See Also
<a name="API_AcceptVpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AcceptVpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AcceptVpcPeeringConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
