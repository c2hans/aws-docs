---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetric.html
---

# AnalyticsIntentMetric
<a name="API_AnalyticsIntentMetric"></a>

Contains the metric and the summary statistic you want to calculate, and the order in which to sort the results, for the intents in the bot.

## Contents
<a name="API_AnalyticsIntentMetric_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsIntentMetric-name"></a>
The metric for which you want to get intent summary statistics.
+  `Count` – The number of times the intent was invoked.
+  `Success` – The number of times the intent succeeded.
+  `Failure` – The number of times the intent failed.
+  `Switched` – The number of times there was a switch to a different intent.
+  `Dropped` – The number of times the user dropped the intent.
Type: String
Valid Values: `Count | Success | Failure | Switched | Dropped`
Required: Yes

 ** statistic **   <a name="lexv2-Type-AnalyticsIntentMetric-statistic"></a>
The summary statistic to calculate.
+  `Sum` – The total count for the category you provide in `name`.
+  `Average` – The total count divided by the number of intents in the category you provide in `name`.
+  `Max` – The highest count in the category you provide in `name`.
Type: String
Valid Values: `Sum | Avg | Max`
Required: Yes

 ** order **   <a name="lexv2-Type-AnalyticsIntentMetric-order"></a>
Specifies whether to sort the results in ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## See Also
<a name="API_AnalyticsIntentMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsIntentMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsIntentMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsIntentMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
