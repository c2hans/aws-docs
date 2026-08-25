---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetIngestedDocumentAcl.html
---

# GetIngestedDocumentAcl
<a name="API_agent-runtime_GetIngestedDocumentAcl"></a>

Retrieves the ingested access control list (ACL) for a specific document in a knowledge base. Use this operation to inspect the allow and deny lists that were ingested for a document to troubleshoot access control issues. To use this operation, you must have the `bedrock:GetIngestedDocumentAcl` permission.

## Request Syntax
<a name="API_agent-runtime_GetIngestedDocumentAcl_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/get-ingested-document-acl HTTP/1.1
Content-type: application/json

{
   "documentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent-runtime_GetIngestedDocumentAcl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent-runtime_GetIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_GetIngestedDocumentAcl-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the document.
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** [knowledgeBaseId](#API_agent-runtime_GetIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_GetIngestedDocumentAcl-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that contains the document.
Length Constraints: Minimum length of 10. Maximum length of 2048.
Pattern: `[0-9a-zA-Z]{10}$|^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]{10}`
Required: Yes

## Request Body
<a name="API_agent-runtime_GetIngestedDocumentAcl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [documentId](#API_agent-runtime_GetIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_GetIngestedDocumentAcl-request-documentId"></a>
The unique identifier of the document to retrieve the ingested access control list (ACL) for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: Yes

## Response Syntax
<a name="API_agent-runtime_GetIngestedDocumentAcl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentAcl": {
      "allowList": {
         "conditions": [
            {
               "conditionOperator": "string",
               "groups": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ],
               "users": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ]
            }
         ],
         "memberRelation": "string"
      },
      "denyList": {
         "conditions": [
            {
               "conditionOperator": "string",
               "groups": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ],
               "users": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ]
            }
         ],
         "memberRelation": "string"
      }
   }
}
```

## Response Elements
<a name="API_agent-runtime_GetIngestedDocumentAcl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentAcl](#API_agent-runtime_GetIngestedDocumentAcl_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetIngestedDocumentAcl-response-documentAcl"></a>
The ingested document access control list (ACL) containing allow and deny membership information.
Type: [DocumentAcl](API_agent-runtime_DocumentAcl.md) object

## Errors
<a name="API_agent-runtime_GetIngestedDocumentAcl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions. Check your permissions and retry your request.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** reason **
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_GetIngestedDocumentAcl_Examples"></a>

### Retrieve the ingested ACL for a document
<a name="API_agent-runtime_GetIngestedDocumentAcl_Example_1"></a>

The following example retrieves the full ingested access control list (ACL) for a document, including both allow and deny membership lists.

#### Sample Request
<a name="API_agent-runtime_GetIngestedDocumentAcl_Example_1_Request"></a>

```
POST /knowledgebases/KB12345678/datasources/DS12345678/get-ingested-document-acl HTTP/1.1
Content-type: application/json

{
    "documentId": "doc-001"
}
```

## See Also
<a name="API_agent-runtime_GetIngestedDocumentAcl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetIngestedDocumentAcl)
