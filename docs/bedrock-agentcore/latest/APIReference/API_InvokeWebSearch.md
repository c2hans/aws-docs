---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeWebSearch.html
---

# InvokeWebSearch
<a name="API_InvokeWebSearch"></a>

Searches the web and returns a ranked list of results. Each result includes a text extract from the page.

You can filter the results by domain and by publication date.

To use this operation, you must have the `bedrock-agentcore:InvokeWebSearch` permission on the resource `arn:${Partition}:bedrock-agentcore:${Region}:aws:tool/web-search.v1`.

## Request Syntax
<a name="API_InvokeWebSearch_RequestSyntax"></a>

```
POST /web-search/{{webSearchId}}/invoke HTTP/1.1
Content-type: application/json

{
   "filters": {
      "domainFilter": {
         "exclude": [ "{{string}}" ],
         "include": [ "{{string}}" ]
      },
      "publishedDateFilter": {
         "publishedAfter": "{{string}}",
         "publishedBefore": "{{string}}"
      }
   },
   "maxResults": {{number}},
   "searchQuery": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InvokeWebSearch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [webSearchId](#API_InvokeWebSearch_RequestSyntax) **   <a name="BedrockAgentCore-InvokeWebSearch-request-uri-webSearchId"></a>
The identifier of the web search tool to invoke. The AWS-managed web search tool is `web-search.v1`.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+([.-][a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_InvokeWebSearch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_InvokeWebSearch_RequestSyntax) **   <a name="BedrockAgentCore-InvokeWebSearch-request-filters"></a>
The filters to apply to the search results.
Type: [WebSearchFilters](API_WebSearchFilters.md) object
Required: No

 ** [maxResults](#API_InvokeWebSearch_RequestSyntax) **   <a name="BedrockAgentCore-InvokeWebSearch-request-maxResults"></a>
The maximum number of results to return. Defaults to 25.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [searchQuery](#API_InvokeWebSearch_RequestSyntax) **   <a name="BedrockAgentCore-InvokeWebSearch-request-searchQuery"></a>
The text to search for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Response Syntax
<a name="API_InvokeWebSearch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "results": [
      {
         "publishedAt": "string",
         "text": "string",
         "title": "string",
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_InvokeWebSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_InvokeWebSearch_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeWebSearch-response-results"></a>
The search results, in ranked order.
Type: Array of [WebSearchResult](API_WebSearchResult.md) objects

## Errors
<a name="API_InvokeWebSearch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.
HTTP Status Code: 403

 ** InternalServerException **
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service can't handle the request right now. Retry the request. If the response includes `retryAfterSeconds`, wait that many seconds before you retry.
 ** message **
A message that describes the error.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request.
HTTP Status Code: 503

 ** ThrottlingException **
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.
HTTP Status Code: 429

 ** ValidationException **
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.
HTTP Status Code: 400

## See Also
<a name="API_InvokeWebSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeWebSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeWebSearch)
