---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationCompactionSettings.html
---

# MigrationCompactionSettings
<a name="API_s3Buckets_MigrationCompactionSettings"></a>

The compaction settings that a migration applies to the destination table.

## Contents
<a name="API_s3Buckets_MigrationCompactionSettings_Contents"></a>

 ** strategy **   <a name="AmazonS3-Type-s3Buckets_MigrationCompactionSettings-strategy"></a>
The compaction strategy. The only valid value is `binpack`, which is the default.
Type: String
Valid Values: `auto | binpack | sort | z-order`
Required: No

 ** targetFileSizeMB **   <a name="AmazonS3-Type-s3Buckets_MigrationCompactionSettings-targetFileSizeMB"></a>
The target size, from 64 to 512 MB, of the data files that the migration writes, and of the files that compaction writes after you complete the migration. The default is 512.
Type: Integer
Valid Range: Minimum value of 64. Maximum value of 512.
Required: No

## See Also
<a name="API_s3Buckets_MigrationCompactionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationCompactionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationCompactionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationCompactionSettings)
