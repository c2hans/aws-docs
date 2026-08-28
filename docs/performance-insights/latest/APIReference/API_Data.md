---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Data.html
---

# Data
<a name="API_Data"></a>

List of data objects which provide details about source metrics. This field can be used to determine the PI metric to render for the insight. This data type also includes static values for the metrics for the Insight that were calculated and included in text and annotations on the DB load chart.

## Contents
<a name="API_Data_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PerformanceInsightsMetric **   <a name="performanceinsights-Type-Data-PerformanceInsightsMetric"></a>
This field determines the Performance Insights metric to render for the insight. The `name` field refers to a Performance Insights metric.
Type: [PerformanceInsightsMetric](API_PerformanceInsightsMetric.md) object
Required: No

## See Also
<a name="API_Data_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/Data)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/Data)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/Data)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
