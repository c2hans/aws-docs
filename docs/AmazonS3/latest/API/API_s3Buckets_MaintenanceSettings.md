---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MaintenanceSettings.html
---

# MaintenanceSettings
<a name="API_s3Buckets_MaintenanceSettings"></a>

The maintenance settings for the destination table. The migration applies them when it creates the table: snapshot management starts then, and compaction starts after you complete the migration. If you don't specify a setting, the migration uses its default: a target file size of 512 MB, the binpack compaction strategy, at least 3 snapshots, and a maximum snapshot age of 120 hours. Unreferenced file removal follows the table bucket's configuration after you complete the migration.

## Contents
<a name="API_s3Buckets_MaintenanceSettings_Contents"></a>

 ** icebergCompaction **   <a name="AmazonS3-Type-s3Buckets_MaintenanceSettings-icebergCompaction"></a>
The compaction settings.
Type: [MigrationCompactionSettings](API_s3Buckets_MigrationCompactionSettings.md) object
Required: No

 ** icebergSnapshotManagement **   <a name="AmazonS3-Type-s3Buckets_MaintenanceSettings-icebergSnapshotManagement"></a>
The snapshot management settings.
Type: [MigrationSnapshotManagementSettings](API_s3Buckets_MigrationSnapshotManagementSettings.md) object
Required: No

## See Also
<a name="API_s3Buckets_MaintenanceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MaintenanceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MaintenanceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MaintenanceSettings)
