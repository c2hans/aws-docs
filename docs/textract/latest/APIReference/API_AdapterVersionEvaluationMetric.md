---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_AdapterVersionEvaluationMetric.html
---

# AdapterVersionEvaluationMetric
<a name="API_AdapterVersionEvaluationMetric"></a>

Contains information on the metrics used to evalute the peformance of a given adapter version. Includes data for baseline model performance and individual adapter version perfromance.

## Contents
<a name="API_AdapterVersionEvaluationMetric_Contents"></a>

 ** AdapterVersion **   <a name="Textract-Type-AdapterVersionEvaluationMetric-AdapterVersion"></a>
The F1 score, precision, and recall metrics for the baseline model.
Type: [EvaluationMetric](API_EvaluationMetric.md) object
Required: No

 ** Baseline **   <a name="Textract-Type-AdapterVersionEvaluationMetric-Baseline"></a>
The F1 score, precision, and recall metrics for the baseline model.
Type: [EvaluationMetric](API_EvaluationMetric.md) object
Required: No

 ** FeatureType **   <a name="Textract-Type-AdapterVersionEvaluationMetric-FeatureType"></a>
Indicates the feature type being analyzed by a given adapter version.
Type: String
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`
Required: No

## See Also
<a name="API_AdapterVersionEvaluationMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/AdapterVersionEvaluationMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionEvaluationMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionEvaluationMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
