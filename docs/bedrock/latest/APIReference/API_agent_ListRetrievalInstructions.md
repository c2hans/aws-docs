---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListRetrievalInstructions.html
---

# ListRetrievalInstructions
<a name="API_agent_ListRetrievalInstructions"></a>

Lists the retrieval instructions in the caller's account. Results are paginated. Use the nextToken parameter to retrieve additional results.

## Request Syntax
<a name="API_agent_ListRetrievalInstructions_RequestSyntax"></a>

```
GET /retrievalinstructions/?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListRetrievalInstructions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_agent_ListRetrievalInstructions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructions-request-uri-maxResults"></a>
The maximum number of results to return in a single page. The effective upper bound is enforced service-side.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_agent_ListRetrievalInstructions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructions-request-uri-nextToken"></a>
The pagination token from a previous ListRetrievalInstructions response.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [status](#API_agent_ListRetrievalInstructions_RequestSyntax) **   <a name="bedrock-agent_ListRetrievalInstructions-request-uri-status"></a>
Return only instructions with this availability status.
Valid Values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_agent_ListRetrievalInstructions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListRetrievalInstructions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "retrievalInstructionSummaries": [
      {
         "createdAt": "string",
         "description": "string",
         "lastTransitionStatus": "string",
         "name": "string",
         "retrievalInstructionArn": "string",
         "retrievalInstructionId": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_agent_ListRetrievalInstructions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_agent_ListRetrievalInstructions_ResponseSyntax) **   <a name="bedrock-agent_ListRetrievalInstructions-response-nextToken"></a>
The pagination token to pass to the next ListRetrievalInstructions call, absent on the last page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [retrievalInstructionSummaries](#API_agent_ListRetrievalInstructions_ResponseSyntax) **   <a name="bedrock-agent_ListRetrievalInstructions-response-retrievalInstructionSummaries"></a>
The retrieval instruction summaries in this page.
Type: Array of [RetrievalInstructionSummary](API_agent_RetrievalInstructionSummary.md) objects

## Errors
<a name="API_agent_ListRetrievalInstructions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ListRetrievalInstructions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListRetrievalInstructions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListRetrievalInstructions)
