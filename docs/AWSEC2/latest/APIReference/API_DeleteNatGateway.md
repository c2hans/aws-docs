---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNatGateway.html
---

# DeleteNatGateway
<a name="API_DeleteNatGateway"></a>

Deletes the specified NAT gateway. Deleting a public NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables.

## Request Parameters
<a name="API_DeleteNatGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NatGatewayId**
The ID of the NAT gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteNatGateway_ResponseElements"></a>

The following elements are returned by the service.

 **natGatewayId**
The ID of the NAT gateway.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteNatGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteNatGateway_Examples"></a>

### Example
<a name="API_DeleteNatGateway_Example_1"></a>

This example deletes NAT gateway nat-04ae55e711cec5680.

#### Sample Request
<a name="API_DeleteNatGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteNatGateway
&NatGatewayId=nat-04ae55e711cec5680
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteNatGateway_Example_1_Response"></a>

```
<DeleteNatGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>741fc8ab-6ebe-452b-b92b-example</requestId>
    <natGatewayId>nat-04ae55e711cec5680</natGatewayId>
</DeleteNatGatewayResponse>
```

## See Also
<a name="API_DeleteNatGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteNatGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteNatGateway)
