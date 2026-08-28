---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRestoreJobsByProtectedResource.html
---

# ListRestoreJobsByProtectedResource
<a name="API_ListRestoreJobsByProtectedResource"></a>

This returns restore jobs that contain the specified protected resource.

You must include `ResourceArn`. You can optionally include `NextToken`, `ByStatus`, `MaxResults`, `ByRecoveryPointCreationDateAfter` , and `ByRecoveryPointCreationDateBefore`.

## Request Syntax
<a name="API_ListRestoreJobsByProtectedResource_RequestSyntax"></a>

```
GET /resources/{{resourceArn}}/restore-jobs/?maxResults={{MaxResults}}&nextToken={{NextToken}}&recoveryPointCreationDateAfter={{ByRecoveryPointCreationDateAfter}}&recoveryPointCreationDateBefore={{ByRecoveryPointCreationDateBefore}}&status={{ByStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRestoreJobsByProtectedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByRecoveryPointCreationDateAfter](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-ByRecoveryPointCreationDateAfter"></a>
Returns only restore jobs of recovery points that were created after the specified date.

 ** [ByRecoveryPointCreationDateBefore](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-ByRecoveryPointCreationDateBefore"></a>
Returns only restore jobs of recovery points that were created before the specified date.

 ** [ByStatus](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-ByStatus"></a>
Returns only restore jobs associated with the specified job status.
Valid Values: `PENDING | RUNNING | COMPLETED | ABORTED | FAILED`

 ** [MaxResults](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request ismade to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [resourceArn](#API_ListRestoreJobsByProtectedResource_RequestSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-request-uri-ResourceArn"></a>
Returns only restore jobs that match the specified resource Amazon Resource Name (ARN).
Required: Yes

## Request Body
<a name="API_ListRestoreJobsByProtectedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRestoreJobsByProtectedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RestoreJobs": [
      {
         "AccountId": "string",
         "BackupSizeInBytes": number,
         "BackupVaultArn": "string",
         "CompletionDate": number,
         "CreatedBy": {
            "RestoreTestingPlanArn": "string"
         },
         "CreatedResourceArn": "string",
         "CreationDate": number,
         "DeletionStatus": "string",
         "DeletionStatusMessage": "string",
         "ExpectedCompletionTimeMinutes": number,
         "IamRoleArn": "string",
         "IsParent": boolean,
         "ParentJobId": "string",
         "PercentDone": "string",
         "RecoveryPointArn": "string",
         "RecoveryPointCreationDate": number,
         "ResourceType": "string",
         "RestoreJobId": "string",
         "SourceResourceArn": "string",
         "Status": "string",
         "StatusMessage": "string",
         "ValidationStatus": "string",
         "ValidationStatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRestoreJobsByProtectedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRestoreJobsByProtectedResource_ResponseSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows youto return more items in your list starting at the location pointed to by the next token
Type: String

 ** [RestoreJobs](#API_ListRestoreJobsByProtectedResource_ResponseSyntax) **   <a name="Backup-ListRestoreJobsByProtectedResource-response-RestoreJobs"></a>
An array of objects that contain detailed information about jobs to restore saved resources.>
Type: Array of [RestoreJobsListMember](API_RestoreJobsListMember.md) objects

## Errors
<a name="API_ListRestoreJobsByProtectedResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListRestoreJobsByProtectedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRestoreJobsByProtectedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobsByProtectedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
