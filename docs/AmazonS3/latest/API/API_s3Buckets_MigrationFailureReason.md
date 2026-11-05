---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationFailureReason.html
---

# MigrationFailureReason
<a name="API_s3Buckets_MigrationFailureReason"></a>

The reason that a migration failed: a code and, when there is one, the resource or reason it applies to. This value is returned only when the migration is in the `failed` state.

## Contents
<a name="API_s3Buckets_MigrationFailureReason_Contents"></a>

 ** code **   <a name="AmazonS3-Type-s3Buckets_MigrationFailureReason-code"></a>
The failure code. It names the cause or the report that lists the findings. Valid values:
+  `rolePermissions` - S3 Tables couldn't assume the migration role, or the role doesn't have a permission that the migration needs. `detail` is the role ARN.
+  `sourcePermissions` - The migration role couldn't read the AWS Glue table or the source objects. `detail` names the table (`database.table`) or the source bucket.
+  `destinationPermissions` - The migration role couldn't write to the table bucket or the report bucket. `detail` names the bucket.
+  `resourceNotFound` - A resource that you specified doesn't exist, such as the AWS Glue table or the source bucket. `detail` names it.
+  `sourceNotSupported` - The source table can't be migrated, for example because it is empty, has too many objects, or has columns or partitions that can't be migrated. The table compatibility report lists the findings.
+  `tableCompatibilityReport` - The migration couldn't create the destination table, for example because a table with that name already exists or the KMS key can't be used. For a sync, the destination table changed after the previous migration. The table compatibility report lists the finding.
+  `objectCompatibilityReport` - Some source objects can't be migrated, for example because they are archived, or because they were overwritten after an earlier migration migrated them. The object compatibility report lists them.
+  `objectMigrationReport` - Some source objects failed to migrate. The object migration report lists them and the cause for each.
+  `reportBucketNotSupported` - The report bucket can't receive the migration's reports, for example because it is in a different Region than the table bucket.
+  `internalError` - S3 Tables encountered an internal error. Retry the migration, and contact AWS Support if the error persists.
Type: String
Valid Values: `rolePermissions | sourcePermissions | destinationPermissions | resourceNotFound | sourceNotSupported | objectMigrationReport | objectCompatibilityReport | tableCompatibilityReport | internalError | reportBucketNotSupported`
Required: Yes

 ** detail **   <a name="AmazonS3-Type-s3Buckets_MigrationFailureReason-detail"></a>
The resource that the failure applies to, such as the role ARN, the AWS Glue table (`database.table`) or a bucket. For `sourceNotSupported`, the reason that the source isn't supported, such as `EMPTY_TABLE`. This value isn't returned for the report codes or for `internalError`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_s3Buckets_MigrationFailureReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationFailureReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationFailureReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationFailureReason)
