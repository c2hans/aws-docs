---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteDhcpOptions.html
---

# DeleteDhcpOptions
<a name="API_DeleteDhcpOptions"></a>

Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC.

## Request Parameters
<a name="API_DeleteDhcpOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DhcpOptionsId**
The ID of the DHCP options set.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteDhcpOptions_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteDhcpOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteDhcpOptions_Examples"></a>

### Example
<a name="API_DeleteDhcpOptions_Example_1"></a>

This example deletes the specified set of DHCP options.

#### Sample Request
<a name="API_DeleteDhcpOptions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteDhcpOptions
&DhcpOptionsId=dopt-7a8b9c2d
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteDhcpOptions_Example_1_Response"></a>

```
<DeleteDhcpOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</DeleteDhcpOptionsResponse>
```

## See Also
<a name="API_DeleteDhcpOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteDhcpOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteDhcpOptions)
