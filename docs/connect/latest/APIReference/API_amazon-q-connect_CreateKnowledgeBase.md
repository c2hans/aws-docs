---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateKnowledgeBase.html
---

# CreateKnowledgeBase
<a name="API_amazon-q-connect_CreateKnowledgeBase"></a>

Creates a knowledge base.

**Note**
When using this API, you cannot reuse [Amazon AppIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html) DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you'll get an `InvalidRequestException` error.
For example, you're programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:
Call [DeleteKnowledgeBase](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteKnowledgeBase.html).
Call [DeleteDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html).
Call [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html) to recreate the DataIntegration or a create different one.
Call CreateKnowledgeBase.

## Request Syntax
<a name="API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax"></a>

```
POST /knowledgeBases HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "knowledgeBaseType": "{{string}}",
   "name": "{{string}}",
   "renderingConfiguration": {
      "templateUri": "{{string}}"
   },
   "serverSideEncryptionConfiguration": {
      "kmsKeyId": "{{string}}"
   },
   "sourceConfiguration": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vectorIngestionConfiguration": {
      "chunkingConfiguration": {
         "chunkingStrategy": "{{string}}",
         "fixedSizeChunkingConfiguration": {
            "maxTokens": {{number}},
            "overlapPercentage": {{number}}
         },
         "hierarchicalChunkingConfiguration": {
            "levelConfigurations": [
               {
                  "maxTokens": {{number}}
               }
            ],
            "overlapTokens": {{number}}
         },
         "semanticChunkingConfiguration": {
            "breakpointPercentileThreshold": {{number}},
            "bufferSize": {{number}},
            "maxTokens": {{number}}
         }
      },
      "parsingConfiguration": {
         "bedrockFoundationModelConfiguration": {
            "modelArn": "{{string}}",
            "parsingPrompt": {
               "parsingPromptText": "{{string}}"
            }
         },
         "parsingStrategy": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateKnowledgeBase_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_amazon-q-connect_CreateKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [description](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [knowledgeBaseType](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-knowledgeBaseType"></a>
The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
Type: String
Valid Values: `EXTERNAL | CUSTOM | QUICK_RESPONSES | MESSAGE_TEMPLATES | MANAGED`
Required: Yes

 ** [name](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [renderingConfiguration](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-renderingConfiguration"></a>
Information about how to render the content.
Type: [RenderingConfiguration](API_amazon-q-connect_RenderingConfiguration.md) object
Required: No

 ** [serverSideEncryptionConfiguration](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-serverSideEncryptionConfiguration"></a>
The configuration information for the customer managed key used for encryption.
This KMS key must have a policy that allows `kms:CreateGrant`, `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect.
For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html).
Type: [ServerSideEncryptionConfiguration](API_amazon-q-connect_ServerSideEncryptionConfiguration.md) object
Required: No

 ** [sourceConfiguration](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-sourceConfiguration"></a>
The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
Type: [SourceConfiguration](API_amazon-q-connect_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [vectorIngestionConfiguration](#API_amazon-q-connect_CreateKnowledgeBase_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-request-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in a data source.
Type: [VectorIngestionConfiguration](API_amazon-q-connect_VectorIngestionConfiguration.md) object
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateKnowledgeBase_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_CreateKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBase](#API_amazon-q-connect_CreateKnowledgeBase_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateKnowledgeBase-response-knowledgeBase"></a>
The knowledge base.
Type: [KnowledgeBaseData](API_amazon-q-connect_KnowledgeBaseData.md) object

## Errors
<a name="API_amazon-q-connect_CreateKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateKnowledgeBase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
