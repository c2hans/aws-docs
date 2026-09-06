---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ManifestOutputLocation.html
---

# S3ManifestOutputLocation
<a name="API_control_S3ManifestOutputLocation"></a>

Location details for where the generated manifest should be written.

## Contents
<a name="API_control_S3ManifestOutputLocation_Contents"></a>

 ** Bucket **   <a name="AmazonS3-Type-control_S3ManifestOutputLocation-Bucket"></a>
The bucket ARN the generated manifest should be written to.
 **Directory buckets** - Directory buckets aren't supported as the buckets to store the generated manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[^:]+:s3:.*`
Required: Yes

 ** ManifestFormat **   <a name="AmazonS3-Type-control_S3ManifestOutputLocation-ManifestFormat"></a>
The format of the generated manifest.
Type: String
Valid Values: `S3InventoryReport_CSV_20211130`
Required: Yes

 ** ExpectedManifestBucketOwner **   <a name="AmazonS3-Type-control_S3ManifestOutputLocation-ExpectedManifestBucketOwner"></a>
The Account ID that owns the bucket the generated manifest is written to.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: No

 ** ManifestEncryption **   <a name="AmazonS3-Type-control_S3ManifestOutputLocation-ManifestEncryption"></a>
Specifies what encryption should be used when the generated manifest objects are written.
Type: [GeneratedManifestEncryption](API_control_GeneratedManifestEncryption.md) data type
Required: No

 ** ManifestPrefix **   <a name="AmazonS3-Type-control_S3ManifestOutputLocation-ManifestPrefix"></a>
Prefix identifying one or more objects to which the manifest applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_control_S3ManifestOutputLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ManifestOutputLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ManifestOutputLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ManifestOutputLocation)
