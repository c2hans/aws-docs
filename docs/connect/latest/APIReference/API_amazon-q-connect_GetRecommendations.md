---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GetRecommendations.html
---

# GetRecommendations
<a name="API_amazon-q-connect_GetRecommendations"></a>

**Important**
This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.

Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use [NotifyRecommendationsReceived](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NotifyRecommendationsReceived.html). This API supports long-polling behavior with the `waitTimeSeconds` parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use [QueryAssistant](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryAssistant.html).

## Request Syntax
<a name="API_amazon-q-connect_GetRecommendations_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/sessions/{{sessionId}}/recommendations?maxResults={{maxResults}}&nextChunkToken={{nextChunkToken}}&recommendationType={{recommendationType}}&waitTimeSeconds={{waitTimeSeconds}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextChunkToken](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-nextChunkToken"></a>
The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [recommendationType](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-recommendationType"></a>
The type of recommendation being requested.
Valid Values: `KNOWLEDGE_CONTENT | GENERATIVE_RESPONSE | GENERATIVE_ANSWER | DETECTED_INTENT | GENERATIVE_ANSWER_CHUNK | BLOCKED_GENERATIVE_ANSWER_CHUNK | INTENT_ANSWER_CHUNK | BLOCKED_INTENT_ANSWER_CHUNK | EMAIL_RESPONSE_CHUNK | EMAIL_OVERVIEW_CHUNK | EMAIL_GENERATIVE_ANSWER_CHUNK | CASE_SUMMARIZATION_CHUNK | BLOCKED_CASE_SUMMARIZATION_CHUNK | SUGGESTED_MESSAGE | NOTES_CHUNK | BLOCKED_NOTES_CHUNK`

 ** [sessionId](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-sessionId"></a>
The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [waitTimeSeconds](#API_amazon-q-connect_GetRecommendations_RequestSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-request-uri-waitTimeSeconds"></a>
The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than `WaitTimeSeconds`. If no messages are available and the wait time expires, the call returns successfully with an empty list.
Valid Range: Minimum value of 0. Maximum value of 20.

## Request Body
<a name="API_amazon-q-connect_GetRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recommendations": [
      {
         "data": {
            "details": { ... },
            "reference": { ... }
         },
         "document": {
            "contentReference": {
               "contentArn": "string",
               "contentId": "string",
               "knowledgeBaseArn": "string",
               "knowledgeBaseId": "string",
               "referenceType": "string",
               "sourceURL": "string"
            },
            "excerpt": {
               "highlights": [
                  {
                     "beginOffsetInclusive": number,
                     "endOffsetExclusive": number
                  }
               ],
               "text": "string"
            },
            "title": {
               "highlights": [
                  {
                     "beginOffsetInclusive": number,
                     "endOffsetExclusive": number
                  }
               ],
               "text": "string"
            }
         },
         "recommendationId": "string",
         "relevanceLevel": "string",
         "relevanceScore": number,
         "type": "string"
      }
   ],
   "triggers": [
      {
         "data": { ... },
         "id": "string",
         "recommendationIds": [ "string" ],
         "source": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_GetRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendations](#API_amazon-q-connect_GetRecommendations_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-response-recommendations"></a>
The recommendations.
Type: Array of [RecommendationData](API_amazon-q-connect_RecommendationData.md) objects

 ** [triggers](#API_amazon-q-connect_GetRecommendations_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetRecommendations-response-triggers"></a>
The triggers corresponding to recommendations.
Type: Array of [RecommendationTrigger](API_amazon-q-connect_RecommendationTrigger.md) objects

## Errors
<a name="API_amazon-q-connect_GetRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_GetRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetRecommendations)
