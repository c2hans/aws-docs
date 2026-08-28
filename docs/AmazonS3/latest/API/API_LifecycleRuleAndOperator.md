---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleRuleAndOperator.html
---

# LifecycleRuleAndOperator
<a name="API_LifecycleRuleAndOperator"></a>

This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.

## Contents
<a name="API_LifecycleRuleAndOperator_Contents"></a>

 ** ObjectSizeGreaterThan **   <a name="AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan"></a>
Minimum object size to which the rule applies.
Type: Long
Required: No

 ** ObjectSizeLessThan **   <a name="AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan"></a>
Maximum object size to which the rule applies.
Type: Long
Required: No

 ** Prefix **   <a name="AmazonS3-Type-LifecycleRuleAndOperator-Prefix"></a>
Prefix identifying one or more objects to which the rule applies.
Type: String
Required: No

 ** Tags **   <a name="AmazonS3-Type-LifecycleRuleAndOperator-Tags"></a>
All of these tags must exist in the object's tag set in order for the rule to apply.
Type: Array of [Tag](API_Tag.md) data types
Required: No

## See Also
<a name="API_LifecycleRuleAndOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleRuleAndOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleRuleAndOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleRuleAndOperator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
