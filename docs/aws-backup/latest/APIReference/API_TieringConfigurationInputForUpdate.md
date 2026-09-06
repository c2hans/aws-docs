---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_TieringConfigurationInputForUpdate.html
---

# TieringConfigurationInputForUpdate
<a name="API_TieringConfigurationInputForUpdate"></a>

This contains metadata about a tiering configuration for update operations.

## Contents
<a name="API_TieringConfigurationInputForUpdate_Contents"></a>

 ** BackupVaultName **   <a name="Backup-Type-TieringConfigurationInputForUpdate-BackupVaultName"></a>
The name of the backup vault where the tiering configuration applies. Use `*` to apply to all backup vaults.
Type: String
Pattern: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`
Required: Yes

 ** ResourceSelection **   <a name="Backup-Type-TieringConfigurationInputForUpdate-ResourceSelection"></a>
An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.
Type: Array of [ResourceSelection](API_ResourceSelection.md) objects
Required: Yes

## See Also
<a name="API_TieringConfigurationInputForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/TieringConfigurationInputForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/TieringConfigurationInputForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/TieringConfigurationInputForUpdate)
