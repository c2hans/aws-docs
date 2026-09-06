---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VersioningConfiguration.html
---

# VersioningConfiguration
<a name="API_control_VersioningConfiguration"></a>

Describes the versioning state of an Amazon S3 on Outposts bucket. For more information, see [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html).

## Contents
<a name="API_control_VersioningConfiguration_Contents"></a>

 ** MFADelete **   <a name="AmazonS3-Type-control_VersioningConfiguration-MFADelete"></a>
Specifies whether MFA delete is enabled or disabled in the bucket versioning configuration for the S3 on Outposts bucket.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** Status **   <a name="AmazonS3-Type-control_VersioningConfiguration-Status"></a>
Sets the versioning state of the S3 on Outposts bucket.
Type: String
Valid Values: `Enabled | Suspended`
Required: No

## See Also
<a name="API_control_VersioningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/VersioningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/VersioningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/VersioningConfiguration)
