---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DatapointInclusionAnnotation.html
---

# DatapointInclusionAnnotation
<a name="API_DatapointInclusionAnnotation"></a>

An Inclusion Annotation.

## Contents
<a name="API_DatapointInclusionAnnotation_Contents"></a>

 ** InclusionAnnotation **   <a name="Glue-Type-DatapointInclusionAnnotation-InclusionAnnotation"></a>
The inclusion annotation value to apply to the statistic.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: No

 ** ProfileId **   <a name="Glue-Type-DatapointInclusionAnnotation-ProfileId"></a>
The ID of the data quality profile the statistic belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatisticId **   <a name="Glue-Type-DatapointInclusionAnnotation-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DatapointInclusionAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DatapointInclusionAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DatapointInclusionAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DatapointInclusionAnnotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
