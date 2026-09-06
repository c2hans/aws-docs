---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateAIPrompt.html
---

# CreateAIPrompt
<a name="API_amazon-q-connect_CreateAIPrompt"></a>

Creates an Amazon Q in Connect AI Prompt.

## Request Syntax
<a name="API_amazon-q-connect_CreateAIPrompt_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/aiprompts HTTP/1.1
Content-type: application/json

{
   "apiFormat": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "inferenceConfiguration": {
      "maxTokensToSample": {{number}},
      "temperature": {{number}},
      "topK": {{number}},
      "topP": {{number}}
   },
   "modelId": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "templateConfiguration": { ... },
   "templateType": "{{string}}",
   "type": "{{string}}",
   "visibilityStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateAIPrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateAIPrompt_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiFormat](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-apiFormat"></a>
The API Format of the AI Prompt.
Recommended values: `MESSAGES | TEXT_COMPLETIONS`
The values `ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS` will be deprecated.
Type: String
Valid Values: `ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS | MESSAGES | TEXT_COMPLETIONS`
Required: Yes

 ** [clientToken](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [description](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-description"></a>
The description of the AI Prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [inferenceConfiguration](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-inferenceConfiguration"></a>
The inference configuration for the AI Prompt being created.
Type: [AIPromptInferenceConfiguration](API_amazon-q-connect_AIPromptInferenceConfiguration.md) object
Required: No

 ** [modelId](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-modelId"></a>
The identifier of the model used for this AI Prompt.
For information about which models are supported in each AWS Region, see [Supported models for system/custom prompts](https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [name](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-name"></a>
The name of the AI Prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [tags](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [templateConfiguration](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-templateConfiguration"></a>
The configuration of the prompt template for this AI Prompt.
Type: [AIPromptTemplateConfiguration](API_amazon-q-connect_AIPromptTemplateConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [templateType](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-templateType"></a>
The type of the prompt template for this AI Prompt.
Type: String
Valid Values: `TEXT`
Required: Yes

 ** [type](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-type"></a>
The type of this AI Prompt.
Type: String
Valid Values: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: Yes

 ** [visibilityStatus](#API_amazon-q-connect_CreateAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-request-visibilityStatus"></a>
The visibility status of the AI Prompt.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_CreateAIPrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aiPrompt": {
      "aiPromptArn": "string",
      "aiPromptId": "string",
      "apiFormat": "string",
      "assistantArn": "string",
      "assistantId": "string",
      "description": "string",
      "inferenceConfiguration": {
         "maxTokensToSample": number,
         "temperature": number,
         "topK": number,
         "topP": number
      },
      "modelId": "string",
      "modifiedTime": number,
      "name": "string",
      "origin": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "templateConfiguration": { ... },
      "templateType": "string",
      "type": "string",
      "visibilityStatus": "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateAIPrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aiPrompt](#API_amazon-q-connect_CreateAIPrompt_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateAIPrompt-response-aiPrompt"></a>
The data of the AI Prompt.
Type: [AIPromptData](API_amazon-q-connect_AIPromptData.md) object

## Errors
<a name="API_amazon-q-connect_CreateAIPrompt_Errors"></a>

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
<a name="API_amazon-q-connect_CreateAIPrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateAIPrompt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateAIPrompt)
