---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListModels.html
---

# ListModels
<a name="API_amazon-q-connect_ListModels"></a>

Lists the models available to an Amazon Q in Connect assistant in the assistant's AWS Region. The available models are determined by the region of the specified assistant.

## Request Syntax
<a name="API_amazon-q-connect_ListModels_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/models?aiPromptType={{aiPromptType}}&maxResults={{maxResults}}&modelLifecycle={{modelLifecycle}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListModels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aiPromptType](#API_amazon-q-connect_ListModels_RequestSyntax) **   <a name="connect-amazon-q-connect_ListModels-request-uri-aiPromptType"></a>
The type of the AI Prompt to filter models by. When specified, only models that support the given AI Prompt type are returned.
Valid Values: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`

 ** [assistantId](#API_amazon-q-connect_ListModels_RequestSyntax) **   <a name="connect-amazon-q-connect_ListModels-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. The assistant's region determines which models are available.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_ListModels_RequestSyntax) **   <a name="connect-amazon-q-connect_ListModels-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [modelLifecycle](#API_amazon-q-connect_ListModels_RequestSyntax) **   <a name="connect-amazon-q-connect_ListModels-request-uri-modelLifecycle"></a>
The lifecycle status of models to filter by. When specified, only models with the given lifecycle status are returned.
Valid Values: `ACTIVE | LEGACY`

 ** [nextToken](#API_amazon-q-connect_ListModels_RequestSyntax) **   <a name="connect-amazon-q-connect_ListModels-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_amazon-q-connect_ListModels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelSummaries": [
      {
         "crossRegionStatus": "string",
         "displayName": "string",
         "endOfLifeTimestamp": number,
         "legacyTimestamp": number,
         "modelId": "string",
         "modelLifecycle": "string",
         "supportedAIPromptTypes": [ "string" ],
         "supportsPromptCaching": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelSummaries](#API_amazon-q-connect_ListModels_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListModels-response-modelSummaries"></a>
The summaries of the models available to the assistant.
Type: Array of [ModelSummary](API_amazon-q-connect_ModelSummary.md) objects

 ** [nextToken](#API_amazon-q-connect_ListModels_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListModels-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_amazon-q-connect_ListModels_Errors"></a>

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
<a name="API_amazon-q-connect_ListModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListModels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListModels)
