---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Removes the association of a resource-based policy from an app monitor.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
DELETE /appmonitor/{{Name}}/policy?policyRevisionId={{PolicyRevisionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="cloudwatchrum-DeleteResourcePolicy-request-uri-Name"></a>
The app monitor that you want to remove the resource policy from.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

 ** [PolicyRevisionId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="cloudwatchrum-DeleteResourcePolicy-request-uri-PolicyRevisionId"></a>
Specifies a specific policy revision to delete. Provide a `PolicyRevisionId` to ensure an atomic delete operation. If the revision ID that you provide doesn't match the latest policy revision ID, the request will be rejected with an `InvalidPolicyRevisionIdException` error.
Length Constraints: Minimum length of 1. Maximum length of 255.

## Request Body
<a name="API_DeleteResourcePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyRevisionId": "string"
}
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyRevisionId](#API_DeleteResourcePolicy_ResponseSyntax) **   <a name="cloudwatchrum-DeleteResourcePolicy-response-PolicyRevisionId"></a>
The revision ID of the policy that was removed, if it had one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** InvalidPolicyRevisionIdException **
The policy revision ID that you provided doeesn't match the latest policy revision ID.
HTTP Status Code: 400

 ** PolicyNotFoundException **
The resource-based policy doesn't exist on this app monitor.
HTTP Status Code: 404

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/DeleteResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
