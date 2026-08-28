---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails.html
---

# AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails"></a>

A rule for when objects transition to specific storage classes.

## Contents
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails_Contents"></a>

 ** Date **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails-Date"></a>
A date on which to transition objects to the specified storage class. If you provide `Date`, you cannot provide `Days`.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Days **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails-Days"></a>
The number of days after which to transition the object to the specified storage class. If you provide `Days`, you cannot provide `Date`.
Type: Integer
Required: No

 ** StorageClass **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails-StorageClass"></a>
The storage class to transition the object to. Valid values are as follows:
+  `DEEP_ARCHIVE`
+  `GLACIER`
+  `INTELLIGENT_TIERING`
+  `ONEZONE_IA`
+  `STANDARD_IA`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
