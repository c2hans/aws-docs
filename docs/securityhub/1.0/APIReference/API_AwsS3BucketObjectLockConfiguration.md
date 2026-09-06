---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketObjectLockConfiguration.html
---

# AwsS3BucketObjectLockConfiguration
<a name="API_AwsS3BucketObjectLockConfiguration"></a>

 The container element for S3 Object Lock configuration parameters. In Amazon S3, Object Lock can help prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely.

## Contents
<a name="API_AwsS3BucketObjectLockConfiguration_Contents"></a>

 ** ObjectLockEnabled **   <a name="securityhub-Type-AwsS3BucketObjectLockConfiguration-ObjectLockEnabled"></a>
 Indicates whether the bucket has an Object Lock configuration enabled.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rule **   <a name="securityhub-Type-AwsS3BucketObjectLockConfiguration-Rule"></a>
 Specifies the Object Lock rule for the specified object.
Type: [AwsS3BucketObjectLockConfigurationRuleDetails](API_AwsS3BucketObjectLockConfigurationRuleDetails.md) object
Required: No

## See Also
<a name="API_AwsS3BucketObjectLockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketObjectLockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketObjectLockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketObjectLockConfiguration)
