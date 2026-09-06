---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergUnreferencedFileRemovalSettings.html
---

# IcebergUnreferencedFileRemovalSettings
<a name="API_s3Buckets_IcebergUnreferencedFileRemovalSettings"></a>

Contains details about the unreferenced file removal settings for an Iceberg table bucket.

## Contents
<a name="API_s3Buckets_IcebergUnreferencedFileRemovalSettings_Contents"></a>

 ** nonCurrentDays **   <a name="AmazonS3-Type-s3Buckets_IcebergUnreferencedFileRemovalSettings-nonCurrentDays"></a>
The number of days an object has to be non-current before it is deleted.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** unreferencedDays **   <a name="AmazonS3-Type-s3Buckets_IcebergUnreferencedFileRemovalSettings-unreferencedDays"></a>
The number of days an object has to be unreferenced before it is marked as non-current.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_s3Buckets_IcebergUnreferencedFileRemovalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergUnreferencedFileRemovalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergUnreferencedFileRemovalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergUnreferencedFileRemovalSettings)
