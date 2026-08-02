---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetric.html
---

# AnalyticsSessionMetric
<a name="API_AnalyticsSessionMetric"></a>

Contains the metric and the summary statistic you want to calculate, and the order in which to sort the results, for the user sessions with the bot.

## Contents
<a name="API_AnalyticsSessionMetric_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsSessionMetric-name"></a>
The metric for which you want to get session summary statistics.
+  `Count` – The number of sessions.
+  `Success` – The number of sessions that succeeded.
+  `Failure` – The number of sessions that failed.
+  `Dropped` – The number of sessions that the user dropped.
+  `Duration` – The duration of sessions.
+  `TurnsPerSession` – The number of turns in the sessions.
+  `Concurrency` – The number of sessions occurring in the same period of time.
Type: String
Valid Values: `Count | Success | Failure | Dropped | Duration | TurnsPerConversation | Concurrency`
Required: Yes

 ** statistic **   <a name="lexv2-Type-AnalyticsSessionMetric-statistic"></a>
The summary statistic to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of sessions in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: Yes

 ** order **   <a name="lexv2-Type-AnalyticsSessionMetric-order"></a>
Specifies whether to sort the results in ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## See Also
<a name="API_AnalyticsSessionMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsSessionMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsSessionMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsSessionMetric)
