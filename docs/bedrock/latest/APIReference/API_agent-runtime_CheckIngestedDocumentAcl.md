---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CheckIngestedDocumentAcl.html
---

# CheckIngestedDocumentAcl
<a name="API_agent-runtime_CheckIngestedDocumentAcl"></a>

Checks whether a user has access to a specific document by verifying against the ingested access control list (ACL) in a knowledge base. Use this operation to validate that document-level access control is working as expected after ingestion. To use this operation, you must have the `bedrock:CheckIngestedDocumentAcl` permission.

## Request Syntax
<a name="API_agent-runtime_CheckIngestedDocumentAcl_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/check-ingested-document-acl HTTP/1.1
Content-type: application/json

{
   "documentId": "{{string}}",
   "userContext": {
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_CheckIngestedDocumentAcl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent-runtime_CheckIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_CheckIngestedDocumentAcl-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the document.
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** [knowledgeBaseId](#API_agent-runtime_CheckIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_CheckIngestedDocumentAcl-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that contains the document.
Length Constraints: Minimum length of 10. Maximum length of 2048.
Pattern: `[0-9a-zA-Z]{10}$|^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]{10}`
Required: Yes

## Request Body
<a name="API_agent-runtime_CheckIngestedDocumentAcl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [documentId](#API_agent-runtime_CheckIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_CheckIngestedDocumentAcl-request-documentId"></a>
The unique identifier of the document to check access for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: Yes

 ** [userContext](#API_agent-runtime_CheckIngestedDocumentAcl_RequestSyntax) **   <a name="bedrock-agent-runtime_CheckIngestedDocumentAcl-request-userContext"></a>
The context object containing identity information for access control filtering, including user ID and optional group memberships used to evaluate the document access control list (ACL).
Type: [UserContext](API_agent-runtime_UserContext.md) object
Required: Yes

## Response Syntax
<a name="API_agent-runtime_CheckIngestedDocumentAcl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "hasAccess": boolean
}
```

## Response Elements
<a name="API_agent-runtime_CheckIngestedDocumentAcl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasAccess](#API_agent-runtime_CheckIngestedDocumentAcl_ResponseSyntax) **   <a name="bedrock-agent-runtime_CheckIngestedDocumentAcl-response-hasAccess"></a>
Specifies whether the user has access to the document based on the ingested access control list (ACL). Returns `true` if the user is allowed access, and `false` otherwise.
Type: Boolean

## Errors
<a name="API_agent-runtime_CheckIngestedDocumentAcl_Errors"></a>

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
<a name="API_agent-runtime_CheckIngestedDocumentAcl_Examples"></a>

### Check if a user has access to a document
<a name="API_agent-runtime_CheckIngestedDocumentAcl_Example_1"></a>

The following example checks whether a specific user has access to a document in a knowledge base based on the ingested ACL.

#### Sample Request
<a name="API_agent-runtime_CheckIngestedDocumentAcl_Example_1_Request"></a>

```
POST /knowledgebases/KB12345678/datasources/DS12345678/check-ingested-document-acl HTTP/1.1
Content-type: application/json

{
    "documentId": "doc-001",
    "userContext": {
        "userId": "user@example.com",
        "userGroups": [
            {
                "id": "engineering",
                "type": "KNOWLEDGE_BASE"
            }
        ]
    }
}
```

## See Also
<a name="API_agent-runtime_CheckIngestedDocumentAcl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/CheckIngestedDocumentAcl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
