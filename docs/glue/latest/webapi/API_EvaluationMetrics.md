---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EvaluationMetrics.html
---

# EvaluationMetrics
<a name="API_EvaluationMetrics"></a>

Evaluation metrics provide an estimate of the quality of your machine learning transform.

## Contents
<a name="API_EvaluationMetrics_Contents"></a>

 ** TransformType **   <a name="Glue-Type-EvaluationMetrics-TransformType"></a>
The type of machine learning transform.
Type: String
Valid Values: `FIND_MATCHES`
Required: Yes

 ** FindMatchesMetrics **   <a name="Glue-Type-EvaluationMetrics-FindMatchesMetrics"></a>
The evaluation metrics for the find matches algorithm.
Type: [FindMatchesMetrics](API_FindMatchesMetrics.md) object
Required: No

## See Also
<a name="API_EvaluationMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EvaluationMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EvaluationMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EvaluationMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
