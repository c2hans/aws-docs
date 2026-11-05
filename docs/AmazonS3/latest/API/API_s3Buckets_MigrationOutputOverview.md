---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationOutputOverview.html
---

# MigrationOutputOverview
<a name="API_s3Buckets_MigrationOutputOverview"></a>

Where a migration writes its reports, and the location of each report once it is written.

## Contents
<a name="API_s3Buckets_MigrationOutputOverview_Contents"></a>

 ** bucket **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputOverview-bucket"></a>
The general purpose bucket that the migration writes every report to.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1024.
Pattern: `arn:aws[-a-z0-9]*:s3[a-z]*:[-a-z0-9]*:([0-9]{12})?:.+`
Required: Yes

 ** objectCompatibilityReport **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputOverview-objectCompatibilityReport"></a>
The object compatibility report: one row for each source object under the source table's location, with whether the migration includes the object and its most severe finding. The migration writes it when planning finishes. If planning fails, the report might not be written.
Type: [ReportOverview](API_s3Buckets_ReportOverview.md) object
Required: Yes

 ** objectMigrationReport **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputOverview-objectMigrationReport"></a>
The object migration report: one row for each source object that the migration tried to migrate, with whether it migrated, how it was transformed, and why it failed. The migration writes it once, when the migration ends. It isn't written if planning fails or if a sync has nothing to migrate.
Type: [ReportOverview](API_s3Buckets_ReportOverview.md) object
Required: Yes

 ** tableCompatibilityReport **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputOverview-tableCompatibilityReport"></a>
The table compatibility report: the sample object that the schema is inferred from, the table-level findings, and one row for each destination column with its type change and how the migration policies apply to it. The migration writes it when planning finishes, before any data migrates. If planning fails, the report might not be written.
Type: [ReportOverview](API_s3Buckets_ReportOverview.md) object
Required: Yes

## See Also
<a name="API_s3Buckets_MigrationOutputOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationOutputOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationOutputOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationOutputOverview)
