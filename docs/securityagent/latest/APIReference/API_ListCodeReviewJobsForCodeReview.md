---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListCodeReviewJobsForCodeReview.html
---

# ListCodeReviewJobsForCodeReview
<a name="API_ListCodeReviewJobsForCodeReview"></a>

Returns a paginated list of code review job summaries for the specified code review configuration.

## Request Syntax
<a name="API_ListCodeReviewJobsForCodeReview_RequestSyntax"></a>

```
POST /ListCodeReviewJobsForCodeReview HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCodeReviewJobsForCodeReview_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCodeReviewJobsForCodeReview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListCodeReviewJobsForCodeReview_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [codeReviewId](#API_ListCodeReviewJobsForCodeReview_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-request-codeReviewId"></a>
The unique identifier of the code review to list jobs for.
Type: String
Required: Yes

 ** [maxResults](#API_ListCodeReviewJobsForCodeReview_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListCodeReviewJobsForCodeReview_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListCodeReviewJobsForCodeReview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviewJobSummaries": [
      {
         "codeReviewId": "string",
         "codeReviewJobId": "string",
         "createdAt": "string",
         "status": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeReviewJobsForCodeReview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviewJobSummaries](#API_ListCodeReviewJobsForCodeReview_ResponseSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-response-codeReviewJobSummaries"></a>
The list of code review job summaries.
Type: Array of [CodeReviewJobSummary](API_CodeReviewJobSummary.md) objects

 ** [nextToken](#API_ListCodeReviewJobsForCodeReview_ResponseSyntax) **   <a name="securityagent-ListCodeReviewJobsForCodeReview-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListCodeReviewJobsForCodeReview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCodeReviewJobsForCodeReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListCodeReviewJobsForCodeReview)
