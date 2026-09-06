---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingSelectionForList.html
---

# RestoreTestingSelectionForList
<a name="API_RestoreTestingSelectionForList"></a>

This contains metadata about a restore testing selection.

## Contents
<a name="API_RestoreTestingSelectionForList_Contents"></a>

 ** CreationTime **   <a name="Backup-Type-RestoreTestingSelectionForList-CreationTime"></a>
The date and time that a restore testing selection was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26,2018 12:11:30.087 AM.
Type: Timestamp
Required: Yes

 ** IamRoleArn **   <a name="Backup-Type-RestoreTestingSelectionForList-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: Yes

 ** ProtectedResourceType **   <a name="Backup-Type-RestoreTestingSelectionForList-ProtectedResourceType"></a>
The type of AWS resource included in a restore testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
Type: String
Required: Yes

 ** RestoreTestingPlanName **   <a name="Backup-Type-RestoreTestingSelectionForList-RestoreTestingPlanName"></a>
Unique string that is the name of the restore testing plan.
The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.
Type: String
Required: Yes

 ** RestoreTestingSelectionName **   <a name="Backup-Type-RestoreTestingSelectionForList-RestoreTestingSelectionName"></a>
Unique name of a restore testing selection.
The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String
Required: Yes

 ** ValidationWindowHours **   <a name="Backup-Type-RestoreTestingSelectionForList-ValidationWindowHours"></a>
This value represents the time, in hours, data is retained after a restore test so that optional validation can be completed.
Accepted value is an integer between 0 and 168 (the hourly equivalent of seven days).
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingSelectionForList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForList)
