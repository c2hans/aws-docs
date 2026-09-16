---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListCodeReviews.html
---

# ListCodeReviews
<a name="API_ListCodeReviews"></a>

Returns a paginated list of code review summaries for the specified agent space.

## Request Syntax
<a name="API_ListCodeReviews_RequestSyntax"></a>

```
POST /ListCodeReviews HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCodeReviews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCodeReviews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListCodeReviews_RequestSyntax) **   <a name="securityagent-ListCodeReviews-request-agentSpaceId"></a>
The unique identifier of the agent space to list code reviews for.
Type: String
Required: Yes

 ** [maxResults](#API_ListCodeReviews_RequestSyntax) **   <a name="securityagent-ListCodeReviews-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListCodeReviews_RequestSyntax) **   <a name="securityagent-ListCodeReviews-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListCodeReviews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviewSummaries": [
      {
         "agentSpaceId": "string",
         "codeReviewId": "string",
         "createdAt": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeReviews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviewSummaries](#API_ListCodeReviews_ResponseSyntax) **   <a name="securityagent-ListCodeReviews-response-codeReviewSummaries"></a>
The list of code review summaries.
Type: Array of [CodeReviewSummary](API_CodeReviewSummary.md) objects

 ** [nextToken](#API_ListCodeReviews_ResponseSyntax) **   <a name="securityagent-ListCodeReviews-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListCodeReviews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCodeReviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListCodeReviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListCodeReviews)
