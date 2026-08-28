---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunction.html
---

# DeleteFunction
<a name="API_DeleteFunction"></a>

Deletes a Lambda function. To delete a specific function version, use the `Qualifier` parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for [DeleteAlias](API_DeleteAlias.md).

**Note**
A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting.

To delete Lambda event source mappings that invoke a function, use [DeleteEventSourceMapping](API_DeleteEventSourceMapping.md). For AWS services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.

## Request Syntax
<a name="API_DeleteFunction_RequestSyntax"></a>

```
DELETE /2015-03-31/functions/{{FunctionName}}?Qualifier={{Qualifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_DeleteFunction_RequestSyntax) **   <a name="lambda-DeleteFunction-request-uri-FunctionName"></a>
The name or ARN of the Lambda function or version.

**Name formats**
+  **Function name** – `my-function` (name-only), `my-function:1` (with version).
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_DeleteFunction_RequestSyntax) **   <a name="lambda-DeleteFunction-request-uri-Qualifier"></a>
Specify a version to delete. You can't delete a version that an alias references.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

## Request Body
<a name="API_DeleteFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFunction_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
```

## Response Elements
<a name="API_DeleteFunction_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_DeleteFunction_ResponseSyntax) **   <a name="lambda-DeleteFunction-response-StatusCode"></a>
The HTTP status code returned by the operation.

## Errors
<a name="API_DeleteFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

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
<a name="API_DeleteFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/DeleteFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DeleteFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
