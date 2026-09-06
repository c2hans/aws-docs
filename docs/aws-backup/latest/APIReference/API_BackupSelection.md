---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupSelection.html
---

# BackupSelection
<a name="API_BackupSelection"></a>

Used to specify a set of resources to a backup plan.

We recommend that you specify conditions, tags, or resources to include or exclude. Otherwise, Backup attempts to select all supported and opted-in storage resources, which could have unintended cost implications.

For more information, see [Assigning resources programmatically](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json).

## Contents
<a name="API_BackupSelection_Contents"></a>

 ** IamRoleArn **   <a name="Backup-Type-BackupSelection-IamRoleArn"></a>
The ARN of the IAM role that AWS Backup uses to authenticate when backing up the target resource; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: Yes

 ** SelectionName **   <a name="Backup-Type-BackupSelection-SelectionName"></a>
The display name of a resource selection document. Must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: Yes

 ** Conditions **   <a name="Backup-Type-BackupSelection-Conditions"></a>
The conditions that you define to assign resources to your backup plans using tags. For example, `"StringEquals": { "ConditionKey": "aws:ResourceTag/backup", "ConditionValue": "daily" }`.
 `Conditions` supports `StringEquals`, `StringLike`, `StringNotEquals`, and `StringNotLike`. Condition operators are case sensitive.
If you specify multiple conditions, the resources much match all conditions (AND logic).
Type: [Conditions](API_Conditions.md) object
Required: No

 ** ListOfTags **   <a name="Backup-Type-BackupSelection-ListOfTags"></a>
We recommend that you use the `Conditions` parameter instead of this parameter.
The conditions that you define to assign resources to your backup plans using tags. For example, `"StringEquals": { "ConditionKey": "backup", "ConditionValue": "daily"}`.
 `ListOfTags` supports only `StringEquals`. Condition operators are case sensitive.
If you specify multiple conditions, the resources much match any of the conditions (OR logic).
Type: Array of [Condition](API_Condition.md) objects
Required: No

 ** NotResources **   <a name="Backup-Type-BackupSelection-NotResources"></a>
The Amazon Resource Names (ARNs) of the resources to exclude from a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.
If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.
Type: Array of strings
Required: No

 ** Resources **   <a name="Backup-Type-BackupSelection-Resources"></a>
The Amazon Resource Names (ARNs) of the resources to assign to a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.
If you need to assign many resources to a backup plan, consider a different resource selection strategy, such as assigning all resources of a resource type or refining your resource selection using tags.
If you specify multiple ARNs, the resources much match any of the ARNs (OR logic).
When using wildcards in ARN patterns for backup selections, the asterisk (\*) must appear at the end of the ARN string (prefix pattern). For example, `arn:aws:s3:::my-bucket-*` is valid, but `arn:aws:s3:::*-logs` is not supported.
Type: Array of strings
Required: No

## See Also
<a name="API_BackupSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupSelection)
