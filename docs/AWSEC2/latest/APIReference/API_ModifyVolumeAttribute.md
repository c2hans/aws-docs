---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolumeAttribute.html
---

# ModifyVolumeAttribute
<a name="API_ModifyVolumeAttribute"></a>

Modifies a volume attribute.

By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume.

You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.

## Request Parameters
<a name="API_ModifyVolumeAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AutoEnableIO**
Indicates whether the volume should be auto-enabled for I/O operations.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VolumeId**
The ID of the volume.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVolumeAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyVolumeAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVolumeAttribute_Examples"></a>

### Example
<a name="API_ModifyVolumeAttribute_Example_1"></a>

This example modifies the attribute of the volume vol-1234567890abcdef0.

#### Sample Request
<a name="API_ModifyVolumeAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVolumeAttribute
&VolumeId=vol-1234567890abcdef0
&AutoEnableIO.Value=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVolumeAttribute_Example_1_Response"></a>

```
<ModifyVolumeAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
   <return>true</return>
</ModifyVolumeAttributeResponse>
```

## See Also
<a name="API_ModifyVolumeAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVolumeAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVolumeAttribute)
