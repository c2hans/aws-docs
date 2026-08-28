---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_TieringConfigurationsListMember.html
---

# TieringConfigurationsListMember
<a name="API_TieringConfigurationsListMember"></a>

This contains metadata about a tiering configuration returned in a list.

## Contents
<a name="API_TieringConfigurationsListMember_Contents"></a>

 ** BackupVaultName **   <a name="Backup-Type-TieringConfigurationsListMember-BackupVaultName"></a>
The name of the backup vault where the tiering configuration applies. Use `*` to apply to all backup vaults.
Type: String
Pattern: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`
Required: No

 ** CreationTime **   <a name="Backup-Type-TieringConfigurationsListMember-CreationTime"></a>
The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="Backup-Type-TieringConfigurationsListMember-LastUpdatedTime"></a>
The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdatedTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp
Required: No

 ** TieringConfigurationArn **   <a name="Backup-Type-TieringConfigurationsListMember-TieringConfigurationArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.
Type: String
Required: No

 ** TieringConfigurationName **   <a name="Backup-Type-TieringConfigurationsListMember-TieringConfigurationName"></a>
The unique name of the tiering configuration.
Type: String
Pattern: `^[a-zA-Z0-9_]{1,200}$`
Required: No

## See Also
<a name="API_TieringConfigurationsListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/TieringConfigurationsListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationsListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationsListMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
