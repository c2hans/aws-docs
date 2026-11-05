---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationStats.html
---

# MigrationStats
<a name="API_s3Buckets_MigrationStats"></a>

The number of source objects that migrated, failed or are pending. For a sync, the counts cover every object of the table after the sync, including objects that earlier migrations migrated. The counts are set when planning finishes and updated when the migration ends.

## Contents
<a name="API_s3Buckets_MigrationStats_Contents"></a>

 ** objectsFailedMigration **   <a name="AmazonS3-Type-s3Buckets_MigrationStats-objectsFailedMigration"></a>
The number of source objects that didn't migrate, because they failed or because another object, such as an object in the same partition, failed. The object migration report lists the cause for each object.
Type: Long
Required: No

 ** objectsMigrated **   <a name="AmazonS3-Type-s3Buckets_MigrationStats-objectsMigrated"></a>
The number of source objects whose data the migration wrote to the destination table. Migrated data can be queried after the migration commits it. If the migration fails or is cancelled, some migrated objects might not be committed.
Type: Long
Required: No

 ** objectsPendingMigration **   <a name="AmazonS3-Type-s3Buckets_MigrationStats-objectsPendingMigration"></a>
The number of source objects that haven't migrated or failed yet. When a migration fails or is cancelled, these are the objects that it didn't migrate.
Type: Long
Required: No

## See Also
<a name="API_s3Buckets_MigrationStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationStats)
