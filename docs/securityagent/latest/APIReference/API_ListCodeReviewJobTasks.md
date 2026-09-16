---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListCodeReviewJobTasks.html
---

# ListCodeReviewJobTasks
<a name="API_ListCodeReviewJobTasks"></a>

Returns a paginated list of task summaries for the specified code review job, optionally filtered by step name or category.

## Request Syntax
<a name="API_ListCodeReviewJobTasks_RequestSyntax"></a>

```
POST /ListCodeReviewJobTasks HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "categoryName": "{{string}}",
   "codeReviewJobId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "stepName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCodeReviewJobTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCodeReviewJobTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [categoryName](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-categoryName"></a>
Filter tasks by category name.
Type: String
Required: No

 ** [codeReviewJobId](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-codeReviewJobId"></a>
The unique identifier of the code review job to list tasks for.
Type: String
Required: No

 ** [maxResults](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

 ** [stepName](#API_ListCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-request-stepName"></a>
Filter tasks by step name.
Type: String
Valid Values: `PREFLIGHT | STATIC_ANALYSIS | PENTEST | FINALIZING | VALIDATION`
Required: No

## Response Syntax
<a name="API_ListCodeReviewJobTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviewJobTaskSummaries": [
      {
         "agentSpaceId": "string",
         "codeReviewId": "string",
         "codeReviewJobId": "string",
         "createdAt": "string",
         "executionStatus": "string",
         "riskType": "string",
         "taskId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeReviewJobTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviewJobTaskSummaries](#API_ListCodeReviewJobTasks_ResponseSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-response-codeReviewJobTaskSummaries"></a>
The list of code review job task summaries.
Type: Array of [CodeReviewJobTaskSummary](API_CodeReviewJobTaskSummary.md) objects

 ** [nextToken](#API_ListCodeReviewJobTasks_ResponseSyntax) **   <a name="securityagent-ListCodeReviewJobTasks-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListCodeReviewJobTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCodeReviewJobTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListCodeReviewJobTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListCodeReviewJobTasks)
