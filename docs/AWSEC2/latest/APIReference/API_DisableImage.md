---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImage.html
---

# DisableImage
<a name="API_DisableImage"></a>

Sets the AMI state to `disabled` and removes all launch permissions from the AMI. A disabled AMI can't be used for instance launches.

A disabled AMI can't be shared. If an AMI was public or previously shared, it is made private. If an AMI was shared with an AWS account, organization, or Organizational Unit, they lose access to the disabled AMI.

A disabled AMI does not appear in [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) API calls by default.

Only the AMI owner can disable an AMI.

You can re-enable a disabled AMI using [EnableImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImage.html).

For more information, see [Disable an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DisableImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

## Response Elements
<a name="API_DisableImage_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_DisableImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableImage_Examples"></a>

### Example
<a name="API_DisableImage_Example_1"></a>

This example disables the specified AMI.

#### Sample Request
<a name="API_DisableImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableImage
&ImageId=ami-0123456789EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableImage_Example_1_Response"></a>

```
<DisableImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>11aabb229-4eac-35bd-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</DisableImageResponse>
```

## See Also
<a name="API_DisableImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableImage)
