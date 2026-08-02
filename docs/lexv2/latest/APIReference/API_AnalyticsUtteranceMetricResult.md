---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetricResult.html
---

# AnalyticsUtteranceMetricResult
<a name="API_AnalyticsUtteranceMetricResult"></a>

An object containing the results for the utterance metric you requested.

## Contents
<a name="API_AnalyticsUtteranceMetricResult_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsUtteranceMetricResult-name"></a>
The metric that you requested.
+  `Count` – The number of utterances.
+  `Missed` – The number of utterances that Amazon Lex failed to recognize.
+  `Detected` – The number of utterances that Amazon Lex managed to detect.
+  `UtteranceTimestamp` – The date and time of the utterance.
Type: String
Valid Values: `Count | Missed | Detected | UtteranceTimestamp`
Required: No

 ** statistic **   <a name="lexv2-Type-AnalyticsUtteranceMetricResult-statistic"></a>
The summary statistic that you requested to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of utterances in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: No

 ** value **   <a name="lexv2-Type-AnalyticsUtteranceMetricResult-value"></a>
The value of the summary statistic for the metric that you requested.
Type: Double
Required: No

## See Also
<a name="API_AnalyticsUtteranceMetricResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsUtteranceMetricResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsUtteranceMetricResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsUtteranceMetricResult)
