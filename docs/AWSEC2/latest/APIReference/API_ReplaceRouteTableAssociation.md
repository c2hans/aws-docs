---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRouteTableAssociation.html
---

# ReplaceRouteTableAssociation
<a name="API_ReplaceRouteTableAssociation"></a>

Changes the route table associated with a given subnet, internet gateway, or virtual private gateway in a VPC. After the operation completes, the subnet or gateway uses the routes in the new route table. For more information about route tables, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon VPC User Guide*.

You can also use this operation to change which table is the main route table in the VPC. Specify the main route table's association ID and the route table ID of the new main route table.

## Request Parameters
<a name="API_ReplaceRouteTableAssociation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The association ID.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RouteTableId**
The ID of the new route table to associate with the subnet.
Type: String
Required: Yes

## Response Elements
<a name="API_ReplaceRouteTableAssociation_ResponseElements"></a>

The following elements are returned by the service.

 **associationState**
The state of the association.
Type: [RouteTableAssociationState](API_RouteTableAssociationState.md) object

 **newAssociationId**
The ID of the new association.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ReplaceRouteTableAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReplaceRouteTableAssociation_Examples"></a>

### Example
<a name="API_ReplaceRouteTableAssociation_Example_1"></a>

This example starts with a route table associated with a subnet, and a corresponding association ID `rtbassoc-04ca27a6914a0b4f`. You want to associate a different route table (table `rtb-1a2b3c4d1a2b3c4d1`) to the subnet. The result is a new association ID representing the new association.

#### Sample Request
<a name="API_ReplaceRouteTableAssociation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReplaceRouteTableAssociation
&AssociationId=rtbassoc-04ca27a6914a0b4f
&RouteTableId=rtb-1a2b3c4d1a2b3c4d1
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReplaceRouteTableAssociation_Example_1_Response"></a>

```
<ReplaceRouteTableAssociationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <newAssociationId>rtbassoc-11223344556677889</newAssociationId>
</ReplaceRouteTableAssociationResponse>
```

## See Also
<a name="API_ReplaceRouteTableAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReplaceRouteTableAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReplaceRouteTableAssociation)
