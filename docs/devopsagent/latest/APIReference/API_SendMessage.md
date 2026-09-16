---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessage.html
---

# SendMessage
<a name="API_SendMessage"></a>

Sends a chat message and streams the response for the specified agent space execution

## Request Syntax
<a name="API_SendMessage_RequestSyntax"></a>

```
POST /agents/agent-space/{{agentSpaceId}}/chat/sendMessage HTTP/1.1
Content-type: application/json

{
   "assetIds": [ "{{string}}" ],
   "content": "{{string}}",
   "context": {
      "approvalAction": {
         "action": "{{string}}",
         "approvalId": "{{string}}",
         "buttonText": "{{string}}",
         "interruptId": "{{string}}",
         "toolUseId": "{{string}}"
      },
      "currentPage": "{{string}}",
      "lastMessage": "{{string}}",
      "userActionResponse": "{{string}}"
   },
   "executionId": "{{string}}",
   "modelTier": "{{string}}",
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-uri-agentSpaceId"></a>
The agent space identifier
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_SendMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetIds](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-assetIds"></a>
Optional list of asset identifiers to attach to the message
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [content](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-content"></a>
The user message content
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: Yes

 ** [context](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-context"></a>
Optional context for the message
Type: [SendMessageContext](API_SendMessageContext.md) object
Required: No

 ** [executionId](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-executionId"></a>
The execution identifier for the chat session
Type: String
Length Constraints: Minimum length of 32. Maximum length of 50.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [modelTier](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-modelTier"></a>
Optional model tier selection. Valid values: smart, balanced, fast. Absent or unrecognized values default to balanced.
Type: String
Required: No

 ** [userId](#API_SendMessage_RequestSyntax) **   <a name="devopsagent-SendMessage-request-userId"></a>
User identifier. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_SendMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contentBlockDelta": {
      "delta": { ... },
      "index": number,
      "sequenceNumber": number
   },
   "contentBlockStart": {
      "id": "string",
      "index": number,
      "parentId": "string",
      "sequenceNumber": number,
      "type": "string"
   },
   "contentBlockStop": {
      "index": number,
      "last": boolean,
      "sequenceNumber": number,
      "text": "string",
      "type": "string"
   },
   "heartbeat": {
   },
   "responseCompleted": {
      "responseId": "string",
      "sequenceNumber": number,
      "usage": {
         "inputTokens": number,
         "outputTokens": number,
         "totalTokens": number
      }
   },
   "responseCreated": {
      "responseId": "string",
      "sequenceNumber": number
   },
   "responseFailed": {
      "errorCode": "string",
      "errorMessage": "string",
      "responseId": "string",
      "sequenceNumber": number
   },
   "responseInProgress": {
      "responseId": "string",
      "sequenceNumber": number
   },
   "summary": {
      "content": "string",
      "sequenceNumber": number
   }
}
```

## Response Elements
<a name="API_SendMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contentBlockDelta](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-contentBlockDelta"></a>
Emitted for each incremental content delta within a content block
Type: [SendMessageContentBlockDeltaEvent](API_SendMessageContentBlockDeltaEvent.md) object

 ** [contentBlockStart](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-contentBlockStart"></a>
Emitted when a new content block starts
Type: [SendMessageContentBlockStartEvent](API_SendMessageContentBlockStartEvent.md) object

 ** [contentBlockStop](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-contentBlockStop"></a>
Emitted when a content block is complete
Type: [SendMessageContentBlockStopEvent](API_SendMessageContentBlockStopEvent.md) object

 ** [heartbeat](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-heartbeat"></a>
Heartbeat event sent periodically to keep the connection alive during idle periods
Type: [SendMessageHeartbeatEvent](API_SendMessageHeartbeatEvent.md) object

 ** [responseCompleted](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-responseCompleted"></a>
Emitted when the response completes successfully
Type: [SendMessageResponseCompletedEvent](API_SendMessageResponseCompletedEvent.md) object

 ** [responseCreated](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-responseCreated"></a>
Emitted when the response is created
Type: [SendMessageResponseCreatedEvent](API_SendMessageResponseCreatedEvent.md) object

 ** [responseFailed](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-responseFailed"></a>
Emitted when the response fails
Type: [SendMessageResponseFailedEvent](API_SendMessageResponseFailedEvent.md) object

 ** [responseInProgress](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-responseInProgress"></a>
Emitted while the response is being generated
Type: [SendMessageResponseInProgressEvent](API_SendMessageResponseInProgressEvent.md) object

 ** [summary](#API_SendMessage_ResponseSyntax) **   <a name="devopsagent-SendMessage-response-summary"></a>
Emitted to provide a summary of agent actions
Type: [SendMessageSummaryEvent](API_SendMessageSummaryEvent.md) object

## Errors
<a name="API_SendMessage_Errors"></a>

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
<a name="API_SendMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/SendMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessage)
