---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryAssistant.html
---

# QueryAssistant
<a name="API_amazon-q-connect_QueryAssistant"></a>

**Important**
This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.

Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use [GetRecommendations](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html).

## Request Syntax
<a name="API_amazon-q-connect_QueryAssistant_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/query HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "overrideKnowledgeBaseSearchType": "{{string}}",
   "queryCondition": [
      { ... }
   ],
   "queryInputData": { ... },
   "queryText": "{{string}}",
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_QueryAssistant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_QueryAssistant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [overrideKnowledgeBaseSearchType](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-overrideKnowledgeBaseSearchType"></a>
The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text.
Type: String
Valid Values: `HYBRID | SEMANTIC`
Required: No

 ** [queryCondition](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-queryCondition"></a>
Information about how to query content.
Type: Array of [QueryCondition](API_amazon-q-connect_QueryCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [queryInputData](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-queryInputData"></a>
Information about the query.
Type: [QueryInputData](API_amazon-q-connect_QueryInputData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [queryText](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-queryText"></a>
The text to search for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** [sessionId](#API_amazon-q-connect_QueryAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-request-sessionId"></a>
The identifier of the Amazon Q in Connect session. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: No

## Response Syntax
<a name="API_amazon-q-connect_QueryAssistant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "results": [
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
         "relevanceScore": number,
         "resultId": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_QueryAssistant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_amazon-q-connect_QueryAssistant_ResponseSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [results](#API_amazon-q-connect_QueryAssistant_ResponseSyntax) **   <a name="connect-amazon-q-connect_QueryAssistant-response-results"></a>
The results of the query.
Type: Array of [ResultData](API_amazon-q-connect_ResultData.md) objects

## Errors
<a name="API_amazon-q-connect_QueryAssistant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** RequestTimeoutException **
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_QueryAssistant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/QueryAssistant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QueryAssistant)
