---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRecoveryPointRestoreMetadata.html
---

# GetRecoveryPointRestoreMetadata
<a name="API_GetRecoveryPointRestoreMetadata"></a>

Returns a set of metadata key-value pairs that were used to create the backup.

## Request Syntax
<a name="API_GetRecoveryPointRestoreMetadata_RequestSyntax"></a>

```
GET /backup-vaults/{{backupVaultName}}/recovery-points/{{recoveryPointArn}}/restore-metadata?backupVaultAccountId={{BackupVaultAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecoveryPointRestoreMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BackupVaultAccountId](#API_GetRecoveryPointRestoreMetadata_RequestSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-request-uri-BackupVaultAccountId"></a>
The account ID of the specified backup vault.
Pattern: `^[0-9]{12}$`

 ** [backupVaultName](#API_GetRecoveryPointRestoreMetadata_RequestSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

 ** [recoveryPointArn](#API_GetRecoveryPointRestoreMetadata_RequestSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-request-uri-RecoveryPointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Required: Yes

## Request Body
<a name="API_GetRecoveryPointRestoreMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecoveryPointRestoreMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "string",
   "RecoveryPointArn": "string",
   "ResourceType": "string",
   "RestoreMetadata": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetRecoveryPointRestoreMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupVaultArn](#API_GetRecoveryPointRestoreMetadata_ResponseSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-response-BackupVaultArn"></a>
An ARN that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String

 ** [RecoveryPointArn](#API_GetRecoveryPointRestoreMetadata_ResponseSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-response-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String

 ** [ResourceType](#API_GetRecoveryPointRestoreMetadata_ResponseSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-response-ResourceType"></a>
The resource type of the recovery point.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [RestoreMetadata](#API_GetRecoveryPointRestoreMetadata_ResponseSyntax) **   <a name="Backup-GetRecoveryPointRestoreMetadata-response-RestoreMetadata"></a>
The set of metadata key-value pairs that describe the original configuration of the backed-up resource. These values vary depending on the service that is being restored.
Type: String to string map

## Errors
<a name="API_GetRecoveryPointRestoreMetadata_Errors"></a>

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
<a name="API_GetRecoveryPointRestoreMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetRecoveryPointRestoreMetadata)
