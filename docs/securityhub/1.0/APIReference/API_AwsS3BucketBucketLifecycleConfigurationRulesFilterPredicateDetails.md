---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails.html
---

# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails"></a>

The configuration for the filter.

## Contents
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails_Contents"></a>

 ** Operands **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails-Operands"></a>
The values to use for the filter.
Type: Array of [AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails.md) objects
Required: No

 ** Prefix **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails-Prefix"></a>
A prefix filter.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Tag **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails-Tag"></a>
A tag filter.
Type: [AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails-Type"></a>
Whether to use `AND` or `OR` to join the operands. Valid values are `LifecycleAndOperator` or `LifecycleOrOperator`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails)
