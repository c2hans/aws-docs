---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetInstanceAttribute.html
---

# ResetInstanceAttribute
<a name="API_ResetInstanceAttribute"></a>

Resets an attribute of an instance to its default value. To reset the `kernel` or `ramdisk`, the instance must be in a stopped state. To reset the `sourceDestCheck`, the instance can be either running or stopped.

The `sourceDestCheck` attribute controls whether source/destination checking is enabled. The default value is `true`, which means checking is enabled. This value must be `false` for a NAT instance to perform NAT. For more information, see [NAT instances](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_ResetInstanceAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The attribute to reset.
Type: String
Valid Values: `kernel | ramdisk | sourceDestCheck`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

## Response Elements
<a name="API_ResetInstanceAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ResetInstanceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ResetInstanceAttribute_Examples"></a>

### Example
<a name="API_ResetInstanceAttribute_Example_1"></a>

This example resets the `sourceDestCheck` attribute.

#### Sample Request
<a name="API_ResetInstanceAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ResetInstanceAttribute
&InstanceId=i-1234567890abcdef0
&Attribute=sourceDestCheck
&AUTHPARAMS
```

#### Sample Response
<a name="API_ResetInstanceAttribute_Example_1_Response"></a>

```
<ResetInstanceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</ResetInstanceAttributeResponse>
```

## See Also
<a name="API_ResetInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ResetInstanceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResetInstanceAttribute)
