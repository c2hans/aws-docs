---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsAndOperator.html
---

# MetricsAndOperator
<a name="API_MetricsAndOperator"></a>

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.

## Contents
<a name="API_MetricsAndOperator_Contents"></a>

 ** AccessPointArn **   <a name="AmazonS3-Type-MetricsAndOperator-AccessPointArn"></a>
The access point ARN used when evaluating an `AND` predicate.
Type: String
Required: No

 ** Prefix **   <a name="AmazonS3-Type-MetricsAndOperator-Prefix"></a>
The prefix used when evaluating an AND predicate.
Type: String
Required: No

 ** Tags **   <a name="AmazonS3-Type-MetricsAndOperator-Tags"></a>
The list of tags used when evaluating an AND predicate.
 `Tag` filters are not supported for directory buckets.
Type: Array of [Tag](API_Tag.md) data types
Required: No

## See Also
<a name="API_MetricsAndOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetricsAndOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetricsAndOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetricsAndOperator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
