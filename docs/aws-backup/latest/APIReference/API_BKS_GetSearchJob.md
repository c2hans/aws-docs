---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_GetSearchJob.html
---

# GetSearchJob
<a name="API_BKS_GetSearchJob"></a>

This operation retrieves metadata of a search job, including its progress.

## Request Syntax
<a name="API_BKS_GetSearchJob_RequestSyntax"></a>

```
GET /search-jobs/{{SearchJobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BKS_GetSearchJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SearchJobIdentifier](#API_BKS_GetSearchJob_RequestSyntax) **   <a name="Backup-BKS_GetSearchJob-request-uri-SearchJobIdentifier"></a>
Required unique string that specifies the search job.
Required: Yes

## Request Body
<a name="API_BKS_GetSearchJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BKS_GetSearchJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CompletionTime": number,
   "CreationTime": number,
   "CurrentSearchProgress": {
      "ItemsMatchedCount": number,
      "ItemsScannedCount": number,
      "RecoveryPointsScannedCount": number
   },
   "EncryptionKeyArn": "string",
   "ItemFilters": {
      "EBSItemFilters": [
         {
            "CreationTimes": [
               {
                  "Operator": "string",
                  "Value": number
               }
            ],
            "FilePaths": [
               {
                  "Operator": "string",
                  "Value": "string"
               }
            ],
            "LastModificationTimes": [
               {
                  "Operator": "string",
                  "Value": number
               }
            ],
            "Sizes": [
               {
                  "Operator": "string",
                  "Value": number
               }
            ]
         }
      ],
      "S3ItemFilters": [
         {
            "CreationTimes": [
               {
                  "Operator": "string",
                  "Value": number
               }
            ],
            "ETags": [
               {
                  "Operator": "string",
                  "Value": "string"
               }
            ],
            "ObjectKeys": [
               {
                  "Operator": "string",
                  "Value": "string"
               }
            ],
            "Sizes": [
               {
                  "Operator": "string",
                  "Value": number
               }
            ],
            "VersionIds": [
               {
                  "Operator": "string",
                  "Value": "string"
               }
            ]
         }
      ]
   },
   "Name": "string",
   "SearchJobArn": "string",
   "SearchJobIdentifier": "string",
   "SearchScope": {
      "BackupResourceArns": [ "string" ],
      "BackupResourceCreationTime": {
         "CreatedAfter": number,
         "CreatedBefore": number
      },
      "BackupResourceTags": {
         "string" : "string"
      },
      "BackupResourceTypes": [ "string" ],
      "SourceResourceArns": [ "string" ]
   },
   "SearchScopeSummary": {
      "TotalItemsToScanCount": number,
      "TotalRecoveryPointsToScanCount": number
   },
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_BKS_GetSearchJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletionTime](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-CompletionTime"></a>
The date and time that a search job completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CreationTime](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-CreationTime"></a>
The date and time that a search job was created, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CurrentSearchProgress](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-CurrentSearchProgress"></a>
Returns numbers representing BackupsScannedCount, ItemsScanned, and ItemsMatched.
Type: [CurrentSearchProgress](API_BKS_CurrentSearchProgress.md) object

 ** [EncryptionKeyArn](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-EncryptionKeyArn"></a>
The encryption key for the specified search job.
Example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
Type: String

 ** [ItemFilters](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-ItemFilters"></a>
Item Filters represent all input item properties specified when the search was created.
Type: [ItemFilters](API_BKS_ItemFilters.md) object

 ** [Name](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-Name"></a>
Returned name of the specified search job.
Type: String

 ** [SearchJobArn](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-SearchJobArn"></a>
The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.
Type: String

 ** [SearchJobIdentifier](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-SearchJobIdentifier"></a>
The unique string that identifies the specified search job.
Type: String

 ** [SearchScope](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-SearchScope"></a>
The search scope is all backup properties input into a search.
Type: [SearchScope](API_BKS_SearchScope.md) object

 ** [SearchScopeSummary](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-SearchScopeSummary"></a>
Returned summary of the specified search job scope, including:
+ TotalBackupsToScanCount, the number of recovery points returned by the search.
+ TotalItemsToScanCount, the number of items returned by the search.
Type: [SearchScopeSummary](API_BKS_SearchScopeSummary.md) object

 ** [Status](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-Status"></a>
The current status of the specified search job.
A search job may have one of the following statuses: `RUNNING`; `COMPLETED`; `STOPPED`; `FAILED`; `TIMED_OUT`; or `EXPIRED` .
Type: String
Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | FAILED`

 ** [StatusMessage](#API_BKS_GetSearchJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchJob-response-StatusMessage"></a>
A status message will be returned for either a earch job with a status of `ERRORED` or a status of `COMPLETED` jobs with issues.
For example, a message may say that a search contained recovery points unable to be scanned because of a permissions issue.
Type: String

## Errors
<a name="API_BKS_GetSearchJob_Errors"></a>

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
<a name="API_BKS_GetSearchJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/GetSearchJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/GetSearchJob)
