---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAccountSetting.html
---

# GetAccountSetting
<a name="API_GetAccountSetting"></a>

Retrieves the account setting value for the specified setting name.

## Request Syntax
<a name="API_GetAccountSetting_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAccountSetting_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetAccountSetting_RequestSyntax) **   <a name="ECR-GetAccountSetting-request-name"></a>
The name of the account setting, such as `BASIC_SCAN_TYPE_VERSION`, `REGISTRY_POLICY_SCOPE`, or `BLOB_MOUNTING`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_GetAccountSetting_ResponseSyntax"></a>

```
{
   "name": "string",
   "value": "string"
}
```

## Response Elements
<a name="API_GetAccountSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [name](#API_GetAccountSetting_ResponseSyntax) **   <a name="ECR-GetAccountSetting-response-name"></a>
Retrieves the name of the account setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [value](#API_GetAccountSetting_ResponseSyntax) **   <a name="ECR-GetAccountSetting-response-value"></a>
The setting value for the setting name. Valid value for basic scan type: `AWS_NATIVE`. Valid values for registry policy scope: `V2`. Valid values for blob mounting: `ENABLED` or `DISABLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_GetAccountSetting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_GetAccountSetting_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetAccountSetting_Example_1"></a>

This example calls the `BASIC_SCAN_TYPE_VERSION` being used in the registry.

#### Sample Request
<a name="API_GetAccountSetting_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.GetAccountSetting
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.11.144 Python/3.6.1 Darwin/16.6.0 botocore/1.7.2
X-Amz-Date: 20170901T223937Z
Authorization: AUTHPARAMS
Content-Length: 48

{
   aws ecr get-account-setting --name BASIC_SCAN_TYPE_VERSION,
}
```

#### Sample Response
<a name="API_GetAccountSetting_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 01 Sep 2017 19:42:18 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 340
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "name": "BASIC_SCAN_TYPE_VERSION",
    "value": "AWS_NATIVE"
}
```

## See Also
<a name="API_GetAccountSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetAccountSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/GetAccountSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
