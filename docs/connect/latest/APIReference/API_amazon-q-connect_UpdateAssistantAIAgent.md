---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_UpdateAssistantAIAgent.html
---

# UpdateAssistantAIAgent
<a name="API_amazon-q-connect_UpdateAssistantAIAgent"></a>

Updates the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.

## Request Syntax
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/aiagentConfiguration HTTP/1.1
Content-type: application/json

{
   "aiAgentType": "{{string}}",
   "configuration": {
      "aiAgentId": "{{string}}"
   },
   "orchestratorUseCase": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_UpdateAssistantAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAssistantAIAgent-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aiAgentType](#API_amazon-q-connect_UpdateAssistantAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAssistantAIAgent-request-aiAgentType"></a>
The type of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.
Type: String
Valid Values: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: Yes

 ** [configuration](#API_amazon-q-connect_UpdateAssistantAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAssistantAIAgent-request-configuration"></a>
The configuration of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.
Type: [AIAgentConfigurationData](API_amazon-q-connect_AIAgentConfigurationData.md) object
Required: Yes

 ** [orchestratorUseCase](#API_amazon-q-connect_UpdateAssistantAIAgent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAssistantAIAgent-request-orchestratorUseCase"></a>
The orchestrator use case for the AI Agent being added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assistant": {
      "aiAgentConfiguration": {
         "string" : {
            "aiAgentId": "string"
         }
      },
      "assistantArn": "string",
      "assistantId": "string",
      "capabilityConfiguration": {
         "type": "string"
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
      "serverSideEncryptionConfiguration": {
         "kmsKeyId": "string"
      },
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistant](#API_amazon-q-connect_UpdateAssistantAIAgent_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateAssistantAIAgent-response-assistant"></a>
The assistant data.
Type: [AssistantData](API_amazon-q-connect_AssistantData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_UpdateAssistantAIAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateAssistantAIAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateAssistantAIAgent)
