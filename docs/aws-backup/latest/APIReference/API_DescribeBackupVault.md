---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeBackupVault.html
---

# DescribeBackupVault
<a name="API_DescribeBackupVault"></a>

Returns metadata about a backup vault specified by its name.

## Request Syntax
<a name="API_DescribeBackupVault_RequestSyntax"></a>

```
GET /backup-vaults/{{backupVaultName}}?backupVaultAccountId={{BackupVaultAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBackupVault_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BackupVaultAccountId](#API_DescribeBackupVault_RequestSyntax) **   <a name="Backup-DescribeBackupVault-request-uri-BackupVaultAccountId"></a>
The account ID of the specified backup vault.

 ** [backupVaultName](#API_DescribeBackupVault_RequestSyntax) **   <a name="Backup-DescribeBackupVault-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Required: Yes

## Request Body
<a name="API_DescribeBackupVault_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBackupVault_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "string",
   "BackupVaultName": "string",
   "CreationDate": number,
   "CreatorRequestId": "string",
   "EncryptionKeyArn": "string",
   "EncryptionKeyType": "string",
   "LatestMpaApprovalTeamUpdate": {
      "ExpiryDate": number,
      "InitiationDate": number,
      "MpaSessionArn": "string",
      "Status": "string",
      "StatusMessage": "string"
   },
   "LockDate": number,
   "Locked": boolean,
   "MaxRetentionDays": number,
   "MinRetentionDays": number,
   "MpaApprovalTeamArn": "string",
   "MpaSessionArn": "string",
   "NumberOfRecoveryPoints": number,
   "SourceBackupVaultArn": "string",
   "VaultState": "string",
   "VaultType": "string"
}
```

## Response Elements
<a name="API_DescribeBackupVault_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupVaultArn](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-BackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String

 ** [BackupVaultName](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.
Type: String

 ** [CreationDate](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-CreationDate"></a>
The date and time that a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CreatorRequestId](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String

 ** [EncryptionKeyArn](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-EncryptionKeyArn"></a>
The server-side encryption key that is used to protect your backups; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
Type: String

 ** [EncryptionKeyType](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-EncryptionKeyType"></a>
The type of encryption key used for the backup vault. Valid values are CUSTOMER\_MANAGED\_KMS\_KEY for customer-managed keys or AWS\_OWNED\_KMS\_KEY for AWS-owned keys.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`

 ** [LatestMpaApprovalTeamUpdate](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-LatestMpaApprovalTeamUpdate"></a>
Information about the latest update to the MPA approval team association for this backup vault.
Type: [LatestMpaApprovalTeamUpdate](API_LatestMpaApprovalTeamUpdate.md) object

 ** [LockDate](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-LockDate"></a>
The date and time when AWS Backup Vault Lock configuration cannot be changed or deleted.
If you applied Vault Lock to your vault without specifying a lock date, you can change any of your Vault Lock settings, or delete Vault Lock from the vault entirely, at any time.
This value is in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [Locked](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-Locked"></a>
A Boolean that indicates whether AWS Backup Vault Lock is currently protecting the backup vault. `True` means that Vault Lock causes delete or update operations on the recovery points stored in the vault to fail.
Type: Boolean

 ** [MaxRetentionDays](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-MaxRetentionDays"></a>
The AWS Backup Vault Lock setting that specifies the maximum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock does not enforce a maximum retention period on the recovery points in the vault (allowing indefinite storage).
If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.
Type: Long

 ** [MinRetentionDays](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-MinRetentionDays"></a>
The AWS Backup Vault Lock setting that specifies the minimum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock will not enforce a minimum retention period.
If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.
Type: Long

 ** [MpaApprovalTeamArn](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-MpaApprovalTeamArn"></a>
The ARN of the MPA approval team associated with this backup vault.
Type: String

 ** [MpaSessionArn](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-MpaSessionArn"></a>
The ARN of the MPA session associated with this backup vault.
Type: String

 ** [NumberOfRecoveryPoints](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-NumberOfRecoveryPoints"></a>
The number of recovery points that are stored in a backup vault.
Recovery point count value displayed in the console can be an approximation. Use [`ListRecoveryPointsByBackupVault`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByBackupVault.html) API to obtain the exact count.
Type: Long

 ** [SourceBackupVaultArn](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-SourceBackupVaultArn"></a>
The ARN of the source backup vault from which this restore access backup vault was created.
Type: String

 ** [VaultState](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-VaultState"></a>
The current state of the vault.->
Type: String
Valid Values: `CREATING | AVAILABLE | FAILED`

 ** [VaultType](#API_DescribeBackupVault_ResponseSyntax) **   <a name="Backup-DescribeBackupVault-response-VaultType"></a>
The type of vault described.
Type: String
Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

## Errors
<a name="API_DescribeBackupVault_Errors"></a>

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
<a name="API_DescribeBackupVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DescribeBackupVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DescribeBackupVault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
