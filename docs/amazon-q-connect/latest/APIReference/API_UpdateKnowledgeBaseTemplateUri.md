---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateKnowledgeBaseTemplateUri.html
---

# UpdateKnowledgeBaseTemplateUri
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri"></a>

Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in `${variable}` format; this interpolated by Amazon Q in Connect using ingested content. For example, if you ingest a Salesforce article, it has an `Id` value, and you can set the template URI to `https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view`.

## Request Syntax
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/templateUri HTTP/1.1
Content-type: application/json

{
   "templateUri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateKnowledgeBaseTemplateUri-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [templateUri](#API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateKnowledgeBaseTemplateUri-request-templateUri"></a>
The template URI to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBase](#API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateKnowledgeBaseTemplateUri-response-knowledgeBase"></a>
The knowledge base to update.
Type: [KnowledgeBaseData](API_amazon-q-connect_KnowledgeBaseData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_Errors"></a>

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
<a name="API_amazon-q-connect_UpdateKnowledgeBaseTemplateUri_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateKnowledgeBaseTemplateUri)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
