---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcPeeringConnection.html
---

# RejectVpcPeeringConnection
<a name="API_RejectVpcPeeringConnection"></a>

Rejects a VPC peering connection request. The VPC peering connection must be in the `pending-acceptance` state. Use the [DescribeVpcPeeringConnections](API_DescribeVpcPeeringConnections.md) request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use [DeleteVpcPeeringConnection](API_DeleteVpcPeeringConnection.md).

## Request Parameters
<a name="API_RejectVpcPeeringConnection_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpcPeeringConnectionId**
The ID of the VPC peering connection.
Type: String
Required: Yes

## Response Elements
<a name="API_RejectVpcPeeringConnection_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_RejectVpcPeeringConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RejectVpcPeeringConnection_Examples"></a>

### Example
<a name="API_RejectVpcPeeringConnection_Example_1"></a>

This example rejects the specified VPC peering connection request.

#### Sample Request
<a name="API_RejectVpcPeeringConnection_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RejectVpcPeeringConnection
&vpcPeeringConnectionId=pcx-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_RejectVpcPeeringConnection_Example_1_Response"></a>

```
<RejectVpcPeeringConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</RejectVpcPeeringConnectionResponse>
```

## See Also
<a name="API_RejectVpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RejectVpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RejectVpcPeeringConnection)
