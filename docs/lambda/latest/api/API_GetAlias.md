---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetAlias.html
---

# GetAlias
<a name="API_GetAlias"></a>

Returns details about a Lambda function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).

## Request Syntax
<a name="API_GetAlias_RequestSyntax"></a>

```
GET /2015-03-31/functions/{{FunctionName}}/aliases/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_GetAlias_RequestSyntax) **   <a name="lambda-GetAlias-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** - `MyFunction`.
+  **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+  **Partial ARN** - `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Name](#API_GetAlias_RequestSyntax) **   <a name="lambda-GetAlias-request-uri-Name"></a>
The name of the alias.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`
Required: Yes

## Request Body
<a name="API_GetAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AliasArn": "string",
   "Description": "string",
   "FunctionVersion": "string",
   "Name": "string",
   "RevisionId": "string",
   "RoutingConfig": {
      "AdditionalVersionWeights": {
         "string" : number
      }
   }
}
```

## Response Elements
<a name="API_GetAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AliasArn](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-AliasArn"></a>
The Amazon Resource Name (ARN) of the alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [Description](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-Description"></a>
A description of the alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [FunctionVersion](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-FunctionVersion"></a>
The function version that the alias invokes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [Name](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-Name"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

 ** [RevisionId](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-RevisionId"></a>
A unique identifier that changes when you update the alias.
Type: String

 ** [RoutingConfig](#API_GetAlias_ResponseSyntax) **   <a name="lambda-GetAlias-response-RoutingConfig"></a>
The [routing configuration](https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html) of the alias.
Type: [AliasRoutingConfiguration](API_AliasRoutingConfiguration.md) object

## Errors
<a name="API_GetAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_GetAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
