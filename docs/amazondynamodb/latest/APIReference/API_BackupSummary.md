---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupSummary.html
---

# BackupSummary
<a name="API_BackupSummary"></a>

Contains details for the backup.

## Contents
<a name="API_BackupSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackupArn **   <a name="DDB-Type-BackupSummary-BackupArn"></a>
ARN associated with the backup.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** BackupCreationDateTime **   <a name="DDB-Type-BackupSummary-BackupCreationDateTime"></a>
Time at which the backup was created.
Type: Timestamp
Required: No

 ** BackupExpiryDateTime **   <a name="DDB-Type-BackupSummary-BackupExpiryDateTime"></a>
Time at which the automatic on-demand backup created by DynamoDB will expire. This `SYSTEM` on-demand backup expires automatically 35 days after its creation.
Type: Timestamp
Required: No

 ** BackupName **   <a name="DDB-Type-BackupSummary-BackupName"></a>
Name of the specified backup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** BackupSizeBytes **   <a name="DDB-Type-BackupSummary-BackupSizeBytes"></a>
Size of the backup in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** BackupStatus **   <a name="DDB-Type-BackupSummary-BackupStatus"></a>
Backup can be in one of the following states: CREATING, ACTIVE, DELETED.
Type: String
Valid Values: `CREATING | DELETED | AVAILABLE`
Required: No

 ** BackupType **   <a name="DDB-Type-BackupSummary-BackupType"></a>
BackupType:
+  `USER` - You create and manage these using the on-demand backup feature.
+  `SYSTEM` - If you delete a table with point-in-time recovery enabled, a `SYSTEM` backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
+  `AWS_BACKUP` - On-demand backup created by you from AWS Backup service.
Type: String
Valid Values: `USER | SYSTEM | AWS_BACKUP`
Required: No

 ** TableArn **   <a name="DDB-Type-BackupSummary-TableArn"></a>
ARN associated with the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** TableId **   <a name="DDB-Type-BackupSummary-TableId"></a>
Unique identifier for the table.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** TableName **   <a name="DDB-Type-BackupSummary-TableName"></a>
Name of the table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_BackupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BackupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BackupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BackupSummary)
