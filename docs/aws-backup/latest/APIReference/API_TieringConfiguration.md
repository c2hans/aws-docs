---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_TieringConfiguration.html
---

# TieringConfiguration
<a name="API_TieringConfiguration"></a>

This contains metadata about a tiering configuration.

## Contents
<a name="API_TieringConfiguration_Contents"></a>

 ** BackupVaultName **   <a name="Backup-Type-TieringConfiguration-BackupVaultName"></a>
The name of the backup vault where the tiering configuration applies. Use `*` to apply to all backup vaults.
Type: String
Pattern: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`
Required: Yes

 ** ResourceSelection **   <a name="Backup-Type-TieringConfiguration-ResourceSelection"></a>
An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.
Type: Array of [ResourceSelection](API_ResourceSelection.md) objects
Required: Yes

 ** TieringConfigurationName **   <a name="Backup-Type-TieringConfiguration-TieringConfigurationName"></a>
The unique name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.
Type: String
Pattern: `^[a-zA-Z0-9_]{1,200}$`
Required: Yes

 ** CreationTime **   <a name="Backup-Type-TieringConfiguration-CreationTime"></a>
The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp
Required: No

 ** CreatorRequestId **   <a name="Backup-Type-TieringConfiguration-CreatorRequestId"></a>
This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="Backup-Type-TieringConfiguration-LastUpdatedTime"></a>
The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdatedTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp
Required: No

 ** TieringConfigurationArn **   <a name="Backup-Type-TieringConfiguration-TieringConfigurationArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.
Type: String
Required: No

## See Also
<a name="API_TieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/TieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/TieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/TieringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
