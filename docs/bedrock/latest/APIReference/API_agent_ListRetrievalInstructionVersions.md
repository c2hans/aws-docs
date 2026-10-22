---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListRetrievalInstructionVersions.html
---

# ListRetrievalInstructionVersions
<a name="API_agent_ListRetrievalInstructionVersions"></a>

Lists the numbered versions of a retrieval instruction, newest first. DRAFT is not listed; read it with GetRetrievalInstruction without retrievalInstructionVersion. Results are paginated. Use the nextToken parameter to retrieve additional results.

## Request Syntax
<a name="API_agent_ListRetrievalInstructionVersions_RequestSyntax"></a>

```
GET /retrievalinstructions/{{retrievalInstructionId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListRetrievalInstructionVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_agent_ListRetrievalInstructionVersions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructionVersions-request-uri-maxResults"></a>
Specifies the maximum number of versions to return in a single page. The service enforces the effective upper bound.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_agent_ListRetrievalInstructionVersions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructionVersions-request-uri-nextToken"></a>
The pagination token from a previous ListRetrievalInstructionVersions response.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [retrievalInstructionId](#API_agent_ListRetrievalInstructionVersions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructionVersions-request-uri-retrievalInstructionId"></a>
The identifier of the retrieval instruction whose versions to list.
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_agent_ListRetrievalInstructionVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListRetrievalInstructionVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "retrievalInstructionVersionSummaries": [
      {
         "createdAt": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_agent_ListRetrievalInstructionVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_agent_ListRetrievalInstructionVersions_ResponseSyntax) **   <a name="bedrock-agent_ListRetrievalInstructionVersions-response-nextToken"></a>
The pagination token to pass to the next ListRetrievalInstructionVersions call, absent on the last page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [retrievalInstructionVersionSummaries](#API_agent_ListRetrievalInstructionVersions_ResponseSyntax) **   <a name="bedrock-agent_ListRetrievalInstructionVersions-response-retrievalInstructionVersionSummaries"></a>
The version summaries in this page, newest first.
Type: Array of [RetrievalInstructionVersionSummary](API_agent_RetrievalInstructionVersionSummary.md) objects

## Errors
<a name="API_agent_ListRetrievalInstructionVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ListRetrievalInstructionVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListRetrievalInstructionVersions)
