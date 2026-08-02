---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_S3StorageOptions.html
---

# S3StorageOptions
<a name="API_S3StorageOptions"></a>

The Amazon S3 storage options that are configured for your server.

## Contents
<a name="API_S3StorageOptions_Contents"></a>

 ** DirectoryListingOptimization **   <a name="TransferFamily-Type-S3StorageOptions-DirectoryListingOptimization"></a>
Specifies whether or not performance for your Amazon S3 directories is optimized.
+ If using the console, this is enabled by default.
+ If using the API or CLI, this is disabled by default.
By default, home directory mappings have a `TYPE` of `DIRECTORY`. If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry` `Type` to `FILE` if you want a mapping to have a file target.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_S3StorageOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/S3StorageOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/S3StorageOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/S3StorageOptions)
