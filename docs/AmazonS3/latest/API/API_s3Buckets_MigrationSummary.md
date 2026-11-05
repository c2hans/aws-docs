---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationSummary.html
---

# MigrationSummary
<a name="API_s3Buckets_MigrationSummary"></a>

A summary of a migration.

## Contents
<a name="API_s3Buckets_MigrationSummary_Contents"></a>

 ** createdAt **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-createdAt"></a>
The date and time that the migration was created.
Type: Timestamp
Required: Yes

 ** migrationId **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-migrationId"></a>
The ID of the migration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** name **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-name"></a>
The name of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** namespace **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-namespace"></a>
The namespace of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** state **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-state"></a>
The state of the migration. Valid values:
+  `new` - S3 Tables accepted the request.
+  `planning` - The migration is checking the source table, its objects and the destination for compatibility, and writing the compatibility reports.
+  `pendingReview` - Planning finished, and the migration waits for you to continue or cancel it with `UpdateTableMigration`.
+  `queued` - The migration is waiting to start migrating data.
+  `migrating` - The migration is running the plan from the `planning` state: it copies data and commits it to the destination table. A migration reaches this state only if `hasValidPlan` is `true`.
+  `succeeded` - Every planned object migrated.
+  `failed` - The migration failed. Check `failureReason` for the cause.
+  `cancelling` - You cancelled the migration, and it is finishing the work in progress.
+  `cancelled` - The migration is cancelled.
Type: String
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`
Required: Yes

 ** stateUpdatedAt **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-stateUpdatedAt"></a>
The date and time that the migration's state last changed.
Type: Timestamp
Required: Yes

 ** tableBucketARN **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket that contains the destination table.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** type **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-type"></a>
The type of the migration. Valid values:
+  `start` - A migration that `StartTableMigration` started.
+  `sync` - A migration that `SyncTableMigration` started.
Type: String
Valid Values: `start | sync`
Required: Yes

 ** hasValidPlan **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-hasValidPlan"></a>
A Boolean value that specifies whether planning produced a plan that the migration can run. If planning hasn't finished, this value isn't returned.
Type: Boolean
Required: No

 ** tableARN **   <a name="AmazonS3-Type-s3Buckets_MigrationSummary-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table, once the migration creates it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: No

## See Also
<a name="API_s3Buckets_MigrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationSummary)
