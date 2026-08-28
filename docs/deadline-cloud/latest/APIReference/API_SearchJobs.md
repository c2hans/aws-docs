---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchJobs.html
---

# SearchJobs
<a name="API_SearchJobs"></a>

Searches for jobs.

## Request Syntax
<a name="API_SearchJobs_RequestSyntax"></a>

```
POST /2023-10-12/farms/{{farmId}}/search/jobs HTTP/1.1
Content-type: application/json

{
   "filterExpressions": {
      "filters": [
         { ... }
      ],
      "operator": "{{string}}"
   },
   "itemOffset": {{number}},
   "pageSize": {{number}},
   "queueIds": [ "{{string}}" ],
   "sortExpressions": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_SearchJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-uri-farmId"></a>
The farm ID of the job.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_SearchJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterExpressions](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-filterExpressions"></a>
The search terms for a resource.
Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md) object
Required: No

 ** [itemOffset](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-itemOffset"></a>
The offset for the search results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: Yes

 ** [pageSize](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-pageSize"></a>
Specifies the number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [queueIds](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-queueIds"></a>
The queue ID to use in the job search.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** [sortExpressions](#API_SearchJobs_RequestSyntax) **   <a name="deadlinecloud-SearchJobs-request-sortExpressions"></a>
The search terms for a resource.
Type: Array of [SearchSortExpression](API_SearchSortExpression.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_SearchJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "endedAt": "string",
         "jobId": "string",
         "jobParameters": {
            "string" : { ... }
         },
         "lifecycleStatus": "string",
         "lifecycleStatusMessage": "string",
         "maxFailedTasksCount": number,
         "maxRetriesPerTask": number,
         "maxWorkerCount": number,
         "name": "string",
         "priority": number,
         "queueId": "string",
         "sourceJobId": "string",
         "startedAt": "string",
         "targetTaskRunStatus": "string",
         "taskFailureRetryCount": number,
         "taskRunStatus": "string",
         "taskRunStatusCounts": {
            "string" : number
         },
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ],
   "nextItemOffset": number,
   "totalResults": number
}
```

## Response Elements
<a name="API_SearchJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_SearchJobs_ResponseSyntax) **   <a name="deadlinecloud-SearchJobs-response-jobs"></a>
The jobs in the search.
Type: Array of [JobSearchSummary](API_JobSearchSummary.md) objects

 ** [nextItemOffset](#API_SearchJobs_ResponseSyntax) **   <a name="deadlinecloud-SearchJobs-response-nextItemOffset"></a>
The next item offset for the search results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.

 ** [totalResults](#API_SearchJobs_ResponseSyntax) **   <a name="deadlinecloud-SearchJobs-response-totalResults"></a>
The total number of results in the search.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.

## Errors
<a name="API_SearchJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_SearchJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
