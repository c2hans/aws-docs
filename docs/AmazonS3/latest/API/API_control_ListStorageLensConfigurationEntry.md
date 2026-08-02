---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurationEntry.html
---

# ListStorageLensConfigurationEntry
<a name="API_control_ListStorageLensConfigurationEntry"></a>

Part of `ListStorageLensConfigurationResult`. Each entry includes the description of the S3 Storage Lens configuration, its home Region, whether it is enabled, its Amazon Resource Name (ARN), and config ID.

## Contents
<a name="API_control_ListStorageLensConfigurationEntry_Contents"></a>

 ** HomeRegion **   <a name="AmazonS3-Type-control_ListStorageLensConfigurationEntry-HomeRegion"></a>
A container for the S3 Storage Lens home Region. Your metrics data is stored and retained in your designated S3 Storage Lens home Region.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** Id **   <a name="AmazonS3-Type-control_ListStorageLensConfigurationEntry-Id"></a>
A container for the S3 Storage Lens configuration ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** StorageLensArn **   <a name="AmazonS3-Type-control_ListStorageLensConfigurationEntry-StorageLensArn"></a>
The ARN of the S3 Storage Lens configuration. This property is read-only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`
Required: Yes

 ** IsEnabled **   <a name="AmazonS3-Type-control_ListStorageLensConfigurationEntry-IsEnabled"></a>
A container for whether the S3 Storage Lens configuration is enabled. This property is required.
Type: Boolean
Required: No

## See Also
<a name="API_control_ListStorageLensConfigurationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListStorageLensConfigurationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListStorageLensConfigurationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListStorageLensConfigurationEntry)
