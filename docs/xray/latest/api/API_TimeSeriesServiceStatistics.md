---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_TimeSeriesServiceStatistics.html
---

# TimeSeriesServiceStatistics
<a name="API_TimeSeriesServiceStatistics"></a>

A list of TimeSeriesStatistic structures.

## Contents
<a name="API_TimeSeriesServiceStatistics_Contents"></a>

 ** EdgeSummaryStatistics **   <a name="xray-Type-TimeSeriesServiceStatistics-EdgeSummaryStatistics"></a>
Response statistics for an edge.
Type: [EdgeStatistics](API_EdgeStatistics.md) object
Required: No

 ** ResponseTimeHistogram **   <a name="xray-Type-TimeSeriesServiceStatistics-ResponseTimeHistogram"></a>
The response time histogram for the selected entities.
Type: Array of [HistogramEntry](API_HistogramEntry.md) objects
Required: No

 ** ServiceForecastStatistics **   <a name="xray-Type-TimeSeriesServiceStatistics-ServiceForecastStatistics"></a>
The forecasted high and low fault count values.
Type: [ForecastStatistics](API_ForecastStatistics.md) object
Required: No

 ** ServiceSummaryStatistics **   <a name="xray-Type-TimeSeriesServiceStatistics-ServiceSummaryStatistics"></a>
Response statistics for a service.
Type: [ServiceStatistics](API_ServiceStatistics.md) object
Required: No

 ** Timestamp **   <a name="xray-Type-TimeSeriesServiceStatistics-Timestamp"></a>
Timestamp of the window for which statistics are aggregated.
Type: Timestamp
Required: No

## See Also
<a name="API_TimeSeriesServiceStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/TimeSeriesServiceStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/TimeSeriesServiceStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/TimeSeriesServiceStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
