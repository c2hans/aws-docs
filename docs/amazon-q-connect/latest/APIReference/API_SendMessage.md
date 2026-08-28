---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SendMessage.html
---

# SendMessage
<a name="API_amazon-q-connect_SendMessage"></a>

Submits a message to the Amazon Q in Connect session.

## Request Syntax
<a name="API_amazon-q-connect_SendMessage_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/sessions/{{sessionId}}/message HTTP/1.1
Content-type: application/json

{
   "aiAgentId": "{{string}}",
   "clientToken": "{{string}}",
   "configuration": {
      "generateChunkedMessage": {{boolean}},
      "generateFillerMessage": {{boolean}}
   },
   "conversationContext": {
      "selfServiceConversationHistory": [
         {
            "botResponse": "{{string}}",
            "inputTranscript": "{{string}}",
            "timestamp": {{number}},
            "turnNumber": {{number}}
         }
      ]
   },
   "message": {
      "value": { ... }
   },
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "orchestratorUseCase": "{{string}}",
   "originRequestId": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_SendMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [sessionId](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-uri-sessionId"></a>
The identifier of the Amazon Q in Connect session.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_SendMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aiAgentId](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-aiAgentId"></a>
The identifier of the AI Agent to use for processing the message.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** [clientToken](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field.For more information about idempotency, see Making retries safe with idempotent APIs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [configuration](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-configuration"></a>
The configuration of the [SendMessage](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html) request.
Type: [MessageConfiguration](API_amazon-q-connect_MessageConfiguration.md) object
Required: No

 ** [conversationContext](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-conversationContext"></a>
The conversation context before the Amazon Q in Connect session.
Type: [ConversationContext](API_amazon-q-connect_ConversationContext.md) object
Required: No

 ** [message](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-message"></a>
The message data to submit to the Amazon Q in Connect session.
Type: [MessageInput](API_amazon-q-connect_MessageInput.md) object
Required: Yes

 ** [metadata](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-metadata"></a>
Additional metadata for the message.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [orchestratorUseCase](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-orchestratorUseCase"></a>
The orchestrator use case for message processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [originRequestId](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-originRequestId"></a>
Request identifier from the origin system, used for end-to-end tracing across spans.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [type](#API_amazon-q-connect_SendMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_SendMessage-request-type"></a>
The message type.
Type: String
Valid Values: `TEXT | TOOL_USE_RESULT`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_SendMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "generateChunkedMessage": boolean,
      "generateFillerMessage": boolean
   },
   "nextMessageToken": "string",
   "requestMessageId": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_SendMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_amazon-q-connect_SendMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_SendMessage-response-configuration"></a>
The configuration of the [SendMessage](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html) request.
Type: [MessageConfiguration](API_amazon-q-connect_MessageConfiguration.md) object

 ** [nextMessageToken](#API_amazon-q-connect_SendMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_SendMessage-response-nextMessageToken"></a>
The token for the next message, used by GetNextMessage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [requestMessageId](#API_amazon-q-connect_SendMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_SendMessage-response-requestMessageId"></a>
The identifier of the submitted message.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_amazon-q-connect_SendMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** DependencyFailedException **
The request failed because it depends on another request that failed.
HTTP Status Code: 424

 ** RequestTimeoutException **
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_SendMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/SendMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SendMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
