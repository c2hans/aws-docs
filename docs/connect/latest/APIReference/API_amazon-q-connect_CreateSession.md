---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateSession.html
---

# CreateSession
<a name="API_amazon-q-connect_CreateSession"></a>

Creates a session. A session is a contextual container used for generating recommendations. Connect Customer creates a new Amazon Q in Connect session for each contact on which Amazon Q in Connect is enabled.

## Request Syntax
<a name="API_amazon-q-connect_CreateSession_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/sessions HTTP/1.1
Content-type: application/json

{
   "aiAgentConfiguration": {
      "{{string}}" : {
         "aiAgentId": "{{string}}"
      }
   },
   "clientToken": "{{string}}",
   "contactArn": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "orchestratorConfigurationList": [
      {
         "aiAgentId": "{{string}}",
         "orchestratorUseCase": "{{string}}"
      }
   ],
   "removeOrchestratorConfigurationList": {{boolean}},
   "tagFilter": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aiAgentConfiguration](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-aiAgentConfiguration"></a>
The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.
Type: String to [AIAgentConfigurationData](API_amazon-q-connect_AIAgentConfigurationData.md) object map
Valid Keys: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** [clientToken](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [contactArn](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-contactArn"></a>
The Amazon Resource Name (ARN) of the email contact in Connect Customer. Used to retrieve email content and establish session context for AI-powered email assistance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: No

 ** [description](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [name](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-name"></a>
The name of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [orchestratorConfigurationList](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-orchestratorConfigurationList"></a>
The list of orchestrator configurations for the session being created.
Type: Array of [OrchestratorConfigurationEntry](API_amazon-q-connect_OrchestratorConfigurationEntry.md) objects
Required: No

 ** [removeOrchestratorConfigurationList](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-removeOrchestratorConfigurationList"></a>
The list of orchestrator configurations to remove from the session.
Type: Boolean
Required: No

 ** [tagFilter](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-tagFilter"></a>
An object that can be used to specify Tag conditions.
Type: [TagFilter](API_amazon-q-connect_TagFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_amazon-q-connect_CreateSession_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateSession-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "session": {
      "aiAgentConfiguration": {
         "string" : {
            "aiAgentId": "string"
         }
      },
      "description": "string",
      "integrationConfiguration": {
         "topicIntegrationArn": "string"
      },
      "name": "string",
      "orchestratorConfigurationList": [
         {
            "aiAgentId": "string",
            "orchestratorUseCase": "string"
         }
      ],
      "origin": "string",
      "sessionArn": "string",
      "sessionId": "string",
      "tagFilter": { ... },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [session](#API_amazon-q-connect_CreateSession_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateSession-response-session"></a>
The session.
Type: [SessionData](API_amazon-q-connect_SessionData.md) object

## Errors
<a name="API_amazon-q-connect_CreateSession_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateSession)
