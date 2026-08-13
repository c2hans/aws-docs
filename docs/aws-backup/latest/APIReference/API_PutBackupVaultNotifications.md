---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutBackupVaultNotifications.html
---

# PutBackupVaultNotifications
<a name="API_PutBackupVaultNotifications"></a>

Turns on notifications on a backup vault for the specified topic and events.

## Request Syntax
<a name="API_PutBackupVaultNotifications_RequestSyntax"></a>

```
PUT /backup-vaults/{{backupVaultName}}/notification-configuration HTTP/1.1
Content-type: application/json

{
   "BackupVaultEvents": [ "{{string}}" ],
   "SNSTopicArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutBackupVaultNotifications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_PutBackupVaultNotifications_RequestSyntax) **   <a name="Backup-PutBackupVaultNotifications-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

## Request Body
<a name="API_PutBackupVaultNotifications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BackupVaultEvents](#API_PutBackupVaultNotifications_RequestSyntax) **   <a name="Backup-PutBackupVaultNotifications-request-BackupVaultEvents"></a>
An array of events that indicate the status of jobs to back up resources to the backup vault. For the list of supported events, common use cases, and code samples, see [Notification options with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html).
The list below includes both supported events and deprecated events that are no longer in use (for reference). Deprecated events do not return statuses or notifications.
Type: Array of strings
Valid Values: `BACKUP_JOB_STARTED | BACKUP_JOB_COMPLETED | BACKUP_JOB_SUCCESSFUL | BACKUP_JOB_FAILED | BACKUP_JOB_EXPIRED | RESTORE_JOB_STARTED | RESTORE_JOB_COMPLETED | RESTORE_JOB_SUCCESSFUL | RESTORE_JOB_FAILED | COPY_JOB_STARTED | COPY_JOB_SUCCESSFUL | COPY_JOB_FAILED | RECOVERY_POINT_MODIFIED | BACKUP_PLAN_CREATED | BACKUP_PLAN_MODIFIED | S3_BACKUP_OBJECT_FAILED | S3_RESTORE_OBJECT_FAILED | CONTINUOUS_BACKUP_INTERRUPTED | RECOVERY_POINT_INDEX_COMPLETED | RECOVERY_POINT_INDEX_DELETED | RECOVERY_POINT_INDEXING_FAILED | EKS_RESTORE_OBJECT_FAILED | EKS_RESTORE_OBJECT_SKIPPED | EKS_BACKUP_OBJECT_FAILED | ACCESS_POINT_AVAILABLE | ACCESS_POINT_CREATION_FAILED | ACCESS_POINT_DELETED | ACCESS_POINT_DELETION_FAILED | ACCESS_POINT_EXPIRED | ACCESS_POINT_DISASSOCIATED`
Required: Yes

 ** [SNSTopicArn](#API_PutBackupVaultNotifications_RequestSyntax) **   <a name="Backup-PutBackupVaultNotifications-request-SNSTopicArn"></a>
The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, `arn:aws:sns:us-west-2:111122223333:MyVaultTopic`.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutBackupVaultNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutBackupVaultNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutBackupVaultNotifications_Errors"></a>

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
<a name="API_PutBackupVaultNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/PutBackupVaultNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultNotifications)
