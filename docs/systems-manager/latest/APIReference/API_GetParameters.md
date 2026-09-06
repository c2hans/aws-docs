---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html
---

# GetParameters
<a name="API_GetParameters"></a>

Get information about one or more parameters by specifying multiple parameter names.

**Note**
To get information about a single parameter, you can use the [GetParameter](API_GetParameter.md) operation instead.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

**Note**
Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to `GetParameter`, `GetParameters`, and `PutParameter` API calls for your AWS account and AWS Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.
For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience `ThrottlingException: Rate exceeded` errors, enable higher throughput. For more information, see [Changing Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html).

## Request Syntax
<a name="API_GetParameters_RequestSyntax"></a>

```
{
   "Names": [ "{{string}}" ],
   "WithDecryption": {{boolean}}
}
```

## Request Parameters
<a name="API_GetParameters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Names](#API_GetParameters_RequestSyntax) **   <a name="systemsmanager-GetParameters-request-Names"></a>
The names or Amazon Resource Names (ARNs) of the parameters that you want to query. For parameters shared with you from another account, you must use the full ARNs.
To query by parameter label, use `"Name": "name:label"`. To query by parameter version, use `"Name": "name:version"`.
The results for `GetParameters` requests are listed in alphabetical order in query responses.
For information about shared parameters, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [WithDecryption](#API_GetParameters_RequestSyntax) **   <a name="systemsmanager-GetParameters-request-WithDecryption"></a>
Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for `String` and `StringList` parameter types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetParameters_ResponseSyntax"></a>

```
{
   "InvalidParameters": [ "string" ],
   "Parameters": [
      {
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
   ]
}
```

## Response Elements
<a name="API_GetParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvalidParameters](#API_GetParameters_ResponseSyntax) **   <a name="systemsmanager-GetParameters-response-InvalidParameters"></a>
A list of parameters that aren't formatted correctly or don't run during an execution.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Parameters](#API_GetParameters_ResponseSyntax) **   <a name="systemsmanager-GetParameters-response-Parameters"></a>
A list of details for a parameter.
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_GetParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidKeyId **
The query key ID isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_GetParameters_Examples"></a>

### Example
<a name="API_GetParameters_Example_1"></a>

This example illustrates one usage of GetParameters.

#### Sample Request
<a name="API_GetParameters_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 73
X-Amz-Target: AmazonSSM.GetParameters
X-Amz-Date: 20240316T001029Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Names": [
        "EC2DevServerTypo",
        "EC2DevServerType",
        "EC2TestServerType",
        "EC2ProdServerType"
    ]
}
```

#### Sample Response
<a name="API_GetParameters_Example_1_Response"></a>

```
{
    "InvalidParameters": [
        "EC2DevServerTypo"
    ],
    "Parameters": [
        {
            "Name": "EC2DevServerType",
            "Type": "String",
            "Value": "t2.micro",
            "Version": 2
        },
        {
            "Name": "EC2ProdServerType",
            "Type": "String",
            "Value": "m4.large",
            "Version": 1
        },
        {
            "Name": "EC2TestServerType",
            "Type": "String",
            "Value": "t2.large",
            "Version": 3
        }
    ]
}
```

## See Also
<a name="API_GetParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetParameters)
