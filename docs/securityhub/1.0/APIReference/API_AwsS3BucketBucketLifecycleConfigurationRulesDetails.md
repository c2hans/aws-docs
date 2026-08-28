---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketBucketLifecycleConfigurationRulesDetails.html
---

# AwsS3BucketBucketLifecycleConfigurationRulesDetails
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesDetails"></a>

Configuration for a lifecycle rule.

## Contents
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesDetails_Contents"></a>

 ** AbortIncompleteMultipartUpload **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-AbortIncompleteMultipartUpload"></a>
How Amazon S3 responds when a multipart upload is incomplete. Specifically, provides a number of days before Amazon S3 cancels the entire upload.
Type: [AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails.md) object
Required: No

 ** ExpirationDate **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-ExpirationDate"></a>
The date when objects are moved or deleted.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExpirationInDays **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-ExpirationInDays"></a>
The length in days of the lifetime for objects that are subject to the rule.
Type: Integer
Required: No

 ** ExpiredObjectDeleteMarker **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-ExpiredObjectDeleteMarker"></a>
Whether Amazon S3 removes a delete marker that has no noncurrent versions. If set to `true`, the delete marker is expired. If set to `false`, the policy takes no action.
If you provide `ExpiredObjectDeleteMarker`, you cannot provide `ExpirationInDays` or `ExpirationDate`.
Type: Boolean
Required: No

 ** Filter **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-Filter"></a>
Identifies the objects that a rule applies to.
Type: [AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails.md) object
Required: No

 ** ID **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-ID"></a>
The unique identifier of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NoncurrentVersionExpirationInDays **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-NoncurrentVersionExpirationInDays"></a>
The number of days that an object is noncurrent before Amazon S3 can perform the associated action.
Type: Integer
Required: No

 ** NoncurrentVersionTransitions **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-NoncurrentVersionTransitions"></a>
Transition rules that describe when noncurrent objects transition to a specified storage class.
Type: Array of [AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails.md) objects
Required: No

 ** Prefix **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-Prefix"></a>
A prefix that identifies one or more objects that the rule applies to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-Status"></a>
The current status of the rule. Indicates whether the rule is currently being applied.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Transitions **   <a name="securityhub-Type-AwsS3BucketBucketLifecycleConfigurationRulesDetails-Transitions"></a>
Transition rules that indicate when objects transition to a specified storage class.
Type: Array of [AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails](API_AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails.md) objects
Required: No

## See Also
<a name="API_AwsS3BucketBucketLifecycleConfigurationRulesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketBucketLifecycleConfigurationRulesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
