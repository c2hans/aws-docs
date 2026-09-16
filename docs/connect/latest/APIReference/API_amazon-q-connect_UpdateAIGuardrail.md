---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_UpdateAIGuardrail.html
---

# UpdateAIGuardrail
<a name="API_amazon-q-connect_UpdateAIGuardrail"></a>

Updates an AI Guardrail.

## Request Syntax
<a name="API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/aiguardrails/{{aiGuardrailId}} HTTP/1.1
Content-type: application/json

{
   "blockedInputMessaging": "{{string}}",
   "blockedOutputsMessaging": "{{string}}",
   "clientToken": "{{string}}",
   "contentPolicyConfig": {
      "filtersConfig": [
         {
            "inputStrength": "{{string}}",
            "outputStrength": "{{string}}",
            "type": "{{string}}"
         }
      ]
   },
   "contextualGroundingPolicyConfig": {
      "filtersConfig": [
         {
            "threshold": {{number}},
            "type": "{{string}}"
         }
      ]
   },
   "description": "{{string}}",
   "sensitiveInformationPolicyConfig": {
      "piiEntitiesConfig": [
         {
            "action": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "regexesConfig": [
         {
            "action": "{{string}}",
            "description": "{{string}}",
            "name": "{{string}}",
            "pattern": "{{string}}"
         }
      ]
   },
   "topicPolicyConfig": {
      "topicsConfig": [
         {
            "definition": "{{string}}",
            "examples": [ "{{string}}" ],
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ]
   },
   "visibilityStatus": "{{string}}",
   "wordPolicyConfig": {
      "managedWordListsConfig": [
         {
            "type": "{{string}}"
         }
      ],
      "wordsConfig": [
         {
            "text": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateAIGuardrail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aiGuardrailId](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-uri-aiGuardrailId"></a>
The identifier of the Amazon Q in Connect AI Guardrail.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** [assistantId](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateAIGuardrail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blockedInputMessaging](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-blockedInputMessaging"></a>
The message to return when the AI Guardrail blocks a prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [blockedOutputsMessaging](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-blockedOutputsMessaging"></a>
The message to return when the AI Guardrail blocks a model response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [clientToken](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [contentPolicyConfig](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-contentPolicyConfig"></a>
The content filter policies to configure for the AI Guardrail.
Type: [AIGuardrailContentPolicyConfig](API_amazon-q-connect_AIGuardrailContentPolicyConfig.md) object
Required: No

 ** [contextualGroundingPolicyConfig](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-contextualGroundingPolicyConfig"></a>
The contextual grounding policy configuration used to create an AI Guardrail.
Type: [AIGuardrailContextualGroundingPolicyConfig](API_amazon-q-connect_AIGuardrailContextualGroundingPolicyConfig.md) object
Required: No

 ** [description](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-description"></a>
A description of the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [sensitiveInformationPolicyConfig](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-sensitiveInformationPolicyConfig"></a>
The sensitive information policy to configure for the AI Guardrail.
Type: [AIGuardrailSensitiveInformationPolicyConfig](API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig.md) object
Required: No

 ** [topicPolicyConfig](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-topicPolicyConfig"></a>
The topic policies to configure for the AI Guardrail.
Type: [AIGuardrailTopicPolicyConfig](API_amazon-q-connect_AIGuardrailTopicPolicyConfig.md) object
Required: No

 ** [visibilityStatus](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-visibilityStatus"></a>
The visibility status of the Amazon Q in Connect AI Guardrail.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

 ** [wordPolicyConfig](#API_amazon-q-connect_UpdateAIGuardrail_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-request-wordPolicyConfig"></a>
The word policy you configure for the AI Guardrail.
Type: [AIGuardrailWordPolicyConfig](API_amazon-q-connect_AIGuardrailWordPolicyConfig.md) object
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateAIGuardrail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aiGuardrail": {
      "aiGuardrailArn": "string",
      "aiGuardrailId": "string",
      "assistantArn": "string",
      "assistantId": "string",
      "blockedInputMessaging": "string",
      "blockedOutputsMessaging": "string",
      "contentPolicyConfig": {
         "filtersConfig": [
            {
               "inputStrength": "string",
               "outputStrength": "string",
               "type": "string"
            }
         ]
      },
      "contextualGroundingPolicyConfig": {
         "filtersConfig": [
            {
               "threshold": number,
               "type": "string"
            }
         ]
      },
      "description": "string",
      "modifiedTime": number,
      "name": "string",
      "sensitiveInformationPolicyConfig": {
         "piiEntitiesConfig": [
            {
               "action": "string",
               "type": "string"
            }
         ],
         "regexesConfig": [
            {
               "action": "string",
               "description": "string",
               "name": "string",
               "pattern": "string"
            }
         ]
      },
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "topicPolicyConfig": {
         "topicsConfig": [
            {
               "definition": "string",
               "examples": [ "string" ],
               "name": "string",
               "type": "string"
            }
         ]
      },
      "visibilityStatus": "string",
      "wordPolicyConfig": {
         "managedWordListsConfig": [
            {
               "type": "string"
            }
         ],
         "wordsConfig": [
            {
               "text": "string"
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_UpdateAIGuardrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aiGuardrail](#API_amazon-q-connect_UpdateAIGuardrail_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateAIGuardrail-response-aiGuardrail"></a>
The data of the updated Amazon Q in Connect AI Guardrail.
Type: [AIGuardrailData](API_amazon-q-connect_AIGuardrailData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateAIGuardrail_Errors"></a>

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
<a name="API_amazon-q-connect_UpdateAIGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateAIGuardrail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateAIGuardrail)
