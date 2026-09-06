---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupVaultDetails.html
---

# AwsBackupBackupVaultDetails
<a name="API_AwsBackupBackupVaultDetails"></a>

Provides details about an AWS Backup backup vault. In AWS Backup, a backup vault is a container that stores and organizes your backups.

## Contents
<a name="API_AwsBackupBackupVaultDetails_Contents"></a>

 ** AccessPolicy **   <a name="securityhub-Type-AwsBackupBackupVaultDetails-AccessPolicy"></a>
A resource-based policy that is used to manage access permissions on the target backup vault.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupVaultArn **   <a name="securityhub-Type-AwsBackupBackupVaultDetails-BackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupVaultName **   <a name="securityhub-Type-AwsBackupBackupVaultDetails-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the AWS account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionKeyArn **   <a name="securityhub-Type-AwsBackupBackupVaultDetails-EncryptionKeyArn"></a>
The unique ARN associated with the server-side encryption key. You can specify a key to encrypt your backups from services that support full AWS Backup management. If you don't specify a key, AWS Backup creates an AWS KMS key for you by default.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Notifications **   <a name="securityhub-Type-AwsBackupBackupVaultDetails-Notifications"></a>
The Amazon SNS event notifications for the specified backup vault.
Type: [AwsBackupBackupVaultNotificationsDetails](API_AwsBackupBackupVaultNotificationsDetails.md) object
Required: No

## See Also
<a name="API_AwsBackupBackupVaultDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupVaultDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupVaultDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupVaultDetails)
