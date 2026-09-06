---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListKnowledgeBases.html
---

# ListKnowledgeBases
<a name="API_amazon-q-connect_ListKnowledgeBases"></a>

Lists the knowledge bases.

## Request Syntax
<a name="API_amazon-q-connect_ListKnowledgeBases_RequestSyntax"></a>

```
GET /knowledgeBases?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListKnowledgeBases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_amazon-q-connect_ListKnowledgeBases_RequestSyntax) **   <a name="connect-amazon-q-connect_ListKnowledgeBases-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_ListKnowledgeBases_RequestSyntax) **   <a name="connect-amazon-q-connect_ListKnowledgeBases-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Request Body
<a name="API_amazon-q-connect_ListKnowledgeBases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListKnowledgeBases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "knowledgeBaseSummaries": [
      {
         "description": "string",
         "knowledgeBaseArn": "string",
         "knowledgeBaseId": "string",
         "knowledgeBaseType": "string",
         "name": "string",
         "renderingConfiguration": {
            "templateUri": "string"
         },
         "serverSideEncryptionConfiguration": {
            "kmsKeyId": "string"
         },
         "sourceConfiguration": { ... },
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "vectorIngestionConfiguration": {
            "chunkingConfiguration": {
               "chunkingStrategy": "string",
               "fixedSizeChunkingConfiguration": {
                  "maxTokens": number,
                  "overlapPercentage": number
               },
               "hierarchicalChunkingConfiguration": {
                  "levelConfigurations": [
                     {
                        "maxTokens": number
                     }
                  ],
                  "overlapTokens": number
               },
               "semanticChunkingConfiguration": {
                  "breakpointPercentileThreshold": number,
                  "bufferSize": number,
                  "maxTokens": number
               }
            },
            "parsingConfiguration": {
               "bedrockFoundationModelConfiguration": {
                  "modelArn": "string",
                  "parsingPrompt": {
                     "parsingPromptText": "string"
                  }
               },
               "parsingStrategy": "string"
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListKnowledgeBases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBaseSummaries](#API_amazon-q-connect_ListKnowledgeBases_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListKnowledgeBases-response-knowledgeBaseSummaries"></a>
Information about the knowledge bases.
Type: Array of [KnowledgeBaseSummary](API_amazon-q-connect_KnowledgeBaseSummary.md) objects

 ** [nextToken](#API_amazon-q-connect_ListKnowledgeBases_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListKnowledgeBases-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_amazon-q-connect_ListKnowledgeBases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_ListKnowledgeBases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListKnowledgeBases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListKnowledgeBases)
