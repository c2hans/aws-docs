---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateChat.html
---

# UpdateChat
<a name="API_UpdateChat"></a>

Updates a chat execution. You can use this operation to change the chat execution's summary or to archive or unarchive it.

Archiving a chat execution hides it from the default chat list. Unarchiving a chat execution restores it to the default chat list.

## Request Syntax
<a name="API_UpdateChat_RequestSyntax"></a>

```
PATCH /agents/agent-space/{{agentSpaceId}}/chat/{{executionId}} HTTP/1.1
Content-type: application/json

{
   "archiveStatus": "{{string}}",
   "clientToken": "{{string}}",
   "summary": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateChat_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_UpdateChat_RequestSyntax) **   <a name="devopsagent-UpdateChat-request-uri-agentSpaceId"></a>
The unique identifier of the agent space that contains the chat execution to update.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [executionId](#API_UpdateChat_RequestSyntax) **   <a name="devopsagent-UpdateChat-request-uri-executionId"></a>
The unique identifier of the chat execution to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_UpdateChat_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [archiveStatus](#API_UpdateChat_RequestSyntax) **   <a name="devopsagent-UpdateChat-request-archiveStatus"></a>
The archive status to set for the chat execution. Use this parameter to archive the chat execution, hiding it from the default chat list, or to unarchive it, restoring it to the default chat list.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** [clientToken](#API_UpdateChat_RequestSyntax) **   <a name="devopsagent-UpdateChat-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [summary](#API_UpdateChat_RequestSyntax) **   <a name="devopsagent-UpdateChat-request-summary"></a>
The new summary to set for the chat execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateChat_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "archiveStatus": "string",
   "executionId": "string",
   "summary": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateChat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [archiveStatus](#API_UpdateChat_ResponseSyntax) **   <a name="devopsagent-UpdateChat-response-archiveStatus"></a>
The archive status of the chat execution after the update.
Type: String
Valid Values: `ACTIVE | ARCHIVED`

 ** [executionId](#API_UpdateChat_ResponseSyntax) **   <a name="devopsagent-UpdateChat-response-executionId"></a>
The unique identifier of the updated chat execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [summary](#API_UpdateChat_ResponseSyntax) **   <a name="devopsagent-UpdateChat-response-summary"></a>
The summary of the chat execution after the update.
Type: String

 ** [updatedAt](#API_UpdateChat_ResponseSyntax) **   <a name="devopsagent-UpdateChat-response-updatedAt"></a>
The date and time at which the chat execution was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateChat_Errors"></a>

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
 ** reason **
A machine-readable reason code that explains why the request conflicted with the current state of the resource. For example, `CHAT_ARCHIVED` indicates that the request acted on a chat that is archived. This field is absent when no specific reason applies.
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
<a name="API_UpdateChat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/UpdateChat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UpdateChat)
