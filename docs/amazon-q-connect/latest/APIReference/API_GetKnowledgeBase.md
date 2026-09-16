---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetKnowledgeBase.html
---

# GetKnowledgeBase
<a name="API_amazon-q-connect_GetKnowledgeBase"></a>

Retrieves information about the knowledge base.

## Request Syntax
<a name="API_amazon-q-connect_GetKnowledgeBase_RequestSyntax"></a>

```
GET /knowledgeBases/{{knowledgeBaseId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_GetKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_GetKnowledgeBase-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetKnowledgeBase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "knowledgeBase": {
      "description": "string",
      "ingestionFailureReasons": [ "string" ],
      "ingestionStatus": "string",
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "knowledgeBaseType": "string",
      "lastContentModificationTime": number,
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
}
```

## Response Elements
<a name="API_amazon-q-connect_GetKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBase](#API_amazon-q-connect_GetKnowledgeBase_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetKnowledgeBase-response-knowledgeBase"></a>
The knowledge base.
Type: [KnowledgeBaseData](API_amazon-q-connect_KnowledgeBaseData.md) object

## Errors
<a name="API_amazon-q-connect_GetKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_amazon-q-connect_GetKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetKnowledgeBase)
