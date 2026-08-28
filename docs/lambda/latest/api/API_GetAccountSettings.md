---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetAccountSettings.html
---

# GetAccountSettings
<a name="API_GetAccountSettings"></a>

Retrieves details about your account's [limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) and usage in an AWS Region.

## Request Syntax
<a name="API_GetAccountSettings_RequestSyntax"></a>

```
GET /2016-08-19/account-settings HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountLimit": {
      "CodeSizeUnzipped": number,
      "CodeSizeZipped": number,
      "ConcurrentExecutions": number,
      "TotalCodeSize": number,
      "UnreservedConcurrentExecutions": number
   },
   "AccountUsage": {
      "FunctionCount": number,
      "TotalCodeSize": number
   }
}
```

## Response Elements
<a name="API_GetAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLimit](#API_GetAccountSettings_ResponseSyntax) **   <a name="lambda-GetAccountSettings-response-AccountLimit"></a>
Limits that are related to concurrency and code storage.
Type: [AccountLimit](API_AccountLimit.md) object

 ** [AccountUsage](#API_GetAccountSettings_ResponseSyntax) **   <a name="lambda-GetAccountSettings-response-AccountUsage"></a>
The number of functions and amount of storage in use.
Type: [AccountUsage](API_AccountUsage.md) object

## Errors
<a name="API_GetAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_GetAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
