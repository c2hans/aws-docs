---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionResult.html
---

# AnalyticsSessionResult
<a name="API_AnalyticsSessionResult"></a>

An object containing the results for the session metrics you requested and the bin and/or group(s) they refer to, if applicable.

## Contents
<a name="API_AnalyticsSessionResult_Contents"></a>

 ** binKeys **   <a name="lexv2-Type-AnalyticsSessionResult-binKeys"></a>
A list of objects containing the criteria you requested for binning results and the values of the bins.
Type: Array of [AnalyticsBinKey](API_AnalyticsBinKey.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** groupByKeys **   <a name="lexv2-Type-AnalyticsSessionResult-groupByKeys"></a>
A list of objects containing the criteria you requested for grouping results and the values of the bins.
Type: Array of [AnalyticsSessionGroupByKey](API_AnalyticsSessionGroupByKey.md) objects
Required: No

 ** metricsResults **   <a name="lexv2-Type-AnalyticsSessionResult-metricsResults"></a>
A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.
Type: Array of [AnalyticsSessionMetricResult](API_AnalyticsSessionMetricResult.md) objects
Required: No

## See Also
<a name="API_AnalyticsSessionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsSessionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsSessionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsSessionResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
