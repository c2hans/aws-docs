---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetricResult.html
---

# AnalyticsIntentMetricResult
<a name="API_AnalyticsIntentMetricResult"></a>

An object containing the results for the intent metric you requested.

## Contents
<a name="API_AnalyticsIntentMetricResult_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsIntentMetricResult-name"></a>
The metric that you requested. See [Key definitions](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-key-definitions.html) for more details about these metrics.
+  `Count` – The number of times the intent was invoked.
+  `Success` – The number of times the intent succeeded.
+  `Failure` – The number of times the intent failed.
+  `Switched` – The number of times there was a switch to a different intent.
+  `Dropped` – The number of times the user dropped the intent.
Type: String
Valid Values: `Count | Success | Failure | Switched | Dropped`
Required: No

 ** statistic **   <a name="lexv2-Type-AnalyticsIntentMetricResult-statistic"></a>
The statistic that you requested to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of intents in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: No

 ** value **   <a name="lexv2-Type-AnalyticsIntentMetricResult-value"></a>
The value of the summary statistic for the metric that you requested.
Type: Double
Required: No

## See Also
<a name="API_AnalyticsIntentMetricResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsIntentMetricResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsIntentMetricResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsIntentMetricResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
