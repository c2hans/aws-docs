---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StatisticAnnotation.html
---

# StatisticAnnotation
<a name="API_StatisticAnnotation"></a>

A Statistic Annotation.

## Contents
<a name="API_StatisticAnnotation_Contents"></a>

 ** InclusionAnnotation **   <a name="Glue-Type-StatisticAnnotation-InclusionAnnotation"></a>
The inclusion annotation applied to the statistic.
Type: [TimestampedInclusionAnnotation](API_TimestampedInclusionAnnotation.md) object
Required: No

 ** ProfileId **   <a name="Glue-Type-StatisticAnnotation-ProfileId"></a>
The Profile ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatisticId **   <a name="Glue-Type-StatisticAnnotation-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatisticRecordedOn **   <a name="Glue-Type-StatisticAnnotation-StatisticRecordedOn"></a>
The timestamp when the annotated statistic was recorded.
Type: Timestamp
Required: No

## See Also
<a name="API_StatisticAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StatisticAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StatisticAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StatisticAnnotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
