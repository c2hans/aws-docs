---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListPendingMessages.html
---

# ListPendingMessages
<a name="API_ListPendingMessages"></a>

List pending messages for a specific execution.

## Request Syntax
<a name="API_ListPendingMessages_RequestSyntax"></a>

```
POST /agents/agent-space/{{agentSpaceId}}/pendingMessages HTTP/1.1
Content-type: application/json

{
   "executionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPendingMessages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_ListPendingMessages_RequestSyntax) **   <a name="devopsagent-ListPendingMessages-request-uri-agentSpaceId"></a>
Unique identifier for an agent space (allows alphanumeric characters and hyphens; 1-64 characters)
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

## Request Body
<a name="API_ListPendingMessages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [executionId](#API_ListPendingMessages_RequestSyntax) **   <a name="devopsagent-ListPendingMessages-request-executionId"></a>
The unique identifier of the execution whose journal records to retrieve
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_ListPendingMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "createdAt": number,
   "executionId": "string",
   "messages": [
      {
         "message": { ... },
         "messageId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPendingMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_ListPendingMessages_ResponseSyntax) **   <a name="devopsagent-ListPendingMessages-response-agentSpaceId"></a>
Unique identifier for an agent space (allows alphanumeric characters and hyphens; 1-64 characters)
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`

 ** [createdAt](#API_ListPendingMessages_ResponseSyntax) **   <a name="devopsagent-ListPendingMessages-response-createdAt"></a>
Timestamp when the pending messages were created.
Type: Timestamp

 ** [executionId](#API_ListPendingMessages_ResponseSyntax) **   <a name="devopsagent-ListPendingMessages-response-executionId"></a>
The unique identifier for the execution.
Type: String

 ** [messages](#API_ListPendingMessages_ResponseSyntax) **   <a name="devopsagent-ListPendingMessages-response-messages"></a>
The list of pending messages for the execution.
Type: Array of [PendingMessage](API_PendingMessage.md) objects

## Errors
<a name="API_ListPendingMessages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListPendingMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListPendingMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListPendingMessages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
