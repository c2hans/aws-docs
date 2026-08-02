---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketVersioningConfiguration.html
---

# AwsS3BucketBucketVersioningConfiguration
<a name="API_AwsS3BucketBucketVersioningConfiguration"></a>

Describes the versioning state of an S3 bucket.

## Contents
<a name="API_AwsS3BucketBucketVersioningConfiguration_Contents"></a>

 ** IsMfaDeleteEnabled **   <a name="securityhub-Type-AwsS3BucketBucketVersioningConfiguration-IsMfaDeleteEnabled"></a>
Specifies whether MFA delete is currently enabled in the S3 bucket versioning configuration. If the S3 bucket was never configured with MFA delete, then this attribute is not included.
Type: Boolean
Required: No

 ** Status **   <a name="securityhub-Type-AwsS3BucketBucketVersioningConfiguration-Status"></a>
The versioning status of the S3 bucket. Valid values are `Enabled` or `Suspended`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketBucketVersioningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketVersioningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketVersioningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketVersioningConfiguration)
