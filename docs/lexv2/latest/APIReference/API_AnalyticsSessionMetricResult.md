---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetricResult.html
---

# AnalyticsSessionMetricResult
<a name="API_AnalyticsSessionMetricResult"></a>

An object containing the results for a session metric you requested.

## Contents
<a name="API_AnalyticsSessionMetricResult_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsSessionMetricResult-name"></a>
The metric that you requested.
+  `Count` – The number of sessions.
+  `Success` – The number of sessions that succeeded.
+  `Failure` – The number of sessions that failed.
+  `Dropped` – The number of sessions that the user dropped.
+  `Duration` – The duration of sessions.
+  `TurnPersession` – The number of turns in the sessions.
+  `Concurrency` – The number of sessions occurring in the same period of time.
Type: String
Valid Values: `Count | Success | Failure | Dropped | Duration | TurnsPerConversation | Concurrency`
Required: No

 ** statistic **   <a name="lexv2-Type-AnalyticsSessionMetricResult-statistic"></a>
The summary statistic that you requested to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of sessions in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: No

 ** value **   <a name="lexv2-Type-AnalyticsSessionMetricResult-value"></a>
The value of the summary statistic for the metric that you requested.
Type: Double
Required: No

## See Also
<a name="API_AnalyticsSessionMetricResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsSessionMetricResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsSessionMetricResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsSessionMetricResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
