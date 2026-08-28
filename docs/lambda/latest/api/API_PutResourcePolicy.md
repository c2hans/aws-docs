---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Adds a [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) to a Lambda resource. Resource-based policies grant access to other [AWS accounts](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-cross-account.html), [organizations](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-organization.html), or [services](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-services.html). Resource-based policies apply to a single Lambda resource (for example, a function, function version, or function alias).

**Important**
This operation replaces any existing policy on the Lambda resource. If you previously added permissions using the [AddPermission](API_AddPermission.md) operation, the new policy overwrites those permissions.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /2026-07-09/resource-policy/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}",
   "RevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambda-PutResourcePolicy-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the Lambda resource you want to add the policy to. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_])+)?`
Required: Yes

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambda-PutResourcePolicy-request-Policy"></a>
The policy document you want to add to your Lambda resource. This is formatted as a JSON string.
For more information, see [Working with resource-based policies in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the * AWS Lambda Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `[\s\S]+`
Required: Yes

 ** [RevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambda-PutResourcePolicy-request-RevisionId"></a>
The revision ID that the existing policy must match for the replacement to proceed. If the revision ID doesn't match, the operation fails with a `PreconditionFailedException` error. To retrieve the current revision ID, use the [GetResourcePolicy](API_GetResourcePolicy.md) operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="lambda-PutResourcePolicy-response-Policy"></a>
The resource-based policy that Lambda adds to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `[\s\S]+`

 ** [RevisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="lambda-PutResourcePolicy-response-RevisionId"></a>
The revision ID of the policy that Lambda adds to your Lambda resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** PolicyLengthExceededException **
The permissions policy for the resource is too large. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
HTTP Status Code: 400

 ** PreconditionFailedException **
The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
+  **For AddPermission and RemovePermission API operations:** Call `GetPolicy` to retrieve the latest RevisionId for your resource.
+  **For all other API operations:** Call `GetFunction` or `GetAlias` to retrieve the latest RevisionId for your resource.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 412

 ** PublicPolicyException **
The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.
 ** Message **
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
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
