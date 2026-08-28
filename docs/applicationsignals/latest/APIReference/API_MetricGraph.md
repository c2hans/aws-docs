---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricGraph.html
---

# MetricGraph
<a name="API_MetricGraph"></a>

A structure that contains metric data queries and time range information that provides context for audit findings through relevant performance metrics.

## Contents
<a name="API_MetricGraph_Contents"></a>

 ** EndTime **   <a name="applicationsignals-Type-MetricGraph-EndTime"></a>
The end time for the metric data included in this graph. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
Type: Timestamp
Required: No

 ** MetricDataQueries **   <a name="applicationsignals-Type-MetricGraph-MetricDataQueries"></a>
An array of metric data queries that define the metrics to be retrieved and analyzed as part of the audit finding context.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

 ** StartTime **   <a name="applicationsignals-Type-MetricGraph-StartTime"></a>
The start time for the metric data included in this graph. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
Type: Timestamp
Required: No

## See Also
<a name="API_MetricGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MetricGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MetricGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MetricGraph)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
