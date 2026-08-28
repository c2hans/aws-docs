---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_StartSearchJob.html
---

# StartSearchJob
<a name="API_BKS_StartSearchJob"></a>

This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.

You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.

## Request Syntax
<a name="API_BKS_StartSearchJob_RequestSyntax"></a>

```
PUT /search-jobs HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "ItemFilters": {
      "EBSItemFilters": [
         {
            "CreationTimes": [
               {
                  "Operator": "{{string}}",
                  "Value": {{number}}
               }
            ],
            "FilePaths": [
               {
                  "Operator": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "LastModificationTimes": [
               {
                  "Operator": "{{string}}",
                  "Value": {{number}}
               }
            ],
            "Sizes": [
               {
                  "Operator": "{{string}}",
                  "Value": {{number}}
               }
            ]
         }
      ],
      "S3ItemFilters": [
         {
            "CreationTimes": [
               {
                  "Operator": "{{string}}",
                  "Value": {{number}}
               }
            ],
            "ETags": [
               {
                  "Operator": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "ObjectKeys": [
               {
                  "Operator": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "Sizes": [
               {
                  "Operator": "{{string}}",
                  "Value": {{number}}
               }
            ],
            "VersionIds": [
               {
                  "Operator": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ]
   },
   "Name": "{{string}}",
   "SearchScope": {
      "BackupResourceArns": [ "{{string}}" ],
      "BackupResourceCreationTime": {
         "CreatedAfter": {{number}},
         "CreatedBefore": {{number}}
      },
      "BackupResourceTags": {
         "{{string}}" : "{{string}}"
      },
      "BackupResourceTypes": [ "{{string}}" ],
      "SourceResourceArns": [ "{{string}}" ]
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_BKS_StartSearchJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BKS_StartSearchJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-ClientToken"></a>
Include this parameter to allow multiple identical calls for idempotency.
A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.
Type: String
Required: No

 ** [EncryptionKeyArn](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-EncryptionKeyArn"></a>
The encryption key for the specified search job.
Type: String
Required: No

 ** [ItemFilters](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-ItemFilters"></a>
Item Filters represent all input item properties specified when the search was created.
Contains either EBSItemFilters or S3ItemFilters
Type: [ItemFilters](API_BKS_ItemFilters.md) object
Required: No

 ** [Name](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-Name"></a>
Include alphanumeric characters to create a name for this search job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [SearchScope](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-SearchScope"></a>
This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.
Type: [SearchScope](API_BKS_SearchScope.md) object
Required: Yes

 ** [Tags](#API_BKS_StartSearchJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchJob-request-Tags"></a>
List of tags returned by the operation.
Type: String to string map
Required: No

## Response Syntax
<a name="API_BKS_StartSearchJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "SearchJobArn": "string",
   "SearchJobIdentifier": "string"
}
```

## Response Elements
<a name="API_BKS_StartSearchJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_BKS_StartSearchJob_ResponseSyntax) **   <a name="Backup-BKS_StartSearchJob-response-CreationTime"></a>
The date and time that a job was created, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [SearchJobArn](#API_BKS_StartSearchJob_ResponseSyntax) **   <a name="Backup-BKS_StartSearchJob-response-SearchJobArn"></a>
The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.
Type: String

 ** [SearchJobIdentifier](#API_BKS_StartSearchJob_ResponseSyntax) **   <a name="Backup-BKS_StartSearchJob-response-SearchJobIdentifier"></a>
The unique string that specifies the search job.
Type: String

## Errors
<a name="API_BKS_StartSearchJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.
A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** message **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
Identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request denied due to exceeding the quota limits permitted.
 ** message **
This request was not successful due to a service quota exceeding limits.
 ** quotaCode **
This is the code specific to the quota type.
 ** resourceId **
Identifier of the resource.
 ** resourceType **
Type of resource.
 ** serviceCode **
This is the code unique to the originating service with the quota.
HTTP Status Code: 402

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
<a name="API_BKS_StartSearchJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/StartSearchJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/StartSearchJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
