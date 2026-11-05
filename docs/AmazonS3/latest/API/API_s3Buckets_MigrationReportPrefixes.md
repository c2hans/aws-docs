---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationReportPrefixes.html
---

# MigrationReportPrefixes
<a name="API_s3Buckets_MigrationReportPrefixes"></a>

The key prefix for each report. If you don't specify a prefix for a report, its keys start at the root of the bucket.

## Contents
<a name="API_s3Buckets_MigrationReportPrefixes_Contents"></a>

 ** objectCompatibilityReport **   <a name="AmazonS3-Type-s3Buckets_MigrationReportPrefixes-objectCompatibilityReport"></a>
The key prefix for the object compatibility report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** objectMigrationReport **   <a name="AmazonS3-Type-s3Buckets_MigrationReportPrefixes-objectMigrationReport"></a>
The key prefix for the object migration report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** tableCompatibilityReport **   <a name="AmazonS3-Type-s3Buckets_MigrationReportPrefixes-tableCompatibilityReport"></a>
The key prefix for the table compatibility report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_s3Buckets_MigrationReportPrefixes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationReportPrefixes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationReportPrefixes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationReportPrefixes)
