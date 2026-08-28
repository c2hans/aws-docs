---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsFilter.html
---

# MetricsFilter
<a name="API_MetricsFilter"></a>

Specifies a metrics configuration filter. The metrics configuration only includes objects that meet the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction (MetricsAndOperator). For more information, see [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html).

## Contents
<a name="API_MetricsFilter_Contents"></a>

 ** AccessPointArn **   <a name="AmazonS3-Type-MetricsFilter-AccessPointArn"></a>
The access point ARN used when evaluating a metrics filter.
Type: String
Required: No

 ** And **   <a name="AmazonS3-Type-MetricsFilter-And"></a>
A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
Type: [MetricsAndOperator](API_MetricsAndOperator.md) data type
Required: No

 ** Prefix **   <a name="AmazonS3-Type-MetricsFilter-Prefix"></a>
The prefix used when evaluating a metrics filter.
Type: String
Required: No

 ** Tag **   <a name="AmazonS3-Type-MetricsFilter-Tag"></a>
The tag used when evaluating a metrics filter.
 `Tag` filters are not supported for directory buckets.
Type: [Tag](API_Tag.md) data type
Required: No

## See Also
<a name="API_MetricsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetricsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetricsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetricsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
