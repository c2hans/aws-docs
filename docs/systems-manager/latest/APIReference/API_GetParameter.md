---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html
---

# GetParameter
<a name="API_GetParameter"></a>

Get information about a single parameter by specifying the parameter name.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

**Note**
To get information about more than one parameter at a time, use the [GetParameters](API_GetParameters.md) operation.

**Note**
Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to `GetParameter`, `GetParameters`, and `PutParameter` API calls for your AWS account and AWS Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.
For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience `ThrottlingException: Rate exceeded` errors, enable higher throughput. For more information, see [Changing Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html).

## Request Syntax
<a name="API_GetParameter_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "WithDecryption": {{boolean}}
}
```

## Request Parameters
<a name="API_GetParameter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetParameter_RequestSyntax) **   <a name="systemsmanager-GetParameter-request-Name"></a>
The name or Amazon Resource Name (ARN) of the parameter that you want to query. For parameters shared with you from another account, you must use the full ARN.
To query by parameter label, use `"Name": "name:label"`. To query by parameter version, use `"Name": "name:version"`.
For more information about shared parameters, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [WithDecryption](#API_GetParameter_RequestSyntax) **   <a name="systemsmanager-GetParameter-request-WithDecryption"></a>
Return decrypted values for secure string parameters. This flag is ignored for `String` and `StringList` parameter types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetParameter_ResponseSyntax"></a>

```
{
   "Parameter": {
      "ARN": "string",
      "DataType": "string",
      "LastModifiedDate": number,
      "Name": "string",
      "Selector": "string",
      "SourceResult": "string",
      "Type": "string",
      "Value": "string",
      "Version": number
   }
}
```

## Response Elements
<a name="API_GetParameter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Parameter](#API_GetParameter_ResponseSyntax) **   <a name="systemsmanager-GetParameter-response-Parameter"></a>
Information about a parameter.
Type: [Parameter](API_Parameter.md) object

## Errors
<a name="API_GetParameter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidKeyId **
The query key ID isn't valid.
HTTP Status Code: 400

 ** ParameterNotFound **
The parameter couldn't be found. Verify the name and try again.
For the `DeleteParameter` and `GetParameter` actions, if the specified parameter doesn't exist, the `ParameterNotFound` exception is *not* recorded in AWS CloudTrail event logs.
HTTP Status Code: 400

 ** ParameterVersionNotFound **
The specified parameter version wasn't found. Verify the parameter name and version, and try again.
HTTP Status Code: 400

## Examples
<a name="API_GetParameter_Examples"></a>

### Example
<a name="API_GetParameter_Example_1"></a>

This example illustrates one usage of GetParameter.

#### Sample Request
<a name="API_GetParameter_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 29
X-Amz-Target: AmazonSSM.GetParameter
X-Amz-Date: 20240316T005724Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Name": "MyGitHubPassword"
}
```

#### Sample Response
<a name="API_GetParameter_Example_1_Response"></a>

```
{
    "Parameter": {
        "ARN": "arn:aws:ssm:us-east-2:111122223333:parameter/MyGitHubPassword",
        "DataType": "text",
        "LastModifiedDate": 1582657288.8,
        "Name": "MyGitHubPassword",
        "Type": "SecureString",
        "Value": "AYA39c3b3042cd2aEXAMPLE/AKIAIOSFODNN7EXAMPLE/fh983hg9awEXAMPLE==",
        "Version": 3
    }
}
```

## See Also
<a name="API_GetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetParameter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetParameter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetParameter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetParameter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetParameter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetParameter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetParameter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
