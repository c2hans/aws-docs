---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateAIAgent.html
---

# CreateAIAgent
<a name="API_amazon-q-connect_CreateAIAgent"></a>

Creates an Amazon Q in Connect AI Agent.

## Request Syntax
<a name="API_amazon-q-connect_CreateAIAgent_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/aiagents HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}",
   "visibilityStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateAIAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateAIAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [configuration](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-configuration"></a>
The configuration of the AI Agent.
Type: [AIAgentConfiguration](API_amazon-q-connect_AIAgentConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [description](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-description"></a>
The description of the AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [name](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-name"></a>
The name of the AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [tags](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [type](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-type"></a>
The type of the AI Agent.
Type: String
Valid Values: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: Yes

 ** [visibilityStatus](#API_amazon-q-connect_CreateAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-request-visibilityStatus"></a>
The visibility status of the AI Agent.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_CreateAIAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aiAgent": {
      "aiAgentArn": "string",
      "aiAgentId": "string",
      "assistantArn": "string",
      "assistantId": "string",
      "configuration": { ... },
      "description": "string",
      "modifiedTime": number,
      "name": "string",
      "origin": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string",
      "visibilityStatus": "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateAIAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aiAgent](#API_amazon-q-connect_CreateAIAgent_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateAIAgent-response-aiAgent"></a>
The data of the created AI Agent.
Type: [AIAgentData](API_amazon-q-connect_AIAgentData.md) object

## Errors
<a name="API_amazon-q-connect_CreateAIAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

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

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateAIAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateAIAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateAIAgent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
