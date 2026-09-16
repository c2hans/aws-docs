---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRestoreJobs.html
---

# ListRestoreJobs
<a name="API_ListRestoreJobs"></a>

Returns a list of jobs that AWS Backup initiated to restore a saved resource, including details about the recovery process.

## Request Syntax
<a name="API_ListRestoreJobs_RequestSyntax"></a>

```
GET /restore-jobs/?accountId={{ByAccountId}}&completeAfter={{ByCompleteAfter}}&completeBefore={{ByCompleteBefore}}&createdAfter={{ByCreatedAfter}}&createdBefore={{ByCreatedBefore}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&parentJobId={{ByParentJobId}}&resourceType={{ByResourceType}}&restoreTestingPlanArn={{ByRestoreTestingPlanArn}}&status={{ByStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRestoreJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByAccountId](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByAccountId"></a>
The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.
Pattern: `^[0-9]{12}$`

 ** [ByCompleteAfter](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByCompleteAfter"></a>
Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByCompleteBefore](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByCompleteBefore"></a>
Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByCreatedAfter](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByCreatedAfter"></a>
Returns only restore jobs that were created after the specified date.

 ** [ByCreatedBefore](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByCreatedBefore"></a>
Returns only restore jobs that were created before the specified date.

 ** [ByParentJobId](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByParentJobId"></a>
This is a filter to list child (nested) restore jobs based on parent restore job ID.

 ** [ByResourceType](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByResourceType"></a>
Include this parameter to return only restore jobs for the specified resources:
+  `Aurora` for Amazon Aurora
+  `CloudFormation` for AWS CloudFormation
+  `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
+  `DynamoDB` for Amazon DynamoDB
+  `EBS` for Amazon Elastic Block Store
+  `EC2` for Amazon Elastic Compute Cloud
+  `EFS` for Amazon Elastic File System
+  `EKS` for Amazon Elastic Kubernetes Service
+  `FSx` for Amazon FSx
+  `Neptune` for Amazon Neptune
+  `RDS` for Amazon Relational Database Service
+  `Redshift` for Amazon Redshift
+  `S3` for Amazon Simple Storage Service (Amazon S3)
+  `SAP HANA on Amazon EC2` for SAP HANA databases on Amazon Elastic Compute Cloud instances
+  `Storage Gateway` for AWS Storage Gateway
+  `Timestream` for Amazon Timestream
+  `VirtualMachine` for VMware virtual machines
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [ByRestoreTestingPlanArn](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByRestoreTestingPlanArn"></a>
This returns only restore testing jobs that match the specified resource Amazon Resource Name (ARN).

 ** [ByStatus](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-ByStatus"></a>
Returns only restore jobs associated with the specified job status.
Valid Values: `PENDING | RUNNING | COMPLETED | ABORTED | FAILED`

 ** [MaxResults](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRestoreJobs_RequestSyntax) **   <a name="Backup-ListRestoreJobs-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListRestoreJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRestoreJobs_ResponseSyntax"></a>

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
<a name="API_ListRestoreJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRestoreJobs_ResponseSyntax) **   <a name="Backup-ListRestoreJobs-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [RestoreJobs](#API_ListRestoreJobs_ResponseSyntax) **   <a name="Backup-ListRestoreJobs-response-RestoreJobs"></a>
An array of objects that contain detailed information about jobs to restore saved resources.
Type: Array of [RestoreJobsListMember](API_RestoreJobsListMember.md) objects

## Errors
<a name="API_ListRestoreJobs_Errors"></a>

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
<a name="API_ListRestoreJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRestoreJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobs)
