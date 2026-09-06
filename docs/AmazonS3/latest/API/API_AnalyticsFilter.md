---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsFilter.html
---

# AnalyticsFilter
<a name="API_AnalyticsFilter"></a>

The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.

## Contents
<a name="API_AnalyticsFilter_Contents"></a>

 ** And **   <a name="AmazonS3-Type-AnalyticsFilter-And"></a>
A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
Type: [AnalyticsAndOperator](API_AnalyticsAndOperator.md) data type
Required: No

 ** Prefix **   <a name="AmazonS3-Type-AnalyticsFilter-Prefix"></a>
The prefix to use when evaluating an analytics filter.
Type: String
Required: No

 ** Tag **   <a name="AmazonS3-Type-AnalyticsFilter-Tag"></a>
The tag to use when evaluating an analytics filter.
Type: [Tag](API_Tag.md) data type
Required: No

## See Also
<a name="API_AnalyticsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsFilter)
