---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupDetails.html
---

# BackupDetails
<a name="API_BackupDetails"></a>

Contains the details of the backup created for the table.

## Contents
<a name="API_BackupDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackupArn **   <a name="DDB-Type-BackupDetails-BackupArn"></a>
ARN associated with the backup.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

 ** BackupCreationDateTime **   <a name="DDB-Type-BackupDetails-BackupCreationDateTime"></a>
Time at which the backup was created. This is the request time of the backup.
Type: Timestamp
Required: Yes

 ** BackupName **   <a name="DDB-Type-BackupDetails-BackupName"></a>
Name of the requested backup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** BackupStatus **   <a name="DDB-Type-BackupDetails-BackupStatus"></a>
Backup can be in one of the following states: CREATING, ACTIVE, DELETED.
Type: String
Valid Values: `CREATING | DELETED | AVAILABLE`
Required: Yes

 ** BackupType **   <a name="DDB-Type-BackupDetails-BackupType"></a>
BackupType:
+  `USER` - You create and manage these using the on-demand backup feature.
+  `SYSTEM` - If you delete a table with point-in-time recovery enabled, a `SYSTEM` backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
+  `AWS_BACKUP` - On-demand backup created by you from AWS Backup service.
Type: String
Valid Values: `USER | SYSTEM | AWS_BACKUP`
Required: Yes

 ** BackupExpiryDateTime **   <a name="DDB-Type-BackupDetails-BackupExpiryDateTime"></a>
Time at which the automatic on-demand backup created by DynamoDB will expire. This `SYSTEM` on-demand backup expires automatically 35 days after its creation.
Type: Timestamp
Required: No

 ** BackupSizeBytes **   <a name="DDB-Type-BackupDetails-BackupSizeBytes"></a>
Size of the backup in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_BackupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BackupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BackupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BackupDetails)
