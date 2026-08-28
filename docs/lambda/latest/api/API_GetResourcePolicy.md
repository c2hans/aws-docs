---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetResourcePolicy.html
---

# GetResourcePolicy
<a name="API_GetResourcePolicy"></a>

Retrieves the [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) attached to a Lambda resource.

## Request Syntax
<a name="API_GetResourcePolicy_RequestSyntax"></a>

```
GET /2026-07-09/resource-policy/{{ResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_GetResourcePolicy_RequestSyntax) **   <a name="lambda-GetResourcePolicy-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the Lambda resource you want to retrieve the policy for. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_])+)?`
Required: Yes

## Request Body
<a name="API_GetResourcePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetResourcePolicy_ResponseSyntax) **   <a name="lambda-GetResourcePolicy-response-Policy"></a>
The resource-based policy attached to the Lambda resource you specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `[\s\S]+`

 ** [RevisionId](#API_GetResourcePolicy_ResponseSyntax) **   <a name="lambda-GetResourcePolicy-response-RevisionId"></a>
The revision ID of the policy. Pass this value as the `RevisionId` in a [PutResourcePolicy](API_PutResourcePolicy.md) or [DeleteResourcePolicy](API_DeleteResourcePolicy.md) request. Doing so ensures the operation acts on the expected version of the policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

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
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
