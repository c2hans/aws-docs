---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-logicallyairgappedbackupvault.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::LogicallyAirGappedBackupVault
<a name="aws-resource-backup-logicallyairgappedbackupvault"></a>

Creates a logical container to where backups may be copied.

This request includes a name, the Region, the maximum number of retention days, the minimum number of retention days, and optionally can include tags and a creator request ID.

**Note**
Do not include sensitive data, such as passport numbers, in the name of a backup vault.

## Syntax
<a name="aws-resource-backup-logicallyairgappedbackupvault-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-logicallyairgappedbackupvault-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::LogicallyAirGappedBackupVault",
  "Properties" : {
      "[AccessPolicy](#cfn-backup-logicallyairgappedbackupvault-accesspolicy)" : {{Json}},
      "[BackupVaultName](#cfn-backup-logicallyairgappedbackupvault-backupvaultname)" : {{String}},
      "[BackupVaultTags](#cfn-backup-logicallyairgappedbackupvault-backupvaulttags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[EncryptionKeyArn](#cfn-backup-logicallyairgappedbackupvault-encryptionkeyarn)" : {{String}},
      "[MaxRetentionDays](#cfn-backup-logicallyairgappedbackupvault-maxretentiondays)" : {{Integer}},
      "[MinRetentionDays](#cfn-backup-logicallyairgappedbackupvault-minretentiondays)" : {{Integer}},
      "[MpaApprovalTeamArn](#cfn-backup-logicallyairgappedbackupvault-mpaapprovalteamarn)" : {{String}},
      "[Notifications](#cfn-backup-logicallyairgappedbackupvault-notifications)" : {{NotificationObjectType}}
    }
}
```

### YAML
<a name="aws-resource-backup-logicallyairgappedbackupvault-syntax.yaml"></a>

```
Type: AWS::Backup::LogicallyAirGappedBackupVault
Properties:
  [AccessPolicy](#cfn-backup-logicallyairgappedbackupvault-accesspolicy): {{Json}}
  [BackupVaultName](#cfn-backup-logicallyairgappedbackupvault-backupvaultname): {{String}}
  [BackupVaultTags](#cfn-backup-logicallyairgappedbackupvault-backupvaulttags): {{
    {{Key}}: {{Value}}}}
  [EncryptionKeyArn](#cfn-backup-logicallyairgappedbackupvault-encryptionkeyarn): {{String}}
  [MaxRetentionDays](#cfn-backup-logicallyairgappedbackupvault-maxretentiondays): {{Integer}}
  [MinRetentionDays](#cfn-backup-logicallyairgappedbackupvault-minretentiondays): {{Integer}}
  [MpaApprovalTeamArn](#cfn-backup-logicallyairgappedbackupvault-mpaapprovalteamarn): {{String}}
  [Notifications](#cfn-backup-logicallyairgappedbackupvault-notifications): {{
    NotificationObjectType}}
```

## Properties
<a name="aws-resource-backup-logicallyairgappedbackupvault-properties"></a>

`AccessPolicy`  <a name="cfn-backup-logicallyairgappedbackupvault-accesspolicy"></a>
The backup vault access policy document in JSON format.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BackupVaultName`  <a name="cfn-backup-logicallyairgappedbackupvault-backupvaultname"></a>
The name of a logical container where backups are stored. Logically air-gapped backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_]{2,50}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BackupVaultTags`  <a name="cfn-backup-logicallyairgappedbackupvault-backupvaulttags"></a>
The tags to assign to the vault.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyArn`  <a name="cfn-backup-logicallyairgappedbackupvault-encryptionkeyarn"></a>
The server-side encryption key that is used to protect your backups; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
If this field is left blank, AWS Backup will create an AWS owned key to be used to encrypt the content of the logically air-gapped vault. The ARN of this created key will be available as `Fn::GetAtt` output.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxRetentionDays`  <a name="cfn-backup-logicallyairgappedbackupvault-maxretentiondays"></a>
The maximum retention period that the vault retains its recovery points.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinRetentionDays`  <a name="cfn-backup-logicallyairgappedbackupvault-minretentiondays"></a>
This setting specifies the minimum retention period that the vault retains its recovery points.
The minimum value accepted is 7 days.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MpaApprovalTeamArn`  <a name="cfn-backup-logicallyairgappedbackupvault-mpaapprovalteamarn"></a>
The Amazon Resource Name (ARN) of the MPA approval team to associate with the backup vault. This cannot be changed after it is set from the CloudFormation template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notifications`  <a name="cfn-backup-logicallyairgappedbackupvault-notifications"></a>
Returns event notifications for the specified backup vault.
*Required*: No
*Type*: [NotificationObjectType](aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-backup-logicallyairgappedbackupvault-return-values"></a>

### Ref
<a name="aws-resource-backup-logicallyairgappedbackupvault-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the backup vault.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-backup-logicallyairgappedbackupvault-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-backup-logicallyairgappedbackupvault-return-values-fn--getatt-fn--getatt"></a>

`BackupVaultArn`  <a name="BackupVaultArn-fn::getatt"></a>
The ARN of the backup vault.

`VaultState`  <a name="VaultState-fn::getatt"></a>
The vault state. The possible values are `CREATING`, `AVAILABLE`, and `FAILED`.

`VaultType`  <a name="VaultType-fn::getatt"></a>
The vault type. The possible values are `BACKUP_VAULT` and `LOGICALLY_AIR_GAPPED_BACKUP_VAULT`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
