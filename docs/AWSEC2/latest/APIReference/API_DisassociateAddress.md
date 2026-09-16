---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateAddress.html
---

# DisassociateAddress
<a name="API_DisassociateAddress"></a>

Disassociates an Elastic IP address from the instance or network interface it's associated with.

This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.

An address cannot be disassociated if the all of the following conditions are met:
+ Network interface has a `publicDualStackDnsName` publicDnsName
+ Public IPv4 address is the primary public IPv4 address
+ Network interface only has one remaining public IPv4 address

## Request Parameters
<a name="API_DisassociateAddress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The association ID. This parameter is required.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PublicIp**
Deprecated.
Type: String
Required: No

## Response Elements
<a name="API_DisassociateAddress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DisassociateAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateAddress_Examples"></a>

### Example
<a name="API_DisassociateAddress_Example_1"></a>

This example disassociates the specified Elastic IP address from the instance to which it is associated.

#### Sample Request
<a name="API_DisassociateAddress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateAddress
&AssociationId=eipassoc-aa7486c3
&AUTHPARAMS
```

## See Also
<a name="API_DisassociateAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateAddress)
