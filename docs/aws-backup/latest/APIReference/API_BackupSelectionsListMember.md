---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupSelectionsListMember.html
---

# BackupSelectionsListMember
<a name="API_BackupSelectionsListMember"></a>

Contains metadata about a `BackupSelection` object.

## Contents
<a name="API_BackupSelectionsListMember_Contents"></a>

 ** BackupPlanId **   <a name="Backup-Type-BackupSelectionsListMember-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String
Required: No

 ** CreationDate **   <a name="Backup-Type-BackupSelectionsListMember-CreationDate"></a>
The date and time a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CreatorRequestId **   <a name="Backup-Type-BackupSelectionsListMember-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.
If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

 ** IamRoleArn **   <a name="Backup-Type-BackupSelectionsListMember-IamRoleArn"></a>
Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: No

 ** SelectionId **   <a name="Backup-Type-BackupSelectionsListMember-SelectionId"></a>
Uniquely identifies a request to assign a set of resources to a backup plan.
Type: String
Required: No

 ** SelectionName **   <a name="Backup-Type-BackupSelectionsListMember-SelectionName"></a>
The display name of a resource selection document.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

## See Also
<a name="API_BackupSelectionsListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupSelectionsListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupSelectionsListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupSelectionsListMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
