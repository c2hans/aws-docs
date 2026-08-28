---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MonitoredRequestCountMetricDataQueries.html
---

# MonitoredRequestCountMetricDataQueries
<a name="API_MonitoredRequestCountMetricDataQueries"></a>

This structure defines the metric that is used as the "good request" or "bad request" value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` is divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.

## Contents
<a name="API_MonitoredRequestCountMetricDataQueries_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BadCountMetric **   <a name="applicationsignals-Type-MonitoredRequestCountMetricDataQueries-BadCountMetric"></a>
If you want to count "bad requests" to determine the percentage of successful requests for this request-based SLO, specify the metric to use as "bad requests" in this structure.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

 ** GoodCountMetric **   <a name="applicationsignals-Type-MonitoredRequestCountMetricDataQueries-GoodCountMetric"></a>
If you want to count "good requests" to determine the percentage of successful requests for this request-based SLO, specify the metric to use as "good requests" in this structure.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

## See Also
<a name="API_MonitoredRequestCountMetricDataQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MonitoredRequestCountMetricDataQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MonitoredRequestCountMetricDataQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MonitoredRequestCountMetricDataQueries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
