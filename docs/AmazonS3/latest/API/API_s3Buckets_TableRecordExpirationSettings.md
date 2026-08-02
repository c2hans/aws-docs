---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationSettings.html
---

# TableRecordExpirationSettings
<a name="API_s3Buckets_TableRecordExpirationSettings"></a>

The record expiration setting that specifies when records expire and are automatically removed from a table.

## Contents
<a name="API_s3Buckets_TableRecordExpirationSettings_Contents"></a>

 ** days **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationSettings-days"></a>
If you enable record expiration for a table, you can specify the number of days to retain your table records. For example, to retain your table records for one year, set this value to `365`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_s3Buckets_TableRecordExpirationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableRecordExpirationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableRecordExpirationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableRecordExpirationSettings)
