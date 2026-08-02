---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetricResult.html
---

# AnalyticsIntentStageMetricResult
<a name="API_AnalyticsIntentStageMetricResult"></a>

An object containing the results for an intent stage metric you requested.

## Contents
<a name="API_AnalyticsIntentStageMetricResult_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsIntentStageMetricResult-name"></a>
The metric that you requested.
+  `Count` – The number of times the intent stage occurred.
+  `Success` – The number of times the intent stage succeeded.
+  `Failure` – The number of times the intent stage failed.
+  `Dropped` – The number of times the user dropped the intent stage.
+  `Retry` – The number of times the bot tried to elicit a response from the user at this stage.
Type: String
Valid Values: `Count | Success | Failed | Dropped | Retry`
Required: No

 ** statistic **   <a name="lexv2-Type-AnalyticsIntentStageMetricResult-statistic"></a>
The summary statistic that you requested to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of intent stages in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: No

 ** value **   <a name="lexv2-Type-AnalyticsIntentStageMetricResult-value"></a>
The value of the summary statistic for the metric that you requested.
Type: Double
Required: No

## See Also
<a name="API_AnalyticsIntentStageMetricResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsIntentStageMetricResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsIntentStageMetricResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsIntentStageMetricResult)
