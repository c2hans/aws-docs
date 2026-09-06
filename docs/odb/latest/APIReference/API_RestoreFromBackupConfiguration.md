---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_RestoreFromBackupConfiguration.html
---

# RestoreFromBackupConfiguration
<a name="API_RestoreFromBackupConfiguration"></a>

The configuration for creating an Autonomous Database by restoring from a backup.

## Contents
<a name="API_RestoreFromBackupConfiguration_Contents"></a>

 ** autonomousDatabaseBackupId **   <a name="odb-Type-RestoreFromBackupConfiguration-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup to restore from.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** cloneType **   <a name="odb-Type-RestoreFromBackupConfiguration-cloneType"></a>
The type of clone to create from the backup.
Type: String
Valid Values: `FULL | METADATA | PARTIAL`
Required: Yes

 ** cloneTableSpaceList **   <a name="odb-Type-RestoreFromBackupConfiguration-cloneTableSpaceList"></a>
The list of tablespace identifiers to clone from the backup.
Type: Array of integers
Required: No

## See Also
<a name="API_RestoreFromBackupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/RestoreFromBackupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/RestoreFromBackupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/RestoreFromBackupConfiguration)
