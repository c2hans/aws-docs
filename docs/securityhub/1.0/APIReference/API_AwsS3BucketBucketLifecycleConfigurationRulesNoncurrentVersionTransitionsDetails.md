---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails.html
---

# AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails"></a>

A transition rule that describes when noncurrent objects transition to a specified storage class.

## Contents
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails_Contents"></a>

 ** Days **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails-Days"></a>
The number of days that an object is noncurrent before Amazon S3 can perform the associated action.
Type: Integer
Required: No

 ** StorageClass **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails-StorageClass"></a>
The class of storage to change the object to after the object is noncurrent for the specified number of days.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails)
