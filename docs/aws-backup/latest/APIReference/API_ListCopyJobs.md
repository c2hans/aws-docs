---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListCopyJobs.html
---

# ListCopyJobs
<a name="API_ListCopyJobs"></a>

Returns metadata about your copy jobs.

## Request Syntax
<a name="API_ListCopyJobs_RequestSyntax"></a>

```
GET /copy-jobs/?accountId={{ByAccountId}}&completeAfter={{ByCompleteAfter}}&completeBefore={{ByCompleteBefore}}&createdAfter={{ByCreatedAfter}}&createdBefore={{ByCreatedBefore}}&destinationVaultArn={{ByDestinationVaultArn}}&maxResults={{MaxResults}}&messageCategory={{ByMessageCategory}}&nextToken={{NextToken}}&parentJobId={{ByParentJobId}}&resourceArn={{ByResourceArn}}&resourceType={{ByResourceType}}&sourceRecoveryPointArn={{BySourceRecoveryPointArn}}&state={{ByState}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCopyJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByAccountId](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByAccountId"></a>
The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.
Pattern: `^[0-9]{12}$`

 ** [ByCompleteAfter](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByCompleteAfter"></a>
Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByCompleteBefore](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByCompleteBefore"></a>
Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByCreatedAfter](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByCreatedAfter"></a>
Returns only copy jobs that were created after the specified date.

 ** [ByCreatedBefore](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByCreatedBefore"></a>
Returns only copy jobs that were created before the specified date.

 ** [ByDestinationVaultArn](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByDestinationVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

 ** [ByMessageCategory](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByMessageCategory"></a>
This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.
Example strings may include `AccessDenied`, `SUCCESS`, `AGGREGATE_ALL`, and `INVALIDPARAMETERS`.
View [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of accepted strings.
The the value ANY returns count of all message categories.
 `AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum.

 ** [ByParentJobId](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByParentJobId"></a>
This is a filter to list child (nested) jobs based on parent job ID.

 ** [ByResourceArn](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByResourceArn"></a>
Returns only copy jobs that match the specified resource Amazon Resource Name (ARN).

 ** [ByResourceType](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByResourceType"></a>
Returns only backup jobs for the specified resources:
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

 ** [BySourceRecoveryPointArn](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-BySourceRecoveryPointArn"></a>
Filters copy jobs by the specified source recovery point ARN.

 ** [ByState](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-ByState"></a>
Returns only copy jobs that are in the specified state.
Valid Values: `CREATED | RUNNING | COMPLETED | FAILED | PARTIAL`

 ** [MaxResults](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListCopyJobs_RequestSyntax) **   <a name="Backup-ListCopyJobs-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListCopyJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCopyJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CopyJobs": [
      {
         "AccountId": "string",
         "BackupSizeInBytes": number,
         "ChildJobsInState": {
            "string" : number
         },
         "CompletionDate": number,
         "CompositeMemberIdentifier": "string",
         "CopyJobId": "string",
         "CreatedBy": {
            "BackupPlanArn": "string",
            "BackupPlanId": "string",
            "BackupPlanName": "string",
            "BackupPlanVersion": "string",
            "BackupRuleCron": "string",
            "BackupRuleId": "string",
            "BackupRuleName": "string",
            "BackupRuleTimezone": "string"
         },
         "CreatedByBackupJobId": "string",
         "CreationDate": number,
         "DestinationBackupVaultArn": "string",
         "DestinationEncryptionKeyArn": "string",
         "DestinationRecoveryPointArn": "string",
         "DestinationRecoveryPointLifecycle": {
            "DeleteAfterDays": number,
            "DeleteAfterEvent": "string",
            "MoveToColdStorageAfterDays": number,
            "OptInToArchiveForSupportedResources": boolean
         },
         "DestinationVaultLockState": "string",
         "DestinationVaultType": "string",
         "IamRoleArn": "string",
         "IsParent": boolean,
         "MessageCategory": "string",
         "NumberOfChildJobs": number,
         "ParentJobId": "string",
         "ResourceArn": "string",
         "ResourceName": "string",
         "ResourceType": "string",
         "SourceBackupVaultArn": "string",
         "SourceRecoveryPointArn": "string",
         "State": "string",
         "StatusMessage": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCopyJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CopyJobs](#API_ListCopyJobs_ResponseSyntax) **   <a name="Backup-ListCopyJobs-response-CopyJobs"></a>
An array of structures containing metadata about your copy jobs returned in JSON format.
Type: Array of [CopyJob](API_CopyJob.md) objects

 ** [NextToken](#API_ListCopyJobs_ResponseSyntax) **   <a name="Backup-ListCopyJobs-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

## Errors
<a name="API_ListCopyJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListCopyJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListCopyJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListCopyJobs)
