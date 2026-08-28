---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFpgaImage.html
---

# DeleteFpgaImage
<a name="API_DeleteFpgaImage"></a>

Deletes the specified Amazon FPGA Image (AFI).

## Request Parameters
<a name="API_DeleteFpgaImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FpgaImageId**
The ID of the AFI.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteFpgaImage_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteFpgaImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteFpgaImage_Examples"></a>

### Example
<a name="API_DeleteFpgaImage_Example_1"></a>

This example deletes the specified AFI.

#### Sample Request
<a name="API_DeleteFpgaImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteFpgaImage
&FpgaImageId=afi-0d123e21abcc85abc
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteFpgaImage_Example_1_Response"></a>

```
<DeleteFpgaImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>dd3bf051-468e-4490-ad8a-2ffexample</requestId>
    <return>true</return>
</DeleteFpgaImageResponse>
```

## See Also
<a name="API_DeleteFpgaImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteFpgaImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteFpgaImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
