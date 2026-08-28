---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribute.html
---

# MetricAttribute
<a name="API_MetricAttribute"></a>

Contains information on a metric that a metric attribution reports on. For more information, see [Measuring impact of recommendations](https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html).

## Contents
<a name="API_MetricAttribute_Contents"></a>

 ** eventType **   <a name="personalize-Type-MetricAttribute-eventType"></a>
The metric's event type.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** expression **   <a name="personalize-Type-MetricAttribute-expression"></a>
The attribute's expression. Available functions are `SUM()` or `SAMPLECOUNT()`. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** metricName **   <a name="personalize-Type-MetricAttribute-metricName"></a>
The metric's name. The name helps you identify the metric in Amazon CloudWatch or Amazon S3.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

## See Also
<a name="API_MetricAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/MetricAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/MetricAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/MetricAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
