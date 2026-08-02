---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails.html
---

# AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails
<a name="API_AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails"></a>

 The default S3 Object Lock retention mode and period that you want to apply to new objects placed in the specified Amazon S3 bucket.

## Contents
<a name="API_AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails_Contents"></a>

 ** Days **   <a name="securityhub-Type-AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails-Days"></a>
 The number of days that you want to specify for the default retention period.
Type: Integer
Required: No

 ** Mode **   <a name="securityhub-Type-AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails-Mode"></a>
 The default Object Lock retention mode you want to apply to new objects placed in the specified bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Years **   <a name="securityhub-Type-AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails-Years"></a>
 The number of years that you want to specify for the default retention period.
Type: Integer
Required: No

## See Also
<a name="API_AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails)
