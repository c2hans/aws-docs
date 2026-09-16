---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html
---

# DeleteNetworkInterface
<a name="API_DeleteNetworkInterface"></a>

Deletes the specified network interface. You must detach the network interface before you can delete it.

## Request Parameters
<a name="API_DeleteNetworkInterface_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteNetworkInterface_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteNetworkInterface_Examples"></a>

### Example
<a name="API_DeleteNetworkInterface_Example_1"></a>

This example deletes the specified network interface.

#### Sample Request
<a name="API_DeleteNetworkInterface_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteNetworkInterface
&NetworkInterfaceId=eni-ffda3197
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteNetworkInterface_Example_1_Response"></a>

```
<DeleteNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e1c6d73b-edaa-4e62-9909-6611404e1739</requestId>
    <return>true</return>
</DeleteNetworkInterfaceResponse>
```

## See Also
<a name="API_DeleteNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteNetworkInterface)
