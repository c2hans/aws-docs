---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UnlabelParameterVersion.html
---

# UnlabelParameterVersion
<a name="API_UnlabelParameterVersion"></a>

Remove a label or labels from a parameter.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

## Request Syntax
<a name="API_UnlabelParameterVersion_RequestSyntax"></a>

```
{
   "Labels": [ "{{string}}" ],
   "Name": "{{string}}",
   "ParameterVersion": {{number}}
}
```

## Request Parameters
<a name="API_UnlabelParameterVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Labels](#API_UnlabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-UnlabelParameterVersion-request-Labels"></a>
One or more labels to delete from the specified parameter version.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_UnlabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-UnlabelParameterVersion-request-Name"></a>
The name of the parameter from which you want to delete one or more labels.
You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ParameterVersion](#API_UnlabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-UnlabelParameterVersion-request-ParameterVersion"></a>
The specific version of the parameter which you want to delete one or more labels from. If it isn't present, the call will fail.
Type: Long
Required: Yes

## Response Syntax
<a name="API_UnlabelParameterVersion_ResponseSyntax"></a>

```
{
   "InvalidLabels": [ "string" ],
   "RemovedLabels": [ "string" ]
}
```

## Response Elements
<a name="API_UnlabelParameterVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvalidLabels](#API_UnlabelParameterVersion_ResponseSyntax) **   <a name="systemsmanager-UnlabelParameterVersion-response-InvalidLabels"></a>
The labels that aren't attached to the given parameter version.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [RemovedLabels](#API_UnlabelParameterVersion_ResponseSyntax) **   <a name="systemsmanager-UnlabelParameterVersion-response-RemovedLabels"></a>
A list of all labels deleted from the parameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_UnlabelParameterVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ParameterNotFound **
The parameter couldn't be found. Verify the name and try again.
For the `DeleteParameter` and `GetParameter` actions, if the specified parameter doesn't exist, the `ParameterNotFound` exception is *not* recorded in AWS CloudTrail event logs.
HTTP Status Code: 400

 ** ParameterVersionNotFound **
The specified parameter version wasn't found. Verify the parameter name and version, and try again.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_UnlabelParameterVersion_Examples"></a>

### Example
<a name="API_UnlabelParameterVersion_Example_1"></a>

This example illustrates one usage of UnlabelParameterVersion.

#### Sample Request
<a name="API_UnlabelParameterVersion_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UnlabelParameterVersion
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240712T183221Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20200325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 67

{
    "Name": "MyParameter",
    "ParameterVersion": 2,
    "Labels": [
        "label"
    ]
}
```

#### Sample Response
<a name="API_UnlabelParameterVersion_Example_1_Response"></a>

```
{
    "InvalidLabels": [],
    "RemovedLabels": [
        "label"
    ]
}
```

## See Also
<a name="API_UnlabelParameterVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UnlabelParameterVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UnlabelParameterVersion)
