---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData.html
---

# GetInstanceUefiData
<a name="API_GetInstanceUefiData"></a>

A binary representation of the UEFI variable store. Only non-volatile variables are stored. This is a base64 encoded and zlib compressed binary value that must be properly encoded.

When you use [register-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/register-image.html) to create an AMI, you can create an exact copy of your variable store by passing the UEFI data in the `UefiData` parameter. You can modify the UEFI data by using the [python-uefivars tool](https://github.com/awslabs/python-uefivars) on GitHub. You can use the tool to convert the UEFI data into a human-readable format (JSON), which you can inspect and modify, and then convert back into the binary format to use with register-image.

For more information, see [UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetInstanceUefiData_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance from which to retrieve the UEFI data.
Type: String
Required: Yes

## Response Elements
<a name="API_GetInstanceUefiData_ResponseElements"></a>

The following elements are returned by the service.

 **instanceId**
The ID of the instance from which to retrieve the UEFI data.
Type: String

 **requestId**
The ID of the request.
Type: String

 **uefiData**
Base64 representation of the non-volatile UEFI variable store.
Type: String

## Errors
<a name="API_GetInstanceUefiData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetInstanceUefiData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetInstanceUefiData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetInstanceUefiData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
