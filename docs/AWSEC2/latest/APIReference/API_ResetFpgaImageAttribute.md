---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetFpgaImageAttribute.html
---

# ResetFpgaImageAttribute
<a name="API_ResetFpgaImageAttribute"></a>

Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute.

## Request Parameters
<a name="API_ResetFpgaImageAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The attribute.
Type: String
Valid Values: `loadPermission`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FpgaImageId**
The ID of the AFI.
Type: String
Required: Yes

## Response Elements
<a name="API_ResetFpgaImageAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ResetFpgaImageAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ResetFpgaImageAttribute_Examples"></a>

### Example
<a name="API_ResetFpgaImageAttribute_Example_1"></a>

This example resets the load permissions for the specified AFI.

#### Sample Request
<a name="API_ResetFpgaImageAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ResetFpgaImageAttribute
&FpgaImageId=afi-0d123e21abcc85abc
&Attribute=loadPermission
&AUTHPARAMS
```

#### Sample Response
<a name="API_ResetFpgaImageAttribute_Example_1_Response"></a>

```
<ResetFpgaImageAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ccb58a32-30ee-4f9b-831c-639example</requestId>
    <return>true</return>
</ResetFpgaImageAttributeResponse>
```

## See Also
<a name="API_ResetFpgaImageAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ResetFpgaImageAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResetFpgaImageAttribute)
