---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails.html
---

# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails"></a>

A value to use for the filter.

## Contents
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails_Contents"></a>

 ** Prefix **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails-Prefix"></a>
Prefix text for matching objects.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Tag **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails-Tag"></a>
A tag that is assigned to matching objects.
Type: [AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails-Type"></a>
The type of filter value. Valid values are `LifecyclePrefixPredicate` or `LifecycleTagPredicate`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
