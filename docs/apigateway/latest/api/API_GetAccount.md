---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetAccount.html
---

# GetAccount
<a name="API_GetAccount"></a>

Gets information about the current Account resource.

## Request Syntax
<a name="API_GetAccount_RequestSyntax"></a>

```
GET /account HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKeyVersion": "string",
   "cloudwatchRoleArn": "string",
   "features": [ "string" ],
   "throttleSettings": {
      "burstLimit": number,
      "rateLimit": number
   }
}
```

## Response Elements
<a name="API_GetAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeyVersion](#API_GetAccount_ResponseSyntax) **   <a name="apigw-GetAccount-response-apiKeyVersion"></a>
The version of the API keys used for the account.
Type: String

 ** [cloudwatchRoleArn](#API_GetAccount_ResponseSyntax) **   <a name="apigw-GetAccount-response-cloudwatchRoleArn"></a>
The ARN of an Amazon CloudWatch role for the current Account.
Type: String

 ** [features](#API_GetAccount_ResponseSyntax) **   <a name="apigw-GetAccount-response-features"></a>
A list of features supported for the account. When usage plans are enabled, the features list will include an entry of `"UsagePlans"`.
Type: Array of strings

 ** [throttleSettings](#API_GetAccount_ResponseSyntax) **   <a name="apigw-GetAccount-response-throttleSettings"></a>
Specifies the API request limits configured for the current Account.
Type: [ThrottleSettings](API_ThrottleSettings.md) object

## Errors
<a name="API_GetAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## See Also
<a name="API_GetAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
