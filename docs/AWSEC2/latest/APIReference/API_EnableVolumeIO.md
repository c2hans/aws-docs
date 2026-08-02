---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVolumeIO.html
---

# EnableVolumeIO
<a name="API_EnableVolumeIO"></a>

Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.

## Request Parameters
<a name="API_EnableVolumeIO_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VolumeId**
The ID of the volume.
Type: String
Required: Yes

## Response Elements
<a name="API_EnableVolumeIO_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_EnableVolumeIO_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableVolumeIO_Examples"></a>

### Example
<a name="API_EnableVolumeIO_Example_1"></a>

This example enables the I/O operations of the volume vol-8888888.

#### Sample Request
<a name="API_EnableVolumeIO_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableVolumeIO
&VolumeId= vol-8888888
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableVolumeIO_Example_1_Response"></a>

```
<EnableVolumeIOResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</EnableVolumeIOResponse>
```

## See Also
<a name="API_EnableVolumeIO_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableVolumeIO)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableVolumeIO)
