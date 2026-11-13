---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQueryDefinitionSummary.html
---

# MetricDataQueryDefinitionSummary
<a name="API_MetricDataQueryDefinitionSummary"></a>

Summary information about a metric data query definition. To get the expression, call `GetMetricDataQueryDefinition`.

## Contents
<a name="API_MetricDataQueryDefinitionSummary_Contents"></a>

 ** Id **   <a name="ACW-Type-MetricDataQueryDefinitionSummary-Id"></a>
The ID of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** Path **   <a name="ACW-Type-MetricDataQueryDefinitionSummary-Path"></a>
The path of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{N}\p{P}\p{S}\p{Zs}]+`
Required: Yes

 ** Type **   <a name="ACW-Type-MetricDataQueryDefinitionSummary-Type"></a>
The language of the expression. Valid values are the following:
+  `PROMQL` – A PromQL query.
+  `SQL` – A CloudWatch Metrics Insights query.
+  `METRIC_MATH` – A metric math expression.
Type: String
Valid Values: `PROMQL | SQL | METRIC_MATH`
Required: Yes

 ** UpdatedAt **   <a name="ACW-Type-MetricDataQueryDefinitionSummary-UpdatedAt"></a>
The date and time when you last updated the metric data query definition.
Type: Timestamp
Required: No

## See Also
<a name="API_MetricDataQueryDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricDataQueryDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricDataQueryDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricDataQueryDefinitionSummary)
