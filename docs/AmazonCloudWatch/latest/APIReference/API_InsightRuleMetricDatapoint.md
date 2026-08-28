---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleMetricDatapoint.html
---

# InsightRuleMetricDatapoint
<a name="API_InsightRuleMetricDatapoint"></a>

One data point from the metric time series returned in a Contributor Insights rule report.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html).

## Contents
<a name="API_InsightRuleMetricDatapoint_Contents"></a>

 ** Timestamp **   <a name="ACW-Type-InsightRuleMetricDatapoint-Timestamp"></a>
The timestamp of the data point.
Type: Timestamp
Required: Yes

 ** Average **   <a name="ACW-Type-InsightRuleMetricDatapoint-Average"></a>
The average value from all contributors during the time period represented by that data point.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** MaxContributorValue **   <a name="ACW-Type-InsightRuleMetricDatapoint-MaxContributorValue"></a>
The maximum value provided by one contributor during this timestamp. Each timestamp is evaluated separately, so the identity of the max contributor could be different for each timestamp.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** Maximum **   <a name="ACW-Type-InsightRuleMetricDatapoint-Maximum"></a>
The maximum value from a single occurence from a single contributor during the time period represented by that data point.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** Minimum **   <a name="ACW-Type-InsightRuleMetricDatapoint-Minimum"></a>
The minimum value from a single contributor during the time period represented by that data point.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** SampleCount **   <a name="ACW-Type-InsightRuleMetricDatapoint-SampleCount"></a>
The number of occurrences that matched the rule during this data point.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** Sum **   <a name="ACW-Type-InsightRuleMetricDatapoint-Sum"></a>
The sum of the values from all contributors during the time period represented by that data point.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

 ** UniqueContributors **   <a name="ACW-Type-InsightRuleMetricDatapoint-UniqueContributors"></a>
The number of unique contributors who published data during this timestamp.
This statistic is returned only if you included it in the `Metrics` array in your request.
Type: Double
Required: No

## See Also
<a name="API_InsightRuleMetricDatapoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleMetricDatapoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleMetricDatapoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleMetricDatapoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
