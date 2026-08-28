---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleRuleFilter.html
---

# LifecycleRuleFilter
<a name="API_control_LifecycleRuleFilter"></a>

The container for the filter of the lifecycle rule.

## Contents
<a name="API_control_LifecycleRuleFilter_Contents"></a>

 ** And **   <a name="AmazonS3-Type-control_LifecycleRuleFilter-And"></a>
The container for the `AND` condition for the lifecycle rule.
Type: [LifecycleRuleAndOperator](API_control_LifecycleRuleAndOperator.md) data type
Required: No

 ** ObjectSizeGreaterThan **   <a name="AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan"></a>
Minimum object size to which the rule applies.
Type: Long
Required: No

 ** ObjectSizeLessThan **   <a name="AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan"></a>
Maximum object size to which the rule applies.
Type: Long
Required: No

 ** Prefix **   <a name="AmazonS3-Type-control_LifecycleRuleFilter-Prefix"></a>
Prefix identifying one or more objects to which the rule applies.
When you're using XML requests, you must replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. For more information, see [ XML-related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) in the *Amazon S3 User Guide*.
Type: String
Required: No

 ** Tag **   <a name="AmazonS3-Type-control_LifecycleRuleFilter-Tag"></a>
A container for a key-value name pair.
Type: [S3Tag](API_control_S3Tag.md) data type
Required: No

## See Also
<a name="API_control_LifecycleRuleFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleRuleFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleRuleFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleRuleFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
