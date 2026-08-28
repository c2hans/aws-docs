---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MetricBasedObservation.html
---

# MetricBasedObservation
<a name="API_MetricBasedObservation"></a>

Describes the metric based observation generated based on evaluated data quality metrics.

## Contents
<a name="API_MetricBasedObservation_Contents"></a>

 ** MetricName **   <a name="Glue-Type-MetricBasedObservation-MetricName"></a>
The name of the data quality metric used for generating the observation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** MetricValues **   <a name="Glue-Type-MetricBasedObservation-MetricValues"></a>
An object of type `DataQualityMetricValues` representing the analysis of the data quality metric value.
Type: [DataQualityMetricValues](API_DataQualityMetricValues.md) object
Required: No

 ** NewRules **   <a name="Glue-Type-MetricBasedObservation-NewRules"></a>
A list of new data quality rules generated as part of the observation based on the data quality metric value.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatisticId **   <a name="Glue-Type-MetricBasedObservation-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_MetricBasedObservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MetricBasedObservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MetricBasedObservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MetricBasedObservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
