---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsAndOperator.html
---

# AnalyticsAndOperator
<a name="API_AnalyticsAndOperator"></a>

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates in any combination, and an object must match all of the predicates for the filter to apply.

## Contents
<a name="API_AnalyticsAndOperator_Contents"></a>

 ** Prefix **   <a name="AmazonS3-Type-AnalyticsAndOperator-Prefix"></a>
The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.
Type: String
Required: No

 ** Tags **   <a name="AmazonS3-Type-AnalyticsAndOperator-Tags"></a>
The list of tags to use when evaluating an AND predicate.
Type: Array of [Tag](API_Tag.md) data types
Required: No

## See Also
<a name="API_AnalyticsAndOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsAndOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsAndOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsAndOperator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
