---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DataMigrationOverview.html
---

# DataMigrationOverview
<a name="API_s3Buckets_DataMigrationOverview"></a>

The maintenance settings and migration policies for the destination table.

## Contents
<a name="API_s3Buckets_DataMigrationOverview_Contents"></a>

 ** maintenanceSettings **   <a name="AmazonS3-Type-s3Buckets_DataMigrationOverview-maintenanceSettings"></a>
The maintenance settings for the destination table. The migration applies them when it creates the table: snapshot management starts then, and compaction starts after you complete the migration. If you don't specify a setting, the migration uses its default: a target file size of 512 MB, the binpack compaction strategy, at least 3 snapshots, and a maximum snapshot age of 120 hours. Unreferenced file removal follows the table bucket's configuration after you complete the migration.
Type: [MaintenanceSettings](API_s3Buckets_MaintenanceSettings.md) object
Required: Yes

 ** migrationPolicies **   <a name="AmazonS3-Type-s3Buckets_DataMigrationOverview-migrationPolicies"></a>
The policies for source data that doesn't fit the destination schema.
Type: [MigrationPolicies](API_s3Buckets_MigrationPolicies.md) object
Required: Yes

## See Also
<a name="API_s3Buckets_DataMigrationOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DataMigrationOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DataMigrationOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DataMigrationOverview)
