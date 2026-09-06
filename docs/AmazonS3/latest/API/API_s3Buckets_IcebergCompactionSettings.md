---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergCompactionSettings.html
---

# IcebergCompactionSettings
<a name="API_s3Buckets_IcebergCompactionSettings"></a>

Contains details about the compaction settings for an Iceberg table.

## Contents
<a name="API_s3Buckets_IcebergCompactionSettings_Contents"></a>

 ** strategy **   <a name="AmazonS3-Type-s3Buckets_IcebergCompactionSettings-strategy"></a>
The compaction strategy to use for the table. This determines how files are selected and combined during compaction operations.
Type: String
Valid Values: `auto | binpack | sort | z-order`
Required: No

 ** targetFileSizeMB **   <a name="AmazonS3-Type-s3Buckets_IcebergCompactionSettings-targetFileSizeMB"></a>
The target file size for the table in MB.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_s3Buckets_IcebergCompactionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergCompactionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergCompactionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergCompactionSettings)
