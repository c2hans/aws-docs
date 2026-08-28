---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImage.html
---

# EnableImage
<a name="API_EnableImage"></a>

Re-enables a disabled AMI. The re-enabled AMI is marked as `available` and can be used for instance launches, appears in describe operations, and can be shared. AWS accounts, organizations, and Organizational Units that lost access to the AMI when it was disabled do not regain access automatically. Once the AMI is available, it can be shared with them again.

Only the AMI owner can re-enable a disabled AMI.

For more information, see [Disable an Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_EnableImage_RequestParameters"></a>

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
<a name="API_EnableImage_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_EnableImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableImage_Examples"></a>

### Example
<a name="API_EnableImage_Example_1"></a>

This example enables the specified AMI.

#### Sample Request
<a name="API_EnableImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableImage
&ImageId=ami-0123456789EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableImage_Example_1_Response"></a>

```
<EnableImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>11aabb229-4eac-35bd-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</EnableImageResponse>
```

## See Also
<a name="API_EnableImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
