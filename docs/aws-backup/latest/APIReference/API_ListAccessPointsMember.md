---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListAccessPointsMember.html
---

# ListAccessPointsMember
<a name="API_ListAccessPointsMember"></a>

Contains metadata about a backup access point.

## Contents
<a name="API_ListAccessPointsMember_Contents"></a>

 ** AccessPointArn **   <a name="Backup-Type-ListAccessPointsMember-AccessPointArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the backup access point.
Type: String
Pattern: `(arn:aws[a-z-]*:backup:[a-z-\d]+:\d{12}:accesspoint/)[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`
Required: Yes

 ** AccessPointMetadata **   <a name="Backup-Type-ListAccessPointsMember-AccessPointMetadata"></a>
Metadata for the backup access point. After the backup access point reaches the `AVAILABLE` status, this map contains `S3AccessPointArn` and `S3AccessPointAlias`, which you use with standard Amazon S3 read APIs to access the backup data. For continuous recovery points, this map also contains `AccessPointInTime` (in format `2021-11-27T03:30:27Z`). The access point provides access to the content present in the backup at that specific time.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: Yes

 ** BackupVaultName **   <a name="Backup-Type-ListAccessPointsMember-BackupVaultName"></a>
The name of the backup vault that contains the recovery point.
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

 ** CreationTime **   <a name="Backup-Type-ListAccessPointsMember-CreationTime"></a>
The date and time that the backup access point was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: Yes

 ** Name **   <a name="Backup-Type-ListAccessPointsMember-Name"></a>
The name of the backup access point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Pattern: `[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`
Required: Yes

 ** RecoveryPointArn **   <a name="Backup-Type-ListAccessPointsMember-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the recovery point that the backup access point provides access to.
Type: String
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:[a-z-\d]+:).+`
Required: Yes

 ** ResourceArn **   <a name="Backup-Type-ListAccessPointsMember-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that was backed up, such as an Amazon S3 bucket.
Type: String
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:).+`
Required: Yes

 ** ResourceType **   <a name="Backup-Type-ListAccessPointsMember-ResourceType"></a>
The type of AWS resource associated with the recovery point. For example, `S3` for Amazon Simple Storage Service.
Type: String
Required: Yes

 ** Status **   <a name="Backup-Type-ListAccessPointsMember-Status"></a>
The current status of the backup access point.
Type: String
Valid Values: `AVAILABLE | CREATING | DELETING | DISASSOCIATED | DISASSOCIATING | EXPIRED | FAILED`
Required: Yes

 ** BackupVaultArn **   <a name="Backup-Type-ListAccessPointsMember-BackupVaultArn"></a>
The Amazon Resource Name (ARN) of the backup vault that contains the recovery point.
Type: String
Required: No

 ** StatusMessage **   <a name="Backup-Type-ListAccessPointsMember-StatusMessage"></a>
A message that provides additional detail about the status of the backup access point, such as the reason a creation or deletion attempt failed.
Type: String
Required: No

## See Also
<a name="API_ListAccessPointsMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListAccessPointsMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListAccessPointsMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListAccessPointsMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
