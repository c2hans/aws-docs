---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensExpandedPrefixesDataExport.html
---

# StorageLensExpandedPrefixesDataExport
<a name="API_control_StorageLensExpandedPrefixesDataExport"></a>

A container for your S3 Storage Lens expanded prefix metrics report configuration. Unlike the default Storage Lens metrics report, the enhanced prefix metrics report includes all S3 Storage Lens storage and activity data related to the full list of prefixes in your Storage Lens configuration.

## Contents
<a name="API_control_StorageLensExpandedPrefixesDataExport_Contents"></a>

 ** S3BucketDestination **   <a name="AmazonS3-Type-control_StorageLensExpandedPrefixesDataExport-S3BucketDestination"></a>
A container for the bucket where the Amazon S3 Storage Lens metrics export files are located.
Type: [S3BucketDestination](API_control_S3BucketDestination.md) data type
Required: No

 ** StorageLensTableDestination **   <a name="AmazonS3-Type-control_StorageLensExpandedPrefixesDataExport-StorageLensTableDestination"></a>
A container for the bucket where the S3 Storage Lens metric export files are located. At least one export destination must be specified.
Type: [StorageLensTableDestination](API_control_StorageLensTableDestination.md) data type
Required: No

## See Also
<a name="API_control_StorageLensExpandedPrefixesDataExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensExpandedPrefixesDataExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensExpandedPrefixesDataExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensExpandedPrefixesDataExport)
