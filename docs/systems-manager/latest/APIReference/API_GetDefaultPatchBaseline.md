---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDefaultPatchBaseline.html
---

# GetDefaultPatchBaseline
<a name="API_GetDefaultPatchBaseline"></a>

Retrieves the default patch baseline. AWS Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.

If you don't specify an operating system value, the default patch baseline for Windows is returned.

## Request Syntax
<a name="API_GetDefaultPatchBaseline_RequestSyntax"></a>

```
{
   "OperatingSystem": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDefaultPatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OperatingSystem](#API_GetDefaultPatchBaseline_RequestSyntax) **   <a name="systemsmanager-GetDefaultPatchBaseline-request-OperatingSystem"></a>
Returns the default patch baseline for the specified operating system.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`
Required: No

## Response Syntax
<a name="API_GetDefaultPatchBaseline_ResponseSyntax"></a>

```
{
   "BaselineId": "string",
   "OperatingSystem": "string"
}
```

## Response Elements
<a name="API_GetDefaultPatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineId](#API_GetDefaultPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetDefaultPatchBaseline-response-BaselineId"></a>
The ID of the default patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

 ** [OperatingSystem](#API_GetDefaultPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetDefaultPatchBaseline-response-OperatingSystem"></a>
The operating system for the returned patch baseline.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`

## Errors
<a name="API_GetDefaultPatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetDefaultPatchBaseline_Examples"></a>

### Example
<a name="API_GetDefaultPatchBaseline_Example_1"></a>

This example illustrates one usage of GetDefaultPatchBaseline.

#### Sample Request
<a name="API_GetDefaultPatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 35
X-Amz-Target: AmazonSSM.GetDefaultPatchBaseline
X-Amz-Date: 20240309T025228Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "OperatingSystem": "AMAZON_LINUX"
}
```

#### Sample Response
<a name="API_GetDefaultPatchBaseline_Example_1_Response"></a>

```
{
    "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-0c10e65780EXAMPLE",
    "OperatingSystem": "AMAZON_LINUX"
}
```

## See Also
<a name="API_GetDefaultPatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetDefaultPatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetDefaultPatchBaseline)
