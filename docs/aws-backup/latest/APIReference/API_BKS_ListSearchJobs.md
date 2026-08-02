---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ListSearchJobs.html
---

# ListSearchJobs
<a name="API_BKS_ListSearchJobs"></a>

This operation returns a list of search jobs belonging to an account.

## Request Syntax
<a name="API_BKS_ListSearchJobs_RequestSyntax"></a>

```
GET /search-jobs?MaxResults={{MaxResults}}&NextToken={{NextToken}}&Status={{ByStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BKS_ListSearchJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByStatus](#API_BKS_ListSearchJobs_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobs-request-uri-ByStatus"></a>
Include this parameter to filter list by search job status.
Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | FAILED`

 ** [MaxResults](#API_BKS_ListSearchJobs_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobs-request-uri-MaxResults"></a>
The maximum number of resource list items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_BKS_ListSearchJobs_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobs-request-uri-NextToken"></a>
The next item following a partial list of returned search jobs.
For example, if a request is made to return `MaxResults` number of backups, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_BKS_ListSearchJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BKS_ListSearchJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SearchJobs": [
      {
         "CompletionTime": number,
         "CreationTime": number,
         "Name": "string",
         "SearchJobArn": "string",
         "SearchJobIdentifier": "string",
         "SearchScopeSummary": {
            "TotalItemsToScanCount": number,
            "TotalRecoveryPointsToScanCount": number
         },
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BKS_ListSearchJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_BKS_ListSearchJobs_ResponseSyntax) **   <a name="Backup-BKS_ListSearchJobs-response-NextToken"></a>
The next item following a partial list of returned backups included in a search job.
For example, if a request is made to return `MaxResults` number of backups, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [SearchJobs](#API_BKS_ListSearchJobs_ResponseSyntax) **   <a name="Backup-BKS_ListSearchJobs-response-SearchJobs"></a>
The search jobs among the list, with details of the returned search jobs.
Type: Array of [SearchJobSummary](API_BKS_SearchJobSummary.md) objects

## Errors
<a name="API_BKS_ListSearchJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** message **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Retry the call after number of seconds.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Request was unsuccessful due to request throttling.
 ** quotaCode **
This is the code unique to the originating service with the quota.
 ** retryAfterSeconds **
Retry the call after number of seconds.
 ** serviceCode **
This is the code unique to the originating service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
 ** message **
The input fails to satisfy the constraints specified by an Amazon service.
HTTP Status Code: 400

## See Also
<a name="API_BKS_ListSearchJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/ListSearchJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ListSearchJobs)
