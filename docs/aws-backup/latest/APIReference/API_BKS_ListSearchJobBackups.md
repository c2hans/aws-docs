---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ListSearchJobBackups.html
---

# ListSearchJobBackups
<a name="API_BKS_ListSearchJobBackups"></a>

This operation returns a list of all backups (recovery points) in a paginated format that were included in the search job.

If a search does not display an expected backup in the results, you can call this operation to display each backup included in the search. Any backups that were not included because they have a `FAILED` status from a permissions issue will be displayed, along with a status message.

Only recovery points with a backup index that has a status of `ACTIVE` will be included in search results. If the index has any other status, its status will be displayed along with a status message.

## Request Syntax
<a name="API_BKS_ListSearchJobBackups_RequestSyntax"></a>

```
GET /search-jobs/{{SearchJobIdentifier}}/backups?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BKS_ListSearchJobBackups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_BKS_ListSearchJobBackups_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobBackups-request-uri-MaxResults"></a>
The maximum number of resource list items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_BKS_ListSearchJobBackups_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobBackups-request-uri-NextToken"></a>
The next item following a partial list of returned backups included in a search job.
For example, if a request is made to return `MaxResults` number of backups, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [SearchJobIdentifier](#API_BKS_ListSearchJobBackups_RequestSyntax) **   <a name="Backup-BKS_ListSearchJobBackups-request-uri-SearchJobIdentifier"></a>
The unique string that specifies the search job.
Required: Yes

## Request Body
<a name="API_BKS_ListSearchJobBackups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BKS_ListSearchJobBackups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": [
      {
         "BackupCreationTime": number,
         "BackupResourceArn": "string",
         "IndexCreationTime": number,
         "ResourceType": "string",
         "SourceResourceArn": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BKS_ListSearchJobBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_BKS_ListSearchJobBackups_ResponseSyntax) **   <a name="Backup-BKS_ListSearchJobBackups-response-NextToken"></a>
The next item following a partial list of returned backups included in a search job.
For example, if a request is made to return `MaxResults` number of backups, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [Results](#API_BKS_ListSearchJobBackups_ResponseSyntax) **   <a name="Backup-BKS_ListSearchJobBackups-response-Results"></a>
The recovery points returned the results of a search job
Type: Array of [SearchJobBackupsResult](API_BKS_SearchJobBackupsResult.md) objects

## Errors
<a name="API_BKS_ListSearchJobBackups_Errors"></a>

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

 ** ResourceNotFoundException **
The resource was not found for this request.
Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.
 ** message **
Request references a resource which does not exist.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

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
<a name="API_BKS_ListSearchJobBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/ListSearchJobBackups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ListSearchJobBackups)
