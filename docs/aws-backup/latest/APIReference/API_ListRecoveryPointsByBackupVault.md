---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRecoveryPointsByBackupVault.html
---

# ListRecoveryPointsByBackupVault
<a name="API_ListRecoveryPointsByBackupVault"></a>

Returns detailed information about the recovery points stored in a backup vault.

## Request Syntax
<a name="API_ListRecoveryPointsByBackupVault_RequestSyntax"></a>

```
GET /backup-vaults/{{backupVaultName}}/recovery-points/?backupPlanId={{ByBackupPlanId}}&backupVaultAccountId={{BackupVaultAccountId}}&createdAfter={{ByCreatedAfter}}&createdBefore={{ByCreatedBefore}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&parentRecoveryPointArn={{ByParentRecoveryPointArn}}&resourceArn={{ByResourceArn}}&resourceType={{ByResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecoveryPointsByBackupVault_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BackupVaultAccountId](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-BackupVaultAccountId"></a>
This parameter will sort the list of recovery points by account ID.
Pattern: `^[0-9]{12}$`

 ** [backupVaultName](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Backup vault name might not be available when a supported service creates the backup.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

 ** [ByBackupPlanId](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByBackupPlanId"></a>
Returns only recovery points that match the specified backup plan ID.

 ** [ByCreatedAfter](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByCreatedAfter"></a>
Returns only recovery points that were created after the specified timestamp.

 ** [ByCreatedBefore](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByCreatedBefore"></a>
Returns only recovery points that were created before the specified timestamp.

 ** [ByParentRecoveryPointArn](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByParentRecoveryPointArn"></a>
This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN).

 ** [ByResourceArn](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByResourceArn"></a>
Returns only recovery points that match the specified resource Amazon Resource Name (ARN).

 ** [ByResourceType](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-ByResourceType"></a>
Returns only recovery points that match the specified resource type(s):
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

 ** [MaxResults](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRecoveryPointsByBackupVault_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListRecoveryPointsByBackupVault_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecoveryPointsByBackupVault_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecoveryPoints": [
      {
         "AggregatedScanResult": {
            "FailedScan": boolean,
            "Findings": [ "string" ],
            "LastComputed": number
         },
         "BackupSizeInBytes": number,
         "BackupVaultArn": "string",
         "BackupVaultName": "string",
         "CalculatedLifecycle": {
            "DeleteAt": number,
            "MoveToColdStorageAt": number
         },
         "CompletionDate": number,
         "CompositeMemberIdentifier": "string",
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
         "CreationDate": number,
         "EncryptionKeyArn": "string",
         "EncryptionKeyType": "string",
         "IamRoleArn": "string",
         "IndexStatus": "string",
         "IndexStatusMessage": "string",
         "InitiationDate": number,
         "IsEncrypted": boolean,
         "IsParent": boolean,
         "LastRestoreTime": number,
         "Lifecycle": {
            "DeleteAfterDays": number,
            "DeleteAfterEvent": "string",
            "MoveToColdStorageAfterDays": number,
            "OptInToArchiveForSupportedResources": boolean
         },
         "ParentRecoveryPointArn": "string",
         "RecoveryPointArn": "string",
         "ResourceArn": "string",
         "ResourceName": "string",
         "ResourceType": "string",
         "SourceBackupVaultArn": "string",
         "Status": "string",
         "StatusMessage": "string",
         "VaultType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecoveryPointsByBackupVault_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecoveryPointsByBackupVault_ResponseSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [RecoveryPoints](#API_ListRecoveryPointsByBackupVault_ResponseSyntax) **   <a name="Backup-ListRecoveryPointsByBackupVault-response-RecoveryPoints"></a>
An array of objects that contain detailed information about recovery points saved in a backup vault.
Type: Array of [RecoveryPointByBackupVault](API_RecoveryPointByBackupVault.md) objects

## Errors
<a name="API_ListRecoveryPointsByBackupVault_Errors"></a>

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
<a name="API_ListRecoveryPointsByBackupVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRecoveryPointsByBackupVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByBackupVault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
