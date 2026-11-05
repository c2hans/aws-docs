---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationOutputConfiguration.html
---

# MigrationOutputConfiguration
<a name="API_s3Buckets_MigrationOutputConfiguration"></a>

The bucket and prefixes that a migration writes its reports to. Every report goes to one bucket, each under its own prefix.

## Contents
<a name="API_s3Buckets_MigrationOutputConfiguration_Contents"></a>

 ** bucket **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputConfiguration-bucket"></a>
The general purpose bucket that the migration writes every report to.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1024.
Pattern: `arn:aws[-a-z0-9]*:s3[a-z]*:[-a-z0-9]*:([0-9]{12})?:.+`
Required: Yes

 ** prefixes **   <a name="AmazonS3-Type-s3Buckets_MigrationOutputConfiguration-prefixes"></a>
The key prefix for each report.
Type: [MigrationReportPrefixes](API_s3Buckets_MigrationReportPrefixes.md) object
Required: No

## See Also
<a name="API_s3Buckets_MigrationOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationOutputConfiguration)
